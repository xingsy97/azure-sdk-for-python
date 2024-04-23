# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from ._configuration import CdnManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AFDCustomDomainsOperations,
    AFDEndpointsOperations,
    AFDOriginGroupsOperations,
    AFDOriginsOperations,
    AFDProfilesOperations,
    CdnManagementClientOperationsMixin,
    CustomDomainsOperations,
    EdgeNodesOperations,
    EndpointsOperations,
    LogAnalyticsOperations,
    ManagedRuleSetsOperations,
    Operations,
    OriginGroupsOperations,
    OriginsOperations,
    PoliciesOperations,
    ProfilesOperations,
    ResourceUsageOperations,
    RoutesOperations,
    RuleSetsOperations,
    RulesOperations,
    SecretsOperations,
    SecurityPoliciesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class CdnManagementClient(
    CdnManagementClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Cdn Management Client.

    :ivar afd_profiles: AFDProfilesOperations operations
    :vartype afd_profiles: azure.mgmt.cdn.operations.AFDProfilesOperations
    :ivar afd_custom_domains: AFDCustomDomainsOperations operations
    :vartype afd_custom_domains: azure.mgmt.cdn.operations.AFDCustomDomainsOperations
    :ivar afd_endpoints: AFDEndpointsOperations operations
    :vartype afd_endpoints: azure.mgmt.cdn.operations.AFDEndpointsOperations
    :ivar afd_origin_groups: AFDOriginGroupsOperations operations
    :vartype afd_origin_groups: azure.mgmt.cdn.operations.AFDOriginGroupsOperations
    :ivar afd_origins: AFDOriginsOperations operations
    :vartype afd_origins: azure.mgmt.cdn.operations.AFDOriginsOperations
    :ivar routes: RoutesOperations operations
    :vartype routes: azure.mgmt.cdn.operations.RoutesOperations
    :ivar rule_sets: RuleSetsOperations operations
    :vartype rule_sets: azure.mgmt.cdn.operations.RuleSetsOperations
    :ivar rules: RulesOperations operations
    :vartype rules: azure.mgmt.cdn.operations.RulesOperations
    :ivar security_policies: SecurityPoliciesOperations operations
    :vartype security_policies: azure.mgmt.cdn.operations.SecurityPoliciesOperations
    :ivar secrets: SecretsOperations operations
    :vartype secrets: azure.mgmt.cdn.operations.SecretsOperations
    :ivar log_analytics: LogAnalyticsOperations operations
    :vartype log_analytics: azure.mgmt.cdn.operations.LogAnalyticsOperations
    :ivar profiles: ProfilesOperations operations
    :vartype profiles: azure.mgmt.cdn.operations.ProfilesOperations
    :ivar endpoints: EndpointsOperations operations
    :vartype endpoints: azure.mgmt.cdn.operations.EndpointsOperations
    :ivar origins: OriginsOperations operations
    :vartype origins: azure.mgmt.cdn.operations.OriginsOperations
    :ivar origin_groups: OriginGroupsOperations operations
    :vartype origin_groups: azure.mgmt.cdn.operations.OriginGroupsOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains: azure.mgmt.cdn.operations.CustomDomainsOperations
    :ivar resource_usage: ResourceUsageOperations operations
    :vartype resource_usage: azure.mgmt.cdn.operations.ResourceUsageOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cdn.operations.Operations
    :ivar edge_nodes: EdgeNodesOperations operations
    :vartype edge_nodes: azure.mgmt.cdn.operations.EdgeNodesOperations
    :ivar policies: PoliciesOperations operations
    :vartype policies: azure.mgmt.cdn.operations.PoliciesOperations
    :ivar managed_rule_sets: ManagedRuleSetsOperations operations
    :vartype managed_rule_sets: azure.mgmt.cdn.operations.ManagedRuleSetsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Azure Subscription ID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2024-02-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = CdnManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.afd_profiles = AFDProfilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.afd_custom_domains = AFDCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.afd_endpoints = AFDEndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.afd_origin_groups = AFDOriginGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.afd_origins = AFDOriginsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.routes = RoutesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.rule_sets = RuleSetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.rules = RulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.security_policies = SecurityPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.secrets = SecretsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.log_analytics = LogAnalyticsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.profiles = ProfilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.origins = OriginsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.origin_groups = OriginGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.resource_usage = ResourceUsageOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.edge_nodes = EdgeNodesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.managed_rule_sets = ManagedRuleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "CdnManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
