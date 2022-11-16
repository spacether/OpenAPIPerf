<a name="__pageTop"></a>
# luisd.apis.tags.custom_entities_api.CustomEntitiesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_entity**](#get_custom_entity) | **get** /api/customentities/{entityType}/{identifierType}/{identifierValue} | [EXPERIMENTAL] GetCustomEntity: Get CustomEntity
[**get_custom_entity_relationships**](#get_custom_entity_relationships) | **get** /api/customentities/{entityType}/{identifierType}/{identifierValue}/relationships | [EXPERIMENTAL] GetCustomEntityRelationships: Get Relationships for Custom Entity
[**list_custom_entities**](#list_custom_entities) | **get** /api/customentities/{entityType} | [EXPERIMENTAL] ListCustomEntities: List Custom Entities
[**upsert_custom_entity**](#upsert_custom_entity) | **post** /api/customentities/{entityType} | [EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity

# **get_custom_entity**
<a name="get_custom_entity"></a>
> CustomEntityResponse get_custom_entity(entity_typeidentifier_typeidentifier_valueidentifier_scope)

[EXPERIMENTAL] GetCustomEntity: Get CustomEntity

Retrieve a CustomEntity by a specific Id at a point in AsAt time.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import custom_entities_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.custom_entity_response import CustomEntityResponse
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
    api_instance = custom_entities_api.CustomEntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityType': "entityType_example",
        'identifierType': "z",
        'identifierValue': "z",
    }
    query_params = {
        'identifierScope': "z",
    }
    try:
        # [EXPERIMENTAL] GetCustomEntity: Get CustomEntity
        api_response = api_instance.get_custom_entity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityType': "entityType_example",
        'identifierType': "z",
        'identifierValue': "z",
    }
    query_params = {
        'identifierScope': "z",
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EXPERIMENTAL] GetCustomEntity: Get CustomEntity
        api_response = api_instance.get_custom_entity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity: %s\n" % e)
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
identifierScope | IdentifierScopeSchema | | 
asAt | AsAtSchema | | optional


# IdentifierScopeSchema

The identifier scope.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The identifier scope. | 

# AsAtSchema

The AsAt at which to retrieve the CustomEntity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The AsAt at which to retrieve the CustomEntity. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityType | EntityTypeSchema | | 
identifierType | IdentifierTypeSchema | | 
identifierValue | IdentifierValueSchema | | 

# EntityTypeSchema

The type of entity to retrieve. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The type of entity to retrieve. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest). | 

# IdentifierTypeSchema

An identifier type attached to the CustomEntity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An identifier type attached to the CustomEntity. | 

# IdentifierValueSchema

