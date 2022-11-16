<a name="__pageTop"></a>
# luisd.apis.tags.packages_api.PackagesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_package**](#delete_package) | **delete** /api/packages/{scope}/{code} | [EXPERIMENTAL] DeletePackage: Delete package
[**get_package**](#get_package) | **get** /api/packages/{scope}/{code} | [EXPERIMENTAL] GetPackage: Get Package
[**list_packages**](#list_packages) | **get** /api/packages | [EXPERIMENTAL] ListPackages: List Packages
[**upsert_packages**](#upsert_packages) | **post** /api/packages | [EXPERIMENTAL] UpsertPackages: Upsert Package

# **delete_package**
<a name="delete_package"></a>
> DeletedEntityResponse delete_package(scopecode)

[EXPERIMENTAL] DeletePackage: Delete package

Delete an package. Deletion will be valid from the package's creation datetime.  This means that the package will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import packages_api
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
    api_instance = packages_api.PackagesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    try:
        # [EXPERIMENTAL] DeletePackage: Delete package
        api_response = api_instance.delete_package(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PackagesApi->delete_package: %s\n" % e)
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
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The package scope.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The package scope. | 

# CodeSchema

The package's code. This, together with the scope uniquely identifies the package to delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The package&#x27;s code. This, together with the scope uniquely identifies the package to delete. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_package.ApiResponseFor200) | The response from deleting an package.
400 | [ApiResponseFor400](#delete_package.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#delete_package.ApiResponseForDefault) | Error response

#### delete_package.ApiResponseFor200
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


#### delete_package.ApiResponseFor400
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


#### delete_package.ApiResponseForDefault
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

# **get_package**
<a name="get_package"></a>
> Package get_package(scopecode)

[EXPERIMENTAL] GetPackage: Get Package

Fetch a Package that matches the specified identifier

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import packages_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.package import Package
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
    api_instance = packages_api.PackagesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetPackage: Get Package
        api_response = api_instance.get_package(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PackagesApi->get_package: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
        'propertyKeys': [
        "propertyKeys_example"
    ],
    }
    try:
        # [EXPERIMENTAL] GetPackage: Get Package
        api_response = api_instance.get_package(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PackagesApi->get_package: %s\n" % e)
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
propertyKeys | PropertyKeysSchema | | optional


# AsAtSchema

The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified. | value must conform to RFC-3339 date-time

# PropertyKeysSchema

A list of property keys from the \"Package\" domain to decorate onto the package.              These take the format {domain}/{scope}/{code} e.g. \"Package/system/Name\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of property keys from the \&quot;Package\&quot; domain to decorate onto the package.              These take the format {domain}/{scope}/{code} e.g. \&quot;Package/system/Name\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope to which the package belongs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope to which the package belongs. | 

# CodeSchema

The package's unique identifier.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The package&#x27;s unique identifier. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_package.ApiResponseFor200) | The package matching the given identifier.
400 | [ApiResponseFor400](#get_package.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_package.ApiResponseForDefault) | Error response

#### get_package.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Package**](../../models/Package.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Package**](../../models/Package.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Package**](../../models/Package.md) |  | 


#### get_package.ApiResponseFor400
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


#### get_package.ApiResponseForDefault
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

# **list_packages**
<a name="list_packages"></a>
> PagedResourceListOfPackage list_packages()

[EXPERIMENTAL] ListPackages: List Packages

Fetch the last pre-AsAt date version of each package in scope (does not fetch the entire history).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import packages_api
from luisd.model.paged_resource_list_of_package import PagedResourceListOfPackage
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
    api_instance = packages_api.PackagesApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
        'sortBy': [
        "sortBy_example"
    ],
        'limit': 1,
        'filter': "",
        'propertyKeys': [
        "propertyKeys_example"
    ],
    }
    try:
        # [EXPERIMENTAL] ListPackages: List Packages
        api_response = api_instance.list_packages(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PackagesApi->list_packages: %s\n" % e)
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
sortBy | SortBySchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional
propertyKeys | PropertyKeysSchema | | optional


# AsAtSchema

The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified. | value must conform to RFC-3339 date-time

# PageSchema

The pagination token to use to continue listing packages from a previous call to list packages.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The pagination token to use to continue listing packages from a previous call to list packages.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | 

# SortBySchema

Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Order the results by these fields. Use use the &#x27;-&#x27; sign to denote descending order e.g. -MyFieldName. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LimitSchema

When paginating, limit the number of returned results to this many.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | When paginating, limit the number of returned results to this many. | value must be a 32 bit integer

# FilterSchema

Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | if omitted the server will use the default value of ""

# PropertyKeysSchema

A list of property keys from the \"Package\" domain to decorate onto each package.                  These take the format {domain}/{scope}/{code} e.g. \"Package/system/Name\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of property keys from the \&quot;Package\&quot; domain to decorate onto each package.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Package/system/Name\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_packages.ApiResponseFor200) | Packages in scope.
400 | [ApiResponseFor400](#list_packages.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#list_packages.ApiResponseForDefault) | Error response

#### list_packages.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPackage**](../../models/PagedResourceListOfPackage.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPackage**](../../models/PagedResourceListOfPackage.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPackage**](../../models/PagedResourceListOfPackage.md) |  | 


#### list_packages.ApiResponseFor400
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


#### list_packages.ApiResponseForDefault
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

# **upsert_packages**
<a name="upsert_packages"></a>
> ResourceListOfPackage upsert_packages()

[EXPERIMENTAL] UpsertPackages: Upsert Package

Upsert; update existing packages with given ids, or create new packages otherwise.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import packages_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.package_set_request import PackageSetRequest
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_package import ResourceListOfPackage
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
    api_instance = packages_api.PackagesApi(api_client)

    # example passing only optional values
    body = PackageSetRequest(
        requests=[
            PackageRequest(
                id=ResourceId(
                    scope="scope_example",
                    code="code_example",
                ),
                order_ids=[
                    ResourceId()
                ],
                order_instruction_ids=[
                    ResourceId()
                ],
                properties=dict(
                    "key": PerpetualProperty(
                        key="key_example",
                        value=PropertyValue(
                            label_value="label_value_example",
                            metric_value=MetricValue(
                                value=3.14,
                                unit="unit_example",
                            ),
                            label_value_set=LabelValueSet(
                                values=[
                                    "values_example"
                                ],
                            ),
                        ),
                    ),
                ),
            )
        ],
    )
    try:
        # [EXPERIMENTAL] UpsertPackages: Upsert Package
        api_response = api_instance.upsert_packages(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PackagesApi->upsert_packages: %s\n" % e)
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
[**PackageSetRequest**](../../models/PackageSetRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PackageSetRequest**](../../models/PackageSetRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PackageSetRequest**](../../models/PackageSetRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PackageSetRequest**](../../models/PackageSetRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#upsert_packages.ApiResponseFor201) | A collection of packages.
400 | [ApiResponseFor400](#upsert_packages.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#upsert_packages.ApiResponseForDefault) | Error response

#### upsert_packages.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyTextPlain, SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPackage**](../../models/ResourceListOfPackage.md) |  | 


# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPackage**](../../models/ResourceListOfPackage.md) |  | 


# SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPackage**](../../models/ResourceListOfPackage.md) |  | 


#### upsert_packages.ApiResponseFor400
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


#### upsert_packages.ApiResponseForDefault
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

