# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor diagnostic-settings show",
)
class Show(AAZCommand):
    """Gets the active diagnostic settings for the specified resource.
    """

    _aaz_info = {
        "version": "2021-05-01-preview",
        "resources": [
            ["mgmt-plane", "/{resourceuri}/providers/microsoft.insights/diagnosticsettings/{}", "2021-05-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the diagnostic setting. Required.",
            required=True,
        )

        # define Arg Group "Target Resource"

        _args_schema = cls._args_schema
        _args_schema.resource = AAZStrArg(
            options=["--resource"],
            arg_group="Target Resource",
            help="Name or ID of the target resource.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DiagnosticSettingsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DiagnosticSettingsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceUri}/providers/Microsoft.Insights/diagnosticSettings/{name}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "name", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceUri", self.ctx.args.resource,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-05-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.event_hub_authorization_rule_id = AAZStrType(
                serialized_name="eventHubAuthorizationRuleId",
            )
            properties.event_hub_name = AAZStrType(
                serialized_name="eventHubName",
            )
            properties.log_analytics_destination_type = AAZStrType(
                serialized_name="logAnalyticsDestinationType",
            )
            properties.logs = AAZListType()
            properties.marketplace_partner_id = AAZStrType(
                serialized_name="marketplacePartnerId",
            )
            properties.metrics = AAZListType()
            properties.service_bus_rule_id = AAZStrType(
                serialized_name="serviceBusRuleId",
            )
            properties.storage_account_id = AAZStrType(
                serialized_name="storageAccountId",
            )
            properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )

            logs = cls._schema_on_200.properties.logs
            logs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.logs.Element
            _element.category = AAZStrType()
            _element.category_group = AAZStrType(
                serialized_name="categoryGroup",
            )
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.retention_policy = AAZObjectType(
                serialized_name="retentionPolicy",
            )
            _build_schema_retention_policy_read(_element.retention_policy)

            metrics = cls._schema_on_200.properties.metrics
            metrics.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.metrics.Element
            _element.category = AAZStrType()
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.retention_policy = AAZObjectType(
                serialized_name="retentionPolicy",
            )
            _build_schema_retention_policy_read(_element.retention_policy)
            _element.time_grain = AAZStrType(
                serialized_name="timeGrain",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


_schema_retention_policy_read = None


def _build_schema_retention_policy_read(_schema):
    global _schema_retention_policy_read
    if _schema_retention_policy_read is not None:
        _schema.days = _schema_retention_policy_read.days
        _schema.enabled = _schema_retention_policy_read.enabled
        return

    _schema_retention_policy_read = AAZObjectType()

    retention_policy_read = _schema_retention_policy_read
    retention_policy_read.days = AAZIntType(
        flags={"required": True},
    )
    retention_policy_read.enabled = AAZBoolType(
        flags={"required": True},
    )

    _schema.days = _schema_retention_policy_read.days
    _schema.enabled = _schema_retention_policy_read.enabled


__all__ = ["Show"]