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

from luisd.model.upsert_structured_data_response import UpsertStructuredDataResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_complex_market_data_request import UpsertComplexMarketDataRequest

from . import path

# Path params


class ScopeSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 64
        min_length = 1
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }]
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'scope': typing.Union[ScopeSchema, str, ],
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


request_path_scope = api_client.PathParameter(
    name="scope",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ScopeSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJsonPatchjson(
    schemas.DictSchema
):


    class MetaOapg:
        
        @staticmethod
        def additional_properties() -> typing.Type['UpsertComplexMarketDataRequest']:
            return UpsertComplexMarketDataRequest
    
    def __getitem__(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'UpsertComplexMarketDataRequest',
    ) -> 'SchemaForRequestBodyApplicationJsonPatchjson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        @staticmethod
        def additional_properties() -> typing.Type['UpsertComplexMarketDataRequest']:
            return UpsertComplexMarketDataRequest
    
    def __getitem__(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'UpsertComplexMarketDataRequest',
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyTextJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        @staticmethod
        def additional_properties() -> typing.Type['UpsertComplexMarketDataRequest']:
            return UpsertComplexMarketDataRequest
    
    def __getitem__(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'UpsertComplexMarketDataRequest',
    ) -> 'SchemaForRequestBodyTextJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        @staticmethod
        def additional_properties() -> typing.Type['UpsertComplexMarketDataRequest']:
            return UpsertComplexMarketDataRequest
    
    def __getitem__(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> 'UpsertComplexMarketDataRequest':
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'UpsertComplexMarketDataRequest',
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


request_body_request_body = api_client.RequestBody(
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
SchemaFor200ResponseBodyTextPlain = UpsertStructuredDataResponse
SchemaFor200ResponseBodyApplicationJson = UpsertStructuredDataResponse
SchemaFor200ResponseBodyTextJson = UpsertStructuredDataResponse


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
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, ],
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
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,dict, frozendict.frozendict, ],
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
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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

    def _upsert_complex_market_data_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = 'application/json-patch+json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        [EARLY ACCESS] UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_scope,
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
        serialized_data = request_body_request_body.serialize(body, content_type)
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


class UpsertComplexMarketData(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, ],
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
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,dict, frozendict.frozendict, ],
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
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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

    def upsert_complex_market_data(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = 'application/json-patch+json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._upsert_complex_market_data_oapg(
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyTextJson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, SchemaForRequestBodyTextJson,dict, frozendict.frozendict, SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = 'application/json-patch+json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._upsert_complex_market_data_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


