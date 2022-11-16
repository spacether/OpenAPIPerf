<a name="__pageTop"></a>
# luisd.apis.tags.property_definitions_api.PropertyDefinitionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_property_definition**](#create_derived_property_definition) | **post** /api/propertydefinitions/derived | [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
[**create_property_definition**](#create_property_definition) | **post** /api/propertydefinitions | CreatePropertyDefinition: Create property definition
[**delete_property_definition**](#delete_property_definition) | **delete** /api/propertydefinitions/{domain}/{scope}/{code} | DeletePropertyDefinition: Delete property definition
[**get_multiple_property_definitions**](#get_multiple_property_definitions) | **get** /api/propertydefinitions | GetMultiplePropertyDefinitions: Get multiple property definitions
[**get_property_definition**](#get_property_definition) | **get** /api/propertydefinitions/{domain}/{scope}/{code} | GetPropertyDefinition: Get property definition
[**update_property_definition**](#update_property_definition) | **put** /api/propertydefinitions/{domain}/{scope}/{code} | UpdatePropertyDefinition: Update property definition

# **create_derived_property_definition**
<a name="create_derived_property_definition"></a>
> PropertyDefinition create_derived_property_definition(create_derived_property_definition_request)

[EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition

Define a new derived property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import property_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.property_definition import PropertyDefinition
from luisd.model.create_derived_property_definition_request import CreateDerivedPropertyDefinitionRequest
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
    api_instance = property_definitions_api.PropertyDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateDerivedPropertyDefinitionRequest(
        domain="NotDefined",
        scope="scope_example",
        code="code_example",
        display_name="display_name_example",
        data_type_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        property_description="property_description_example",
        derivation_formula="derivation_formula_example",
    )
    try:
        # [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
        api_response = api_instance.create_derived_property_definition(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->create_derived_property_definition: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDerivedPropertyDefinitionRequest**](../../models/CreateDerivedPropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDerivedPropertyDefinitionRequest**](../../models/CreateDerivedPropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDerivedPropertyDefinitionRequest**](../../models/CreateDerivedPropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDerivedPropertyDefinitionRequest**](../../models/CreateDerivedPropertyDefinitionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_derived_property_definition.ApiResponseFor201) | The newly created derived property definition
400 | [ApiResponseFor400](#create_derived_property_definition.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#create_derived_property_definition.ApiResponseForDefault) | Error response

#### create_derived_property_definition.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyTextPlain, SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


#### create_derived_property_definition.ApiResponseFor400
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


#### create_derived_property_definition.ApiResponseForDefault
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

# **create_property_definition**
<a name="create_property_definition"></a>
> PropertyDefinition create_property_definition(create_property_definition_request)

CreatePropertyDefinition: Create property definition

Define a new property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import property_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.create_property_definition_request import CreatePropertyDefinitionRequest
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.property_definition import PropertyDefinition
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
    api_instance = property_definitions_api.PropertyDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreatePropertyDefinitionRequest(
        domain="NotDefined",
        scope="scope_example",
        code="code_example",
        value_required=True,
        display_name="display_name_example",
        data_type_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        life_time="Perpetual",
        constraint_style="constraint_style_example",
        property_description="property_description_example",
    )
    try:
        # CreatePropertyDefinition: Create property definition
        api_response = api_instance.create_property_definition(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->create_property_definition: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePropertyDefinitionRequest**](../../models/CreatePropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePropertyDefinitionRequest**](../../models/CreatePropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePropertyDefinitionRequest**](../../models/CreatePropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePropertyDefinitionRequest**](../../models/CreatePropertyDefinitionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_property_definition.ApiResponseFor201) | The newly created property definition
400 | [ApiResponseFor400](#create_property_definition.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#create_property_definition.ApiResponseForDefault) | Error response

#### create_property_definition.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyTextPlain, SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


#### create_property_definition.ApiResponseFor400
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


#### create_property_definition.ApiResponseForDefault
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

# **delete_property_definition**
<a name="delete_property_definition"></a>
> DeletedEntityResponse delete_property_definition(domainscopecode)

DeletePropertyDefinition: Delete property definition

Delete the definition of the specified property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import property_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.deleted_entity_response import DeletedEntityResponse
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
    api_instance = property_definitions_api.PropertyDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'domain': "NotDefined",
        'scope': "z",
        'code': "z",
    }
    try:
        # DeletePropertyDefinition: Delete property definition
        api_response = api_instance.delete_property_definition(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->delete_property_definition: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
domain | DomainSchema | | 
scope | ScopeSchema | | 
code | CodeSchema | | 

# DomainSchema

The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | must be one of ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "CustomEntity", ] 

# ScopeSchema

The scope of the property to be deleted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the property to be deleted. | 

# CodeSchema

The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_property_definition.ApiResponseFor200) | The time that the property definition was deleted
400 | [ApiResponseFor400](#delete_property_definition.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#delete_property_definition.ApiResponseForDefault) | Error response

#### delete_property_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](../../models/DeletedEntityResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](../../models/DeletedEntityResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](../../models/DeletedEntityResponse.md) |  | 


#### delete_property_definition.ApiResponseFor400
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


#### delete_property_definition.ApiResponseForDefault
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

# **get_multiple_property_definitions**
<a name="get_multiple_property_definitions"></a>
> ResourceListOfPropertyDefinition get_multiple_property_definitions(property_keys)

GetMultiplePropertyDefinitions: Get multiple property definitions

Retrieve the definition of one or more specified properties.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import property_definitions_api
from luisd.model.resource_list_of_property_definition import ResourceListOfPropertyDefinition
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
    api_instance = property_definitions_api.PropertyDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'propertyKeys': [
        "propertyKeys_example"
    ],
    }
    try:
        # GetMultiplePropertyDefinitions: Get multiple property definitions
        api_response = api_instance.get_multiple_property_definitions(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_multiple_property_definitions: %s\n" % e)

    # example passing only optional values
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'propertyKeys': [
        "propertyKeys_example"
    ],
    }
    try:
        # GetMultiplePropertyDefinitions: Get multiple property definitions
        api_response = api_instance.get_multiple_property_definitions(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_multiple_property_definitions: %s\n" % e)
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
filter | FilterSchema | | optional
propertyKeys | PropertyKeysSchema | | 


# AsAtSchema

The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified. | value must conform to RFC-3339 date-time

# FilterSchema

Expression to filter the result set.               For example, to filter on the Lifetime, use \"lifeTime eq 'Perpetual'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the result set.               For example, to filter on the Lifetime, use \&quot;lifeTime eq &#x27;Perpetual&#x27;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# PropertyKeysSchema

One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. &#x27;Portfolio/Manager/Id&#x27;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_multiple_property_definitions.ApiResponseFor200) | The requested property definitions
400 | [ApiResponseFor400](#get_multiple_property_definitions.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_multiple_property_definitions.ApiResponseForDefault) | Error response

#### get_multiple_property_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPropertyDefinition**](../../models/ResourceListOfPropertyDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPropertyDefinition**](../../models/ResourceListOfPropertyDefinition.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPropertyDefinition**](../../models/ResourceListOfPropertyDefinition.md) |  | 


#### get_multiple_property_definitions.ApiResponseFor400
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


#### get_multiple_property_definitions.ApiResponseForDefault
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

# **get_property_definition**
<a name="get_property_definition"></a>
> PropertyDefinition get_property_definition(domainscopecode)

GetPropertyDefinition: Get property definition

Retrieve the definition of a specified property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import property_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.property_definition import PropertyDefinition
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
    api_instance = property_definitions_api.PropertyDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'domain': "NotDefined",
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # GetPropertyDefinition: Get property definition
        api_response = api_instance.get_property_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_property_definition: %s\n" % e)

    # example passing only optional values
    path_params = {
        'domain': "NotDefined",
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # GetPropertyDefinition: Get property definition
        api_response = api_instance.get_property_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_property_definition: %s\n" % e)
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

The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
domain | DomainSchema | | 
scope | ScopeSchema | | 
code | CodeSchema | | 

# DomainSchema

The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | must be one of ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "CustomEntity", ] 

# ScopeSchema

The scope of the specified property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the specified property. | 

# CodeSchema

The code of the specified property. Together with the domain and scope this uniquely              identifies the property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the specified property. Together with the domain and scope this uniquely              identifies the property. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_property_definition.ApiResponseFor200) | The requested property definition
400 | [ApiResponseFor400](#get_property_definition.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_property_definition.ApiResponseForDefault) | Error response

#### get_property_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


#### get_property_definition.ApiResponseFor400
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


#### get_property_definition.ApiResponseForDefault
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

# **update_property_definition**
<a name="update_property_definition"></a>
> PropertyDefinition update_property_definition(domainscopecodeupdate_property_definition_request)

UpdatePropertyDefinition: Update property definition

Update the definition of a specified existing property. Not all elements within a property definition  are modifiable due to the potential implications for values already stored against the property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import property_definitions_api
from luisd.model.update_property_definition_request import UpdatePropertyDefinitionRequest
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.property_definition import PropertyDefinition
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
    api_instance = property_definitions_api.PropertyDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'domain': "NotDefined",
        'scope': "z",
        'code': "z",
    }
    body = UpdatePropertyDefinitionRequest(
        display_name="display_name_example",
        property_description="property_description_example",
    )
    try:
        # UpdatePropertyDefinition: Update property definition
        api_response = api_instance.update_property_definition(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->update_property_definition: %s\n" % e)
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
[**UpdatePropertyDefinitionRequest**](../../models/UpdatePropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdatePropertyDefinitionRequest**](../../models/UpdatePropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdatePropertyDefinitionRequest**](../../models/UpdatePropertyDefinitionRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdatePropertyDefinitionRequest**](../../models/UpdatePropertyDefinitionRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
domain | DomainSchema | | 
scope | ScopeSchema | | 
code | CodeSchema | | 

# DomainSchema

The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | must be one of ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "CustomEntity", ] 

# ScopeSchema

The scope of the property being updated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the property being updated. | 

# CodeSchema

The code of the property being updated. Together with the domain and scope this uniquely              identifies the property.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the property being updated. Together with the domain and scope this uniquely              identifies the property. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_property_definition.ApiResponseFor200) | The updated property definition
400 | [ApiResponseFor400](#update_property_definition.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#update_property_definition.ApiResponseForDefault) | Error response

#### update_property_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyDefinition**](../../models/PropertyDefinition.md) |  | 


#### update_property_definition.ApiResponseFor400
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


#### update_property_definition.ApiResponseForDefault
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

