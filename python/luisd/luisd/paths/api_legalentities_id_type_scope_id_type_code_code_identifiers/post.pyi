# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from luisd import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from luisd import schemas  # noqa: F401

from luisd.model.legal_entity import LegalEntity
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.set_legal_entity_identifiers_request import SetLegalEntityIdentifiersRequest

# Path params


class IdTypeScopeSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdTypeScopeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class IdTypeCodeSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdTypeCodeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class CodeSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CodeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idTypeScope': typing.Union[IdTypeScopeSchema, None, str, ],
        'idTypeCode': typing.Union[IdTypeCodeSchema, None, str, ],
        'code': typing.Union[CodeSchema, None, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id_type_scope = api_client.PathParameter(
    name="idTypeScope",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdTypeScopeSchema,
    required=True,
)
request_path_id_type_code = api_client.PathParameter(
    name="idTypeCode",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdTypeCodeSchema,
    required=True,
)
request_path_code = api_client.PathParameter(
    name="code",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CodeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJsonPatchjson = SetLegalEntityIdentifiersRequest
SchemaForRequestBodyApplicationJson = SetLegalEntityIdentifiersRequest
SchemaForRequestBodyTextJson = SetLegalEntityIdentifiersRequest
SchemaForRequestBodyApplicationJson = SetLegalEntityIdentifiersRequest


request_body_set_legal_entity_identifiers_request = api_client.RequestBody(
    content={
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyTextPlain = LegalEntity
SchemaFor200ResponseBodyApplicationJson = LegalEntity
SchemaFor200ResponseBodyTextJson = LegalEntity


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyTextPlain,
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyTextJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
    },
)
SchemaFor400ResponseBodyTextPlain = LusidValidationProblemDetails
SchemaFor400ResponseBodyApplicationJson = LusidValidationProblemDetails
SchemaFor400ResponseBodyTextJson = LusidValidationProblemDetails


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyTextPlain,
        SchemaFor400ResponseBodyApplicationJson,
        SchemaFor400ResponseBodyTextJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = LusidProblemDetails


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'text/plain',
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,],
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,],
        content_type: typing_extensions.Literal["text/json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/*+json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...


    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _set_legal_entity_identifiers_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = 'application/json-patch+json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        [EXPERIMENTAL] SetLegalEntityIdentifiers: Set Legal Entity Identifiers
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_id_type_scope,
            request_path_id_type_code,
            request_path_code,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_set_legal_entity_identifiers_request.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                default_response = _status_code_to_response.get('default')
                if default_response:
                    api_response = default_response.deserialize(response, self.api_client.configuration)
                else:
                    api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class SetLegalEntityIdentifiers(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,],
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,],
        content_type: typing_extensions.Literal["text/json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/*+json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...


    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def set_legal_entity_identifiers(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = 'application/json-patch+json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._set_legal_entity_identifiers_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,],
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,],
        content_type: typing_extensions.Literal["text/json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/*+json"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...


    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationJson,],
        content_type: str = 'application/json-patch+json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._set_legal_entity_identifiers_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


