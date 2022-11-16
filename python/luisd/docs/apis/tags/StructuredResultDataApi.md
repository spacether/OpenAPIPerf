<a name="__pageTop"></a>
# luisd.apis.tags.structured_result_data_api.StructuredResultDataApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_map**](#create_data_map) | **post** /api/unitresults/datamap/{scope} | [EXPERIMENTAL] CreateDataMap: Create data map
[**delete_structured_result_data**](#delete_structured_result_data) | **post** /api/unitresults/{scope}/$delete | [EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data
[**get_data_map**](#get_data_map) | **post** /api/unitresults/datamap/{scope}/$get | [EXPERIMENTAL] GetDataMap: Get data map
[**get_structured_result_data**](#get_structured_result_data) | **post** /api/unitresults/{scope}/$get | [EXPERIMENTAL] GetStructuredResultData: Get structured result data
[**get_virtual_document**](#get_virtual_document) | **post** /api/unitresults/virtualdocument/{scope}/$get | [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
[**upsert_structured_result_data**](#upsert_structured_result_data) | **post** /api/unitresults/{scope} | [BETA] UpsertStructuredResultData: Upsert structured result data

# **create_data_map**
<a name="create_data_map"></a>
> UpsertStructuredDataResponse create_data_map(scoperequest_body)

[EXPERIMENTAL] CreateDataMap: Create data map

Create or update one or more structured result store address definition data maps in a particular scope. Note these are immutable and cannot be changed once created.                In the request, each data map must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data map object in the response.                The response returns both the collection of successfully created or updated data maps, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import structured_result_data_api
from luisd.model.upsert_structured_data_response import UpsertStructuredDataResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.create_data_map_request import CreateDataMapRequest
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
    api_instance = structured_result_data_api.StructuredResultDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    body = dict(
        "key": CreateDataMapRequest(
            id=DataMapKey(
                version="4.072888001528021798096225500850762068629.9333975650685139102691291732729478",
                code="z",
            ),
            data=DataMapping(
                data_definitions=[
                    DataDefinition(
                        address="address_example",
                        name="z",
                        data_type="data_type_example",
                        key_type="key_type_example",
                    )
                ],
            ),
        ),
    )
    try:
        # [EXPERIMENTAL] CreateDataMap: Create data map
        api_response = api_instance.create_data_map(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->create_data_map: %s\n" % e)
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

Individual data map creation requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Individual data map creation requests. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

Individual data map creation requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Individual data map creation requests. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyTextJson

Individual data map creation requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Individual data map creation requests. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

Individual data map creation requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Individual data map creation requests. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | [**CreateDataMapRequest**]({{complexTypePrefix}}CreateDataMapRequest.md) | any string name can be used but the value must be the correct type | [optional] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The scope in which to create or update data maps.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope in which to create or update data maps. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_data_map.ApiResponseFor200) | The successfully created or updated data maps along with any failures.
400 | [ApiResponseFor400](#create_data_map.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#create_data_map.ApiResponseForDefault) | Error response

#### create_data_map.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertStructuredDataResponse**](../../models/UpsertStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertStructuredDataResponse**](../../models/UpsertStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertStructuredDataResponse**](../../models/UpsertStructuredDataResponse.md) |  | 


#### create_data_map.ApiResponseFor400
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


#### create_data_map.ApiResponseForDefault
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

# **delete_structured_result_data**
<a name="delete_structured_result_data"></a>
> AnnulStructuredDataResponse delete_structured_result_data(scoperequest_body)

[EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data

Delete one or more structured result data items from a particular scope. Each item is identified by a unique ID which includes  information about its type as well as the exact effective datetime (to the microsecond) at which it entered the system (became valid).                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully deleted data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import structured_result_data_api
from luisd.model.annul_structured_data_response import AnnulStructuredDataResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.structured_result_data_id import StructuredResultDataId
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
    api_instance = structured_result_data_api.StructuredResultDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    body = dict(
        "key": StructuredResultDataId(
            source="z",
            code="z",
            effective_at="effective_at_example",
            result_type="result_type_example",
        ),
    )
    try:
        # [EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data
        api_response = api_instance.delete_structured_result_data(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->delete_structured_result_data: %s\n" % e)
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

The data IDs to delete, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data IDs to delete, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The data IDs to delete, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data IDs to delete, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyTextJson

The data IDs to delete, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data IDs to delete, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The data IDs to delete, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data IDs to delete, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The scope from which to delete data items.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope from which to delete data items. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_structured_result_data.ApiResponseFor200) | The successfully deleted data items along with any failures.
400 | [ApiResponseFor400](#delete_structured_result_data.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#delete_structured_result_data.ApiResponseForDefault) | Error response

#### delete_structured_result_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulStructuredDataResponse**](../../models/AnnulStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulStructuredDataResponse**](../../models/AnnulStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulStructuredDataResponse**](../../models/AnnulStructuredDataResponse.md) |  | 


#### delete_structured_result_data.ApiResponseFor400
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


#### delete_structured_result_data.ApiResponseForDefault
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

# **get_data_map**
<a name="get_data_map"></a>
> GetDataMapResponse get_data_map(scoperequest_body)

[EXPERIMENTAL] GetDataMap: Get data map

Retrieve one or more structured result store address definition data maps from a particular scope.                Each data map can be identified by its invariant key, which can be thought of as a permanent URL.  For each ID, LUSID returns the most recently matched item.                In the request, each data map must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data map in the response.                The response returns three collections. The first contains successfully retrieved data maps. The second contains those with a  valid identifier but that could not be found. The third contains those that failed because LUSID could not construct a valid identifier from the request.                For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import structured_result_data_api
from luisd.model.get_data_map_response import GetDataMapResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.data_map_key import DataMapKey
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
    api_instance = structured_result_data_api.StructuredResultDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    body = dict(
        "key": DataMapKey(
            version="4.072888001528021798096225500850762068629.9333975650685139102691291732729478",
            code="z",
        ),
    )
    try:
        # [EXPERIMENTAL] GetDataMap: Get data map
        api_response = api_instance.get_data_map(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_data_map: %s\n" % e)
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

The data map keys to look up, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data map keys to look up, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The data map keys to look up, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data map keys to look up, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyTextJson

The data map keys to look up, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data map keys to look up, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The data map keys to look up, each keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data map keys to look up, each keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | [**DataMapKey**]({{complexTypePrefix}}DataMapKey.md) | any string name can be used but the value must be the correct type | [optional] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The scope from which to retrieve data maps.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope from which to retrieve data maps. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_map.ApiResponseFor200) | The successfully retrieved data maps along with any failures.
400 | [ApiResponseFor400](#get_data_map.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_data_map.ApiResponseForDefault) | Error response

#### get_data_map.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GetDataMapResponse**](../../models/GetDataMapResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetDataMapResponse**](../../models/GetDataMapResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetDataMapResponse**](../../models/GetDataMapResponse.md) |  | 


#### get_data_map.ApiResponseFor400
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


#### get_data_map.ApiResponseForDefault
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

# **get_structured_result_data**
<a name="get_structured_result_data"></a>
> GetStructuredResultDataResponse get_structured_result_data(scoperequest_body)

[EXPERIMENTAL] GetStructuredResultData: Get structured result data

Retrieve one or more structured result data items from a particular scope.                Each item can be identified by its time invariant structured result data identifier. For each ID, LUSID  returns the most recently matched item with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified to control how far back to look from the specified  effective datetime. LUSID returns the most recent item within this window.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.    The response returns three collections. The first contains successfully retrieved data items. The second contains those with a  valid identifier but that could not be found. The third contains those that failed because LUSID could not construct a valid identifier from the request.    For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import structured_result_data_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.structured_result_data_id import StructuredResultDataId
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.get_structured_result_data_response import GetStructuredResultDataResponse
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
    api_instance = structured_result_data_api.StructuredResultDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    query_params = {
    }
    body = dict(
        "key": StructuredResultDataId(
            source="z",
            code="z",
            effective_at="effective_at_example",
            result_type="result_type_example",
        ),
    )
    try:
        # [EXPERIMENTAL] GetStructuredResultData: Get structured result data
        api_response = api_instance.get_structured_result_data(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_structured_result_data: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
        'maxAge': "maxAge_example",
    }
    body = dict(
        "key": StructuredResultDataId(
            source="z",
            code="z",
            effective_at="effective_at_example",
            result_type="result_type_example",
        ),
    )
    try:
        # [EXPERIMENTAL] GetStructuredResultData: Get structured result data
        api_response = api_instance.get_structured_result_data(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_structured_result_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyTextJson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asAt | AsAtSchema | | optional
maxAge | MaxAgeSchema | | optional


# AsAtSchema

The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. | value must conform to RFC-3339 date-time

# MaxAgeSchema

The duration of the look-back window in ISO8601 time interval format, for example 'P1Y2M3DT4H30M' (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a data item must exist to be retrieved.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The duration of the look-back window in ISO8601 time interval format, for example &#x27;P1Y2M3DT4H30M&#x27; (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a data item must exist to be retrieved. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The scope from which to retrieve data items.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope from which to retrieve data items. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_structured_result_data.ApiResponseFor200) | The successfully retrieved data items along with any failures.
400 | [ApiResponseFor400](#get_structured_result_data.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_structured_result_data.ApiResponseForDefault) | Error response

#### get_structured_result_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GetStructuredResultDataResponse**](../../models/GetStructuredResultDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetStructuredResultDataResponse**](../../models/GetStructuredResultDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetStructuredResultDataResponse**](../../models/GetStructuredResultDataResponse.md) |  | 


#### get_structured_result_data.ApiResponseFor400
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


#### get_structured_result_data.ApiResponseForDefault
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

# **get_virtual_document**
<a name="get_virtual_document"></a>
> GetVirtualDocumentResponse get_virtual_document(scoperequest_body)

[EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents

Retrieve one or more virtual documents from a particular scope.                Each item can be identified by its time invariant structured result data identifier. For each ID, LUSID  returns the most recently matched item with respect to the provided effective datetime.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns two collections. The first contains successfully retrieved data items. The second contains those with a  valid identifier but that could not be found, or those that failed because LUSID could not construct a valid identifier from the request.                For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import structured_result_data_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.structured_result_data_id import StructuredResultDataId
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.get_virtual_document_response import GetVirtualDocumentResponse
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
    api_instance = structured_result_data_api.StructuredResultDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    query_params = {
    }
    body = dict(
        "key": StructuredResultDataId(
            source="z",
            code="z",
            effective_at="effective_at_example",
            result_type="result_type_example",
        ),
    )
    try:
        # [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
        api_response = api_instance.get_virtual_document(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_virtual_document: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    body = dict(
        "key": StructuredResultDataId(
            source="z",
            code="z",
            effective_at="effective_at_example",
            result_type="result_type_example",
        ),
    )
    try:
        # [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
        api_response = api_instance.get_virtual_document(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->get_virtual_document: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyTextJson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | [**StructuredResultDataId**]({{complexTypePrefix}}StructuredResultDataId.md) | any string name can be used but the value must be the correct type | [optional] 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asAt | AsAtSchema | | optional


# AsAtSchema

The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The scope in which to construct the virtual documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope in which to construct the virtual documents. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_virtual_document.ApiResponseFor200) | The successfully retrieved virtual documents along with any failures.
400 | [ApiResponseFor400](#get_virtual_document.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_virtual_document.ApiResponseForDefault) | Error response

#### get_virtual_document.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GetVirtualDocumentResponse**](../../models/GetVirtualDocumentResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetVirtualDocumentResponse**](../../models/GetVirtualDocumentResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetVirtualDocumentResponse**](../../models/GetVirtualDocumentResponse.md) |  | 


#### get_virtual_document.ApiResponseFor400
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


#### get_virtual_document.ApiResponseForDefault
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

# **upsert_structured_result_data**
<a name="upsert_structured_result_data"></a>
> UpsertStructuredDataResponse upsert_structured_result_data(scoperequest_body)

[BETA] UpsertStructuredResultData: Upsert structured result data

Create or update one or more structured result data items in a particular scope. An item is updated if it already exists  and created if it does not.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully created or updated data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import structured_result_data_api
from luisd.model.upsert_structured_data_response import UpsertStructuredDataResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_structured_result_data_request import UpsertStructuredResultDataRequest
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
    api_instance = structured_result_data_api.StructuredResultDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
    }
    body = dict(
        "key": UpsertStructuredResultDataRequest(
            id=StructuredResultDataId(
                source="z",
                code="z",
                effective_at="effective_at_example",
                result_type="result_type_example",
            ),
            data=StructuredResultData(
                document_format="document_format_example",
                version="version_example",
                name="name_example",
                document="document_example",
                data_map_key=DataMapKey(
                    version="4.072888001528021798096225500850762068629.9333975650685139102691291732729478",
                    code="z",
                ),
            ),
        ),
    )
    try:
        # [BETA] UpsertStructuredResultData: Upsert structured result data
        api_response = api_instance.upsert_structured_result_data(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling StructuredResultDataApi->upsert_structured_result_data: %s\n" % e)
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

The set of data items to create or update, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of data items to create or update, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The set of data items to create or update, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of data items to create or update, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyTextJson

The set of data items to create or update, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of data items to create or update, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | any string name can be used but the value must be the correct type | [optional] 

# SchemaForRequestBodyApplicationJson

The set of data items to create or update, keyed by a unique, ephemeral correlation ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of data items to create or update, keyed by a unique, ephemeral correlation ID. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | [**UpsertStructuredResultDataRequest**]({{complexTypePrefix}}UpsertStructuredResultDataRequest.md) | any string name can be used but the value must be the correct type | [optional] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 

# ScopeSchema

The scope in which to create or update data items.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope in which to create or update data items. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_structured_result_data.ApiResponseFor200) | The successfully created or updated data items along with any failures.
400 | [ApiResponseFor400](#upsert_structured_result_data.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#upsert_structured_result_data.ApiResponseForDefault) | Error response

#### upsert_structured_result_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertStructuredDataResponse**](../../models/UpsertStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertStructuredDataResponse**](../../models/UpsertStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertStructuredDataResponse**](../../models/UpsertStructuredDataResponse.md) |  | 


#### upsert_structured_result_data.ApiResponseFor400
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


#### upsert_structured_result_data.ApiResponseForDefault
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

