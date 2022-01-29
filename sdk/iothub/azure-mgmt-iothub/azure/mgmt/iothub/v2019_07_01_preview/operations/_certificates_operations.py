# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_by_iot_hub_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "certificateName": _SERIALIZER.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2019-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "certificateName": _SERIALIZER.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    *,
    if_match: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "certificateName": _SERIALIZER.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_generate_verification_code_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    *,
    if_match: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "certificateName": _SERIALIZER.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_verify_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    *,
    if_match: str,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2019-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "certificateName": _SERIALIZER.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )

class CertificatesOperations(object):
    """CertificatesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.iothub.v2019_07_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_iot_hub(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> "_models.CertificateListDescription":
        """Get the certificate list.

        Returns the list of certificates.

        :param resource_group_name: The name of the resource group that contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateListDescription, or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateListDescription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CertificateListDescription"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_by_iot_hub_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            template_url=self.list_by_iot_hub.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CertificateListDescription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_iot_hub.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        **kwargs: Any
    ) -> "_models.CertificateDescription":
        """Get the certificate.

        Returns the certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription, or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateDescription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CertificateDescription"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CertificateDescription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}'}  # type: ignore


    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        certificate_description: "_models.CertificateBodyDescription",
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.CertificateDescription":
        """Upload the certificate to the IoT hub.

        Adds new or replaces existing certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate.
        :type certificate_name: str
        :param certificate_description: The certificate body.
        :type certificate_description:
         ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateBodyDescription
        :param if_match: ETag of the Certificate. Do not specify for creating a brand new certificate.
         Required to update an existing certificate.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription, or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateDescription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CertificateDescription"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(certificate_description, 'CertificateBodyDescription')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateDescription', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('CertificateDescription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        if_match: str,
        **kwargs: Any
    ) -> None:
        """Delete an X509 certificate.

        Deletes an existing X509 certificate or does nothing if it does not exist.

        :param resource_group_name: The name of the resource group that contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate.
        :type certificate_name: str
        :param if_match: ETag of the Certificate.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            if_match=if_match,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}'}  # type: ignore


    @distributed_trace
    def generate_verification_code(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        if_match: str,
        **kwargs: Any
    ) -> "_models.CertificateWithNonceDescription":
        """Generate verification code for proof of possession flow.

        Generates verification code for proof of possession flow. The verification code will be used to
        generate a leaf certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate.
        :type certificate_name: str
        :param if_match: ETag of the Certificate.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateWithNonceDescription, or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateWithNonceDescription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CertificateWithNonceDescription"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_generate_verification_code_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            if_match=if_match,
            template_url=self.generate_verification_code.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CertificateWithNonceDescription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    generate_verification_code.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode'}  # type: ignore


    @distributed_trace
    def verify(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        if_match: str,
        certificate_verification_body: "_models.CertificateVerificationDescription",
        **kwargs: Any
    ) -> "_models.CertificateDescription":
        """Verify certificate's private key possession.

        Verifies the certificate's private key possession by providing the leaf cert issued by the
        verifying pre uploaded certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate.
        :type certificate_name: str
        :param if_match: ETag of the Certificate.
        :type if_match: str
        :param certificate_verification_body: The name of the certificate.
        :type certificate_verification_body:
         ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateVerificationDescription
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription, or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_07_01_preview.models.CertificateDescription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CertificateDescription"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(certificate_verification_body, 'CertificateVerificationDescription')

        request = build_verify_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            content_type=content_type,
            if_match=if_match,
            json=_json,
            template_url=self.verify.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CertificateDescription', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    verify.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify'}  # type: ignore

