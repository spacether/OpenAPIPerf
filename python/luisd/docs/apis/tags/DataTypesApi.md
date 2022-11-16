<a name="__pageTop"></a>
# luisd.apis.tags.data_types_api.DataTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_type**](#create_data_type) | **post** /api/datatypes | [BETA] CreateDataType: Create data type definition
[**get_data_type**](#get_data_type) | **get** /api/datatypes/{scope}/{code} | [EARLY ACCESS] GetDataType: Get data type definition
[**get_units_from_data_type**](#get_units_from_data_type) | **get** /api/datatypes/{scope}/{code}/units | [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
[**list_data_type_summaries**](#list_data_type_summaries) | **get** /api/datatypes | [EXPERIMENTAL] ListDataTypeSummaries: List all data type summaries, without the reference data
[**list_data_types**](#list_data_types) | **get** /api/datatypes/{scope} | [EARLY ACCESS] ListDataTypes: List data types
[**update_data_type**](#update_data_type) | **put** /api/datatypes/{scope}/{code} | [EXPERIMENTAL] UpdateDataType: Update data type definition
[**update_reference_values**](#update_reference_values) | **put** /api/datatypes/{scope}/{code}/referencedatavalues | [EXPERIMENTAL] UpdateReferenceValues: Update reference data on a data type

# **create_data_type**
<a name="create_data_type"></a>
> DataType create_data_type()

[BETA] CreateDataType: Create data type definition

Create a new data type definition    Data types cannot be created in either the \"default\" or \"system\" scopes.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.create_data_type_request import CreateDataTypeRequest
from luisd.model.data_type import DataType
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only optional values
    body = CreateDataTypeRequest(
        scope="z",
        code="z",
        type_value_range="Open",
        display_name="Aa6w77ikCX*cKCmv|`K/V",
        description="Aa6w77ikCX*cKCmv|`K/V",
        value_type="String",
        acceptable_values=[
            "acceptable_values_example"
        ],
        unit_schema="NoUnits",
        acceptable_units=[
            CreateUnitDefinition(
                code="z",
                display_name="Aa6w77ikCX*cKCmv|`K/V",
                description="Aa6w77ikCX*cKCmv|`K/V",
                details=dict(
                    "key": "key_example",
                ),
            )
        ],
        reference_data=ReferenceData(
            field_definitions=[
                FieldDefinition(
                    key="Aa6w77ikCX*cKCmv|`K/V",
                    is_required=True,
                    is_unique=True,
                )
            ],
            values=[
                FieldValue(
                    value="Aa6w77ikCX*cKCmv|`K/V",
                    fields=dict(
                        "key": "key_example",
                    ),
                )
            ],
        ),
    )
    try:
        # [BETA] CreateDataType: Create data type definition
        api_response = api_instance.create_data_type(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->create_data_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDataTypeRequest**](../../models/CreateDataTypeRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDataTypeRequest**](../../models/CreateDataTypeRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDataTypeRequest**](../../models/CreateDataTypeRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDataTypeRequest**](../../models/CreateDataTypeRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_data_type.ApiResponseFor201) | Success
400 | [ApiResponseFor400](#create_data_type.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#create_data_type.ApiResponseForDefault) | Error response

#### create_data_type.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyTextPlain, SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


#### create_data_type.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### create_data_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_data_type**
<a name="get_data_type"></a>
> DataType get_data_type(scopecode)

[EARLY ACCESS] GetDataType: Get data type definition

Get the definition of a specified data type

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.data_type import DataType
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] GetDataType: Get data type definition
        api_response = api_instance.get_data_type(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->get_data_type: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EARLY ACCESS] GetDataType: Get data type definition
        api_response = api_instance.get_data_type(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->get_data_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asAt | AsAtSchema | | optional


# AsAtSchema

The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the data type | 

# CodeSchema

The code of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the data type | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_type.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#get_data_type.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_data_type.ApiResponseForDefault) | Error response

#### get_data_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


#### get_data_type.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### get_data_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_units_from_data_type**
<a name="get_units_from_data_type"></a>
> ResourceListOfIUnitDefinitionDto get_units_from_data_type(scopecode)

[EARLY ACCESS] GetUnitsFromDataType: Get units from data type

Get the definitions of the specified units associated bound to a specific data type

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_i_unit_definition_dto import ResourceListOfIUnitDefinitionDto
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
        api_response = api_instance.get_units_from_data_type(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->get_units_from_data_type: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'units': [
        "units_example"
    ],
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
        api_response = api_instance.get_units_from_data_type(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->get_units_from_data_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
units | UnitsSchema | | optional
filter | FilterSchema | | optional
asAt | AsAtSchema | | optional


# UnitsSchema

One or more unit identifiers for which the definition is being requested

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | One or more unit identifiers for which the definition is being requested | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FilterSchema

Optional. Expression to filter the result set.               For example, to filter on the Schema, use \"schema eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Optional. Expression to filter the result set.               For example, to filter on the Schema, use \&quot;schema eq &#x27;string&#x27;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# AsAtSchema

Optional. The as at of the requested data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | Optional. The as at of the requested data type | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the data type | 

# CodeSchema

The code of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the data type | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_units_from_data_type.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#get_units_from_data_type.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_units_from_data_type.ApiResponseForDefault) | Error response

#### get_units_from_data_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfIUnitDefinitionDto**](../../models/ResourceListOfIUnitDefinitionDto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfIUnitDefinitionDto**](../../models/ResourceListOfIUnitDefinitionDto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfIUnitDefinitionDto**](../../models/ResourceListOfIUnitDefinitionDto.md) |  | 


#### get_units_from_data_type.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### get_units_from_data_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_data_type_summaries**
<a name="list_data_type_summaries"></a>
> PagedResourceListOfDataTypeSummary list_data_type_summaries()

[EXPERIMENTAL] ListDataTypeSummaries: List all data type summaries, without the reference data

List all data type summaries

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.paged_resource_list_of_data_type_summary import PagedResourceListOfDataTypeSummary
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
        'start': 1,
        'limit': 1,
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'sortBy': [
        "sortBy_example"
    ],
    }
    try:
        # [EXPERIMENTAL] ListDataTypeSummaries: List all data type summaries, without the reference data
        api_response = api_instance.list_data_type_summaries(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->list_data_type_summaries: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asAt | AsAtSchema | | optional
page | PageSchema | | optional
start | StartSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional
sortBy | SortBySchema | | optional


# AsAtSchema

The asAt datetime at which to list the data type summaries. Defaults to returning the latest version               of each summary if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to list the data type summaries. Defaults to returning the latest version               of each summary if not specified. | value must conform to RFC-3339 date-time

# PageSchema

The pagination token to use to continue listing data type summaries. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The pagination token to use to continue listing data type summaries. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | 

# StartSchema

When paginating, skip this number of results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | When paginating, skip this number of results. | value must be a 32 bit integer

# LimitSchema

When paginating, limit the results to this number. Defaults to 100 if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | When paginating, limit the results to this number. Defaults to 100 if not specified. | value must be a 32 bit integer

# FilterSchema

Optional. Expression to filter the result set.                For example, to filter on the Scope, use \"id.scope eq 'myscope'\", to filter on Schema, use \"schema eq 'string'\",               to filter on AcceptableValues use \"acceptableValues any (~ eq 'value')\"               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Optional. Expression to filter the result set.                For example, to filter on the Scope, use \&quot;id.scope eq &#x27;myscope&#x27;\&quot;, to filter on Schema, use \&quot;schema eq &#x27;string&#x27;\&quot;,               to filter on AcceptableValues use \&quot;acceptableValues any (~ eq &#x27;value&#x27;)\&quot;               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# SortBySchema

Sort the results by these fields. Use use the '-' sign to denote descending allocation e.g. -MyFieldName.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Sort the results by these fields. Use use the &#x27;-&#x27; sign to denote descending allocation e.g. -MyFieldName. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_data_type_summaries.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#list_data_type_summaries.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#list_data_type_summaries.ApiResponseForDefault) | Error response

#### list_data_type_summaries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfDataTypeSummary**](../../models/PagedResourceListOfDataTypeSummary.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfDataTypeSummary**](../../models/PagedResourceListOfDataTypeSummary.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfDataTypeSummary**](../../models/PagedResourceListOfDataTypeSummary.md) |  | 


#### list_data_type_summaries.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### list_data_type_summaries.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_data_types**
<a name="list_data_types"></a>
> ResourceListOfDataType list_data_types(scope)

[EARLY ACCESS] ListDataTypes: List data types

List all data types in a specified scope

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_data_type import ResourceListOfDataType
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] ListDataTypes: List data types
        api_response = api_instance.list_data_types(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->list_data_types: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
        'includeSystem': True,
        'sortBy': [
        "sortBy_example"
    ],
        'start': 1,
        'limit': 1,
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
    }
    try:
        # [EARLY ACCESS] ListDataTypes: List data types
        api_response = api_instance.list_data_types(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->list_data_types: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asAt | AsAtSchema | | optional
includeSystem | IncludeSystemSchema | | optional
sortBy | SortBySchema | | optional
start | StartSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional


# AsAtSchema

The as at of the requested data types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The as at of the requested data types | value must conform to RFC-3339 date-time

# IncludeSystemSchema

Whether to additionally include those data types in the \"system\" scope

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, bool,  | NoneClass, BoolClass,  | Whether to additionally include those data types in the \&quot;system\&quot; scope | 

# SortBySchema

Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Optional. Order the results by these fields. Use use the &#x27;-&#x27; sign to denote descending order e.g. -MyFieldName | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StartSchema

Optional. When paginating, skip this number of results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Optional. When paginating, skip this number of results | value must be a 32 bit integer

# LimitSchema

Optional. When paginating, limit the number of returned results to this many.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Optional. When paginating, limit the number of returned results to this many. | value must be a 32 bit integer

# FilterSchema

Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \&quot;displayName eq &#x27;string&#x27;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The requested scope of the data types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The requested scope of the data types | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_data_types.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#list_data_types.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#list_data_types.ApiResponseForDefault) | Error response

#### list_data_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfDataType**](../../models/ResourceListOfDataType.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfDataType**](../../models/ResourceListOfDataType.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfDataType**](../../models/ResourceListOfDataType.md) |  | 


#### list_data_types.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### list_data_types.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_data_type**
<a name="update_data_type"></a>
> DataType update_data_type(scopecodeupdate_data_type_request)

[EXPERIMENTAL] UpdateDataType: Update data type definition

Update the definition of the specified existing data type    Not all elements within a data type definition are modifiable due to the potential implications for data  already stored against the types

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.data_type import DataType
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.update_data_type_request import UpdateDataTypeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    body = UpdateDataTypeRequest(
        display_name="Aa6w77ikCX*cKCmv|`K/V",
        description="Aa6w77ikCX*cKCmv|`K/V",
        acceptable_values=[
            "acceptable_values_example"
        ],
        acceptable_units=[
            UpdateUnitRequest(
                code="z",
                display_name="Aa6w77ikCX*cKCmv|`K/V",
                description="Aa6w77ikCX*cKCmv|`K/V",
            )
        ],
    )
    try:
        # [EXPERIMENTAL] UpdateDataType: Update data type definition
        api_response = api_instance.update_data_type(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->update_data_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateDataTypeRequest**](../../models/UpdateDataTypeRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateDataTypeRequest**](../../models/UpdateDataTypeRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateDataTypeRequest**](../../models/UpdateDataTypeRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateDataTypeRequest**](../../models/UpdateDataTypeRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the data type | 

# CodeSchema

The code of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the data type | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_data_type.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#update_data_type.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#update_data_type.ApiResponseForDefault) | Error response

#### update_data_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


#### update_data_type.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### update_data_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_reference_values**
<a name="update_reference_values"></a>
> DataType update_reference_values(scopecodefield_value)

[EXPERIMENTAL] UpdateReferenceValues: Update reference data on a data type

Replaces the whole set of reference values

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import data_types_api
from luisd.model.data_type import DataType
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.field_value import FieldValue
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    body = [{"value":"FRA","fields":{"english_short_name":"France","continent":"Europe"}},{"value":"DEU","fields":{"english_short_name":"Germany","continent":"Europe"}}]
    try:
        # [EXPERIMENTAL] UpdateReferenceValues: Update reference data on a data type
        api_response = api_instance.update_reference_values(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling DataTypesApi->update_reference_values: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

The updated reference values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The updated reference values | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) |  | 

# SchemaForRequestBodyApplicationJson

The updated reference values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The updated reference values | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) |  | 

# SchemaForRequestBodyTextJson

The updated reference values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The updated reference values | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) |  | 

# SchemaForRequestBodyApplicationJson

The updated reference values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The updated reference values | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) | [**FieldValue**]({{complexTypePrefix}}FieldValue.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the data type | 

# CodeSchema

The code of the data type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the data type | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_reference_values.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#update_reference_values.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#update_reference_values.ApiResponseForDefault) | Error response

#### update_reference_values.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataType**](../../models/DataType.md) |  | 


#### update_reference_values.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](../../models/LusidValidationProblemDetails.md) |  | 


#### update_reference_values.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](../../models/LusidProblemDetails.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

