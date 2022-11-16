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

from luisd.model.paged_resource_list_of_legal_entity import PagedResourceListOfLegalEntity
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails

# Query params


class EffectiveAtSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'dateorcutlabel'


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EffectiveAtSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class AsAtSchema(
    schemas.DateTimeBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date-time'


    def __new__(
        cls,
        *args: typing.Union[None, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AsAtSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class PageSchema(
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
    ) -> 'PageSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class LimitSchema(
    schemas.Int32Base,
    schemas.IntBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneDecimalMixin
):


    class MetaOapg:
        format = 'int32'


    def __new__(
        cls,
        *args: typing.Union[None, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LimitSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class FilterSchema(
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
    ) -> 'FilterSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class PropertyKeysSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PropertyKeysSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'effectiveAt': typing.Union[EffectiveAtSchema, None, str, ],
        'asAt': typing.Union[AsAtSchema, None, str, datetime, ],
        'page': typing.Union[PageSchema, None, str, ],
        'limit': typing.Union[LimitSchema, None, decimal.Decimal, int, ],
        'filter': typing.Union[FilterSchema, None, str, ],
        'propertyKeys': typing.Union[PropertyKeysSchema, list, tuple, None, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_effective_at = api_client.QueryParameter(
    name="effectiveAt",
    style=api_client.ParameterStyle.FORM,
    schema=EffectiveAtSchema,
    explode=True,
)
request_query_as_at = api_client.QueryParameter(
    name="asAt",
    style=api_client.ParameterStyle.FORM,
    schema=AsAtSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_property_keys = api_client.QueryParameter(
    name="propertyKeys",
    style=api_client.ParameterStyle.FORM,
    schema=PropertyKeysSchema,
    explode=True,
)
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
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idTypeScope': typing.Union[IdTypeScopeSchema, None, str, ],
        'idTypeCode': typing.Union[IdTypeCodeSchema, None, str, ],
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
SchemaFor200ResponseBodyTextPlain = PagedResourceListOfLegalEntity
SchemaFor200ResponseBodyApplicationJson = PagedResourceListOfLegalEntity
SchemaFor200ResponseBodyTextJson = PagedResourceListOfLegalEntity


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
    def _list_legal_entities_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
    def _list_legal_entities_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _list_legal_entities_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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

    def _list_legal_entities_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        [EARLY ACCESS] ListLegalEntities: List Legal Entities
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_id_type_scope,
            request_path_id_type_code,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_effective_at,
            request_query_as_at,
            request_query_page,
            request_query_limit,
            request_query_filter,
            request_query_property_keys,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
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


class ListLegalEntities(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def list_legal_entities(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
    def list_legal_entities(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def list_legal_entities(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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

    def list_legal_entities(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_legal_entities_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_legal_entities_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


