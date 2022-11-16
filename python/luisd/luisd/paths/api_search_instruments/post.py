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

from luisd.model.instrument_search_property import InstrumentSearchProperty
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.instrument_match import InstrumentMatch
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails

from . import path

# Query params


class MasteredEffectiveAtSchema(
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
    ) -> 'MasteredEffectiveAtSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
MasteredOnlySchema = schemas.BoolSchema


class ScopeSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        max_length = 64
        min_length = 1
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }]


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ScopeSchema':
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
        'masteredEffectiveAt': typing.Union[MasteredEffectiveAtSchema, None, str, ],
        'masteredOnly': typing.Union[MasteredOnlySchema, bool, ],
        'scope': typing.Union[ScopeSchema, None, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_mastered_effective_at = api_client.QueryParameter(
    name="masteredEffectiveAt",
    style=api_client.ParameterStyle.FORM,
    schema=MasteredEffectiveAtSchema,
    explode=True,
)
request_query_mastered_only = api_client.QueryParameter(
    name="masteredOnly",
    style=api_client.ParameterStyle.FORM,
    schema=MasteredOnlySchema,
    explode=True,
)
request_query_scope = api_client.QueryParameter(
    name="scope",
    style=api_client.ParameterStyle.FORM,
    schema=ScopeSchema,
    explode=True,
)
# body param


class SchemaForRequestBodyApplicationJsonPatchjson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentSearchProperty']:
            return InstrumentSearchProperty

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentSearchProperty'], typing.List['InstrumentSearchProperty']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyApplicationJsonPatchjson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentSearchProperty':
        return super().__getitem__(i)


class SchemaForRequestBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentSearchProperty']:
            return InstrumentSearchProperty

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentSearchProperty'], typing.List['InstrumentSearchProperty']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentSearchProperty':
        return super().__getitem__(i)


class SchemaForRequestBodyTextJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentSearchProperty']:
            return InstrumentSearchProperty

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentSearchProperty'], typing.List['InstrumentSearchProperty']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyTextJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentSearchProperty':
        return super().__getitem__(i)


class SchemaForRequestBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentSearchProperty']:
            return InstrumentSearchProperty

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentSearchProperty'], typing.List['InstrumentSearchProperty']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentSearchProperty':
        return super().__getitem__(i)


request_body_instrument_search_property = api_client.RequestBody(
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
_auth = [
    'oauth2',
]


class SchemaFor200ResponseBodyTextPlain(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentMatch']:
            return InstrumentMatch

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentMatch'], typing.List['InstrumentMatch']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyTextPlain':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentMatch':
        return super().__getitem__(i)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentMatch']:
            return InstrumentMatch

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentMatch'], typing.List['InstrumentMatch']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentMatch':
        return super().__getitem__(i)


class SchemaFor200ResponseBodyTextJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InstrumentMatch']:
            return InstrumentMatch

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InstrumentMatch'], typing.List['InstrumentMatch']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyTextJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InstrumentMatch':
        return super().__getitem__(i)


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'text/plain',
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, ],
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: typing_extensions.Literal["application/json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,list, tuple, ],
        content_type: typing_extensions.Literal["text/json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: typing_extensions.Literal["application/*+json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...


    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _instruments_search_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = 'application/json-patch+json',
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        [EXPERIMENTAL] InstrumentsSearch: Instruments search
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_mastered_effective_at,
            request_query_mastered_only,
            request_query_scope,
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

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_instrument_search_property.serialize(body, content_type)
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


class InstrumentsSearch(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, ],
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: typing_extensions.Literal["application/json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,list, tuple, ],
        content_type: typing_extensions.Literal["text/json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: typing_extensions.Literal["application/*+json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...


    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def instruments_search(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = 'application/json-patch+json',
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._instruments_search_oapg(
            body=body,
            query_params=query_params,
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, ],
        content_type: typing_extensions.Literal["application/json-patch+json"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        body: typing.Union[SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: typing_extensions.Literal["application/json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        body: typing.Union[SchemaForRequestBodyTextJson,list, tuple, ],
        content_type: typing_extensions.Literal["text/json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        body: typing.Union[SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: typing_extensions.Literal["application/*+json"],
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, SchemaForRequestBodyTextJson,list, tuple, SchemaForRequestBodyApplicationJson,list, tuple, ],
        content_type: str = 'application/json-patch+json',
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._instruments_search_oapg(
            body=body,
            query_params=query_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