The identifier value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The identifier value. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_entity.ApiResponseFor200) | The requested Custom Entity
400 | [ApiResponseFor400](#get_custom_entity.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_custom_entity.ApiResponseForDefault) | Error response

#### get_custom_entity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityResponse**](../../models/CustomEntityResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityResponse**](../../models/CustomEntityResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityResponse**](../../models/CustomEntityResponse.md) |  | 


#### get_custom_entity.ApiResponseFor400
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


#### get_custom_entity.ApiResponseForDefault
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

# **get_custom_entity_relationships**
<a name="get_custom_entity_relationships"></a>
> ResourceListOfRelationship get_custom_entity_relationships(entity_typeidentifier_scopeidentifier_typeidentifier_value)

[EXPERIMENTAL] GetCustomEntityRelationships: Get Relationships for Custom Entity

Get relationships for the specified Custom Entity.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import custom_entities_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_relationship import ResourceListOfRelationship
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
    api_instance = custom_entities_api.CustomEntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityType': "entityType_example",
        'identifierType': "z",
        'identifierValue': "z",
    }
    query_params = {
        'identifierScope': "z",
    }
    try:
        # [EXPERIMENTAL] GetCustomEntityRelationships: Get Relationships for Custom Entity
        api_response = api_instance.get_custom_entity_relationships(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity_relationships: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityType': "entityType_example",
        'identifierType': "z",
        'identifierValue': "z",
    }
    query_params = {
        'identifierScope': "z",
        'effectiveAt': "A",
        'asAt': "1970-01-01T00:00:00.00Z",
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'identifierTypes': [
        "identifierTypes_example"
    ],
    }
    try:
        # [EXPERIMENTAL] GetCustomEntityRelationships: Get Relationships for Custom Entity
        api_response = api_instance.get_custom_entity_relationships(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity_relationships: %s\n" % e)
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
identifierScope | IdentifierScopeSchema | | 
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
filter | FilterSchema | | optional
identifierTypes | IdentifierTypesSchema | | optional


# IdentifierScopeSchema

The identifier scope.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The identifier scope. | 

# EffectiveAtSchema

The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. | 

# AsAtSchema

The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | value must conform to RFC-3339 date-time

# FilterSchema

Expression to filter relationships. Users should provide null or empty string for this field until further notice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter relationships. Users should provide null or empty string for this field until further notice. | 

# IdentifierTypesSchema

Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityType | EntityTypeSchema | | 
identifierType | IdentifierTypeSchema | | 
identifierValue | IdentifierValueSchema | | 

# EntityTypeSchema

The type of entity get relationships for.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The type of entity get relationships for. | 

# IdentifierTypeSchema

An identifier type attached to the CustomEntity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An identifier type attached to the CustomEntity. | 

# IdentifierValueSchema

The identifier value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The identifier value. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_entity_relationships.ApiResponseFor200) | The relationships for the specified custom entity.
400 | [ApiResponseFor400](#get_custom_entity_relationships.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_custom_entity_relationships.ApiResponseForDefault) | Error response

#### get_custom_entity_relationships.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelationship**](../../models/ResourceListOfRelationship.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelationship**](../../models/ResourceListOfRelationship.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelationship**](../../models/ResourceListOfRelationship.md) |  | 


#### get_custom_entity_relationships.ApiResponseFor400
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


#### get_custom_entity_relationships.ApiResponseForDefault
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

# **list_custom_entities**
<a name="list_custom_entities"></a>
> PagedResourceListOfCustomEntityResponse list_custom_entities(entity_type)

[EXPERIMENTAL] ListCustomEntities: List Custom Entities

List all the Custom Entities matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import custom_entities_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.paged_resource_list_of_custom_entity_response import PagedResourceListOfCustomEntityResponse
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
    api_instance = custom_entities_api.CustomEntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityType': "entityType_example",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] ListCustomEntities: List Custom Entities
        api_response = api_instance.list_custom_entities(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->list_custom_entities: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityType': "entityType_example",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': "1970-01-01T00:00:00.00Z",
        'limit': 1,
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
    }
    try:
        # [EXPERIMENTAL] ListCustomEntities: List Custom Entities
        api_response = api_instance.list_custom_entities(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->list_custom_entities: %s\n" % e)
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
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional
page | PageSchema | | optional


# EffectiveAtSchema

The effective datetime or cut label at which to list the entities. Defaults to the current LUSID              system datetime if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The effective datetime or cut label at which to list the entities. Defaults to the current LUSID              system datetime if not specified. | 

# AsAtSchema

The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. | value must conform to RFC-3339 date-time

# LimitSchema

When paginating, limit the results to this number. Defaults to 100 if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | When paginating, limit the results to this number. Defaults to 100 if not specified. | value must be a 32 bit integer

# FilterSchema

Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | 

# PageSchema

The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityType | EntityTypeSchema | | 

# EntityTypeSchema

The type of entity to list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The type of entity to list. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_custom_entities.ApiResponseFor200) | The requested custom entities
400 | [ApiResponseFor400](#list_custom_entities.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#list_custom_entities.ApiResponseForDefault) | Error response

#### list_custom_entities.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfCustomEntityResponse**](../../models/PagedResourceListOfCustomEntityResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfCustomEntityResponse**](../../models/PagedResourceListOfCustomEntityResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfCustomEntityResponse**](../../models/PagedResourceListOfCustomEntityResponse.md) |  | 


#### list_custom_entities.ApiResponseFor400
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


#### list_custom_entities.ApiResponseForDefault
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

# **upsert_custom_entity**
<a name="upsert_custom_entity"></a>
> CustomEntityResponse upsert_custom_entity(entity_typecustom_entity_request)

[EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity

Insert the custom entity if it does not exist or update the custom entity with the supplied state if it does exist.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import custom_entities_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.custom_entity_request import CustomEntityRequest
from luisd.model.custom_entity_response import CustomEntityResponse
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
    api_instance = custom_entities_api.CustomEntitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityType': "entityType_example",
    }
    body = CustomEntityRequest(
        display_name="display_name_example",
        description="description_example",
        effective_at="effective_at_example",
        identifiers=[
            CustomEntityIdRequest(
                identifier_scope="identifier_scope_example",
                identifier_type="identifier_type_example",
                identifier_value="identifier_value_example",
            )
        ],
        fields=[
            CustomEntityField(
                name="name_example",
                value=dict(),
            )
        ],
    )
    try:
        # [EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity
        api_response = api_instance.upsert_custom_entity(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CustomEntitiesApi->upsert_custom_entity: %s\n" % e)
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
[**CustomEntityRequest**](../../models/CustomEntityRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityRequest**](../../models/CustomEntityRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityRequest**](../../models/CustomEntityRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityRequest**](../../models/CustomEntityRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityType | EntityTypeSchema | | 

# EntityTypeSchema

The type of the CustomEntity to be created. An entityType can be created using the M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.GetDefinition(System.String,System.Nullable{System.DateTimeOffset}) endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The type of the CustomEntity to be created. An entityType can be created using the M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.GetDefinition(System.String,System.Nullable{System.DateTimeOffset}) endpoint. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_custom_entity.ApiResponseFor200) | The upserted Custom Entity
400 | [ApiResponseFor400](#upsert_custom_entity.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#upsert_custom_entity.ApiResponseForDefault) | Error response

#### upsert_custom_entity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityResponse**](../../models/CustomEntityResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityResponse**](../../models/CustomEntityResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomEntityResponse**](../../models/CustomEntityResponse.md) |  | 


#### upsert_custom_entity.ApiResponseFor400
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


#### upsert_custom_entity.ApiResponseForDefault
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

