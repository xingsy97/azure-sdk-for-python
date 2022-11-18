# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
# pylint: disable=protected-access
import copy

import yaml
from marshmallow import INCLUDE, ValidationError, post_load, pre_load

from azure.ai.ml._schema import CommandJobSchema, AnonymousEnvironmentSchema
from azure.ai.ml._schema.core.fields import (
    ArmStr,
    FileRefField,
    NestedField,
    StringTransformedEnum,
    UnionField,
    ComputeField,
    RegistryStr,
    ArmVersionedStr,
)
from azure.ai.ml._schema.job import BaseJobSchema
from azure.ai.ml._schema.job.input_output_fields_provider import InputsField, OutputsField
from azure.ai.ml._schema.pipeline.settings import PipelineJobSettingsSchema
from azure.ai.ml._utils.utils import load_file
from azure.ai.ml.constants import JobType
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY, AzureMLResourceType

_SCHEDULED_JOB_UPDATES_KEY = "scheduled_job_updates"


class CreateJobFileRefField(FileRefField):
    def _serialize(self, value, attr, obj, **kwargs):
        """FileRefField does not support serialize.

        This function is overwrite because we need job can be dumped inside schedule.
        """
        from azure.ai.ml.entities._builders import BaseNode
        if isinstance(value, BaseNode):
            # Dump as Job to avoid missing field.
            value = value._to_job()
        return value._to_dict()

    def _deserialize(self, value, attr, data, **kwargs) -> "Job":
        # Get component info from component yaml file.
        data = super()._deserialize(value, attr, data, **kwargs)
        job_dict = yaml.safe_load(data)

        from azure.ai.ml.entities import Job

        return Job._load(  # pylint: disable=no-member
            data=job_dict,
            yaml_path=self.context[BASE_PATH_CONTEXT_KEY] / value,
            **kwargs,
        )


class BaseCreateJobSchema(BaseJobSchema):
    compute = ComputeField()
    job = UnionField(
        [
            ArmStr(azureml_type=AzureMLResourceType.JOB),
            CreateJobFileRefField,
        ],
        required=True,
    )

    def _get_job_instance_for_remote_job(self, id, data, **kwargs):  # pylint: disable=redefined-builtin
        """Get a job instance to store updates for remote job."""
        from azure.ai.ml.entities import Job

        data = {} if data is None else data
        if "type" not in data:
            raise ValidationError("'type' must be specified when scheduling a remote job with updates.")
        # Create a job instance if job is arm id
        job_instance = Job._load(  # pylint: disable=no-member
            data=data,
            **kwargs,
        )
        # Set back the id and base path to created job
        job_instance._id = id
        job_instance._base_path = self.context[BASE_PATH_CONTEXT_KEY]  # pylint: disable=no-member
        return job_instance

    @pre_load
    def pre_load(self, data, **kwargs):  # pylint: disable=unused-argument
        if isinstance(data, dict):
            # Put the raw replicas into context.
            # dict type indicates there are updates to the scheduled job.
            copied_data = copy.deepcopy(data)
            copied_data.pop("job", None)
            self.context[_SCHEDULED_JOB_UPDATES_KEY] = copied_data  # pylint: disable=no-member
        return data

    @post_load
    def make(self, data: dict, **kwargs) -> "Job":
        from azure.ai.ml.entities import Job

        # Get the loaded job
        job = data.pop("job")
        # Get the raw dict data before load
        raw_data = self.context.get(_SCHEDULED_JOB_UPDATES_KEY, {})  # pylint: disable=no-member
        if isinstance(job, Job):

            if job._source_path is None:
                raise ValidationError("Could not load job for schedule without '_source_path' set.")
            # Load local job again with updated values
            job_dict = yaml.safe_load(load_file(job._source_path))
            return Job._load(  # pylint: disable=no-member
                data={**job_dict, **raw_data},
                yaml_path=job._source_path,
                **kwargs,
            )
        # Create a job instance for remote job
        return self._get_job_instance_for_remote_job(job, raw_data, **kwargs)


class PipelineCreateJobSchema(BaseCreateJobSchema):
    # Note: Here we do not inherit PipelineJobSchema, as we don't need the post_load, pre_load inside.
    type = StringTransformedEnum(allowed_values=[JobType.PIPELINE])
    inputs = InputsField()
    outputs = OutputsField()
    settings = NestedField(PipelineJobSettingsSchema, unknown=INCLUDE)


class CommandCreateJobSchema(BaseCreateJobSchema, CommandJobSchema):
    class Meta:
        # Refer to https://github.com/Azure/azureml_run_specification/blob/master
        #   /specs/job-endpoint.md#properties-in-difference-job-types
        # code and command can not be set during runtime
        exclude = ["code", "command"]
    environment = UnionField(
        [
            NestedField(AnonymousEnvironmentSchema),
            RegistryStr(azureml_type=AzureMLResourceType.ENVIRONMENT),
            ArmVersionedStr(azureml_type=AzureMLResourceType.ENVIRONMENT, allow_default_version=True),
        ],
    )
