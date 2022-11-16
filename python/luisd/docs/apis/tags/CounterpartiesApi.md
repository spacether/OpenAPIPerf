<a name="__pageTop"></a>
# luisd.apis.tags.counterparties_api.CounterpartiesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_counterparty_agreement**](#delete_counterparty_agreement) | **delete** /api/counterparties/counterpartyagreements/{scope}/{code} | [EXPERIMENTAL] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
[**delete_credit_support_annex**](#delete_credit_support_annex) | **delete** /api/counterparties/creditsupportannexes/{scope}/{code} | [EXPERIMENTAL] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
[**get_counterparty_agreement**](#get_counterparty_agreement) | **get** /api/counterparties/counterpartyagreements/{scope}/{code} | [EXPERIMENTAL] GetCounterpartyAgreement: Get Counterparty Agreement
[**get_credit_support_annex**](#get_credit_support_annex) | **get** /api/counterparties/creditsupportannexes/{scope}/{code} | [EXPERIMENTAL] GetCreditSupportAnnex: Get Credit Support Annex
[**list_counterparty_agreements**](#list_counterparty_agreements) | **get** /api/counterparties/counterpartyagreements | [EXPERIMENTAL] ListCounterpartyAgreements: List the set of Counterparty Agreements
[**list_credit_support_annexes**](#list_credit_support_annexes) | **get** /api/counterparties/creditsupportannexes | [EXPERIMENTAL] ListCreditSupportAnnexes: List the set of Credit Support Annexes
[**upsert_counterparty_agreement**](#upsert_counterparty_agreement) | **post** /api/counterparties/counterpartyagreements | [EXPERIMENTAL] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
[**upsert_credit_support_annex**](#upsert_credit_support_annex) | **post** /api/counterparties/creditsupportannexes | [EXPERIMENTAL] UpsertCreditSupportAnnex: Upsert Credit Support Annex

# **delete_counterparty_agreement**
<a name="delete_counterparty_agreement"></a>
> AnnulSingleStructuredDataResponse delete_counterparty_agreement(scopecode)

[EXPERIMENTAL] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code

Delete the specified Counterparty Agreement from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    try:
        # [EXPERIMENTAL] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
        api_response = api_instance.delete_counterparty_agreement(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->delete_counterparty_agreement: %s\n" % e)
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

The scope of the Counterparty Agreement to delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope of the Counterparty Agreement to delete. | 

# CodeSchema

The Counterparty Agreement to delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The Counterparty Agreement to delete. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_counterparty_agreement.ApiResponseFor200) | The AsAt of deletion or failure
400 | [ApiResponseFor400](#delete_counterparty_agreement.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#delete_counterparty_agreement.ApiResponseForDefault) | Error response

#### delete_counterparty_agreement.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](../../models/AnnulSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](../../models/AnnulSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](../../models/AnnulSingleStructuredDataResponse.md) |  | 


#### delete_counterparty_agreement.ApiResponseFor400
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


#### delete_counterparty_agreement.ApiResponseForDefault
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

# **delete_credit_support_annex**
<a name="delete_credit_support_annex"></a>
> AnnulSingleStructuredDataResponse delete_credit_support_annex(scopecode)

[EXPERIMENTAL] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code

Delete the specified Credit Support Annex from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    try:
        # [EXPERIMENTAL] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
        api_response = api_instance.delete_credit_support_annex(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->delete_credit_support_annex: %s\n" % e)
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

The scope of the Credit Support Annex to delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope of the Credit Support Annex to delete. | 

# CodeSchema

The Credit Support Annex to delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The Credit Support Annex to delete. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_credit_support_annex.ApiResponseFor200) | The AsAt of deletion or failure
400 | [ApiResponseFor400](#delete_credit_support_annex.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#delete_credit_support_annex.ApiResponseForDefault) | Error response

#### delete_credit_support_annex.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](../../models/AnnulSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](../../models/AnnulSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](../../models/AnnulSingleStructuredDataResponse.md) |  | 


#### delete_credit_support_annex.ApiResponseFor400
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


#### delete_credit_support_annex.ApiResponseForDefault
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

# **get_counterparty_agreement**
<a name="get_counterparty_agreement"></a>
> GetCounterpartyAgreementResponse get_counterparty_agreement(scopecode)

[EXPERIMENTAL] GetCounterpartyAgreement: Get Counterparty Agreement

Get a Counterparty Agreement from a single scope.  The response will return either the Counterparty Agreement that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.get_counterparty_agreement_response import GetCounterpartyAgreementResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetCounterpartyAgreement: Get Counterparty Agreement
        api_response = api_instance.get_counterparty_agreement(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->get_counterparty_agreement: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EXPERIMENTAL] GetCounterpartyAgreement: Get Counterparty Agreement
        api_response = api_instance.get_counterparty_agreement(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->get_counterparty_agreement: %s\n" % e)
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

The asAt datetime at which to retrieve the Counterparty Agreement. Defaults to return the latest version if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the Counterparty Agreement. Defaults to return the latest version if not specified. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the Counterparty Agreement to retrieve.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope of the Counterparty Agreement to retrieve. | 

# CodeSchema

The name of the Counterparty Agreement to retrieve the data for.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The name of the Counterparty Agreement to retrieve the data for. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_counterparty_agreement.ApiResponseFor200) | The successfully retrieved Counterparty Agreement or any failure
400 | [ApiResponseFor400](#get_counterparty_agreement.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_counterparty_agreement.ApiResponseForDefault) | Error response

#### get_counterparty_agreement.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCounterpartyAgreementResponse**](../../models/GetCounterpartyAgreementResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCounterpartyAgreementResponse**](../../models/GetCounterpartyAgreementResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCounterpartyAgreementResponse**](../../models/GetCounterpartyAgreementResponse.md) |  | 


#### get_counterparty_agreement.ApiResponseFor400
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


#### get_counterparty_agreement.ApiResponseForDefault
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

# **get_credit_support_annex**
<a name="get_credit_support_annex"></a>
> GetCreditSupportAnnexResponse get_credit_support_annex(scopecode)

[EXPERIMENTAL] GetCreditSupportAnnex: Get Credit Support Annex

Get a Credit Support Annex from a single scope.  The response will return either the Credit Support Annex that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.get_credit_support_annex_response import GetCreditSupportAnnexResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetCreditSupportAnnex: Get Credit Support Annex
        api_response = api_instance.get_credit_support_annex(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->get_credit_support_annex: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EXPERIMENTAL] GetCreditSupportAnnex: Get Credit Support Annex
        api_response = api_instance.get_credit_support_annex(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->get_credit_support_annex: %s\n" % e)
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

The asAt datetime at which to retrieve the Credit Support Annex . Defaults to return the latest version if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to retrieve the Credit Support Annex . Defaults to return the latest version if not specified. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the Credit Support Annex to retrieve.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The scope of the Credit Support Annex to retrieve. | 

# CodeSchema

The name of the Credit Support Annex to retrieve the data for.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The name of the Credit Support Annex to retrieve the data for. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_credit_support_annex.ApiResponseFor200) | The successfully retrieved credit support annexes or any failure
400 | [ApiResponseFor400](#get_credit_support_annex.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_credit_support_annex.ApiResponseForDefault) | Error response

#### get_credit_support_annex.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCreditSupportAnnexResponse**](../../models/GetCreditSupportAnnexResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCreditSupportAnnexResponse**](../../models/GetCreditSupportAnnexResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCreditSupportAnnexResponse**](../../models/GetCreditSupportAnnexResponse.md) |  | 


#### get_credit_support_annex.ApiResponseFor400
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


#### get_credit_support_annex.ApiResponseForDefault
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

# **list_counterparty_agreements**
<a name="list_counterparty_agreements"></a>
> ResourceListOfGetCounterpartyAgreementResponse list_counterparty_agreements()

[EXPERIMENTAL] ListCounterpartyAgreements: List the set of Counterparty Agreements

List the set of Counterparty Agreements at the specified AsAt date/time

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.resource_list_of_get_counterparty_agreement_response import ResourceListOfGetCounterpartyAgreementResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EXPERIMENTAL] ListCounterpartyAgreements: List the set of Counterparty Agreements
        api_response = api_instance.list_counterparty_agreements(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->list_counterparty_agreements: %s\n" % e)
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


# AsAtSchema

The asAt datetime at which to list the Counterparty Agreements. Defaults to latest if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to list the Counterparty Agreements. Defaults to latest if not specified. | value must conform to RFC-3339 date-time

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_counterparty_agreements.ApiResponseFor200) | The requested Counterparty Agreements
400 | [ApiResponseFor400](#list_counterparty_agreements.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#list_counterparty_agreements.ApiResponseForDefault) | Error response

#### list_counterparty_agreements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetCounterpartyAgreementResponse**](../../models/ResourceListOfGetCounterpartyAgreementResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetCounterpartyAgreementResponse**](../../models/ResourceListOfGetCounterpartyAgreementResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetCounterpartyAgreementResponse**](../../models/ResourceListOfGetCounterpartyAgreementResponse.md) |  | 


#### list_counterparty_agreements.ApiResponseFor400
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


#### list_counterparty_agreements.ApiResponseForDefault
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

# **list_credit_support_annexes**
<a name="list_credit_support_annexes"></a>
> ResourceListOfGetCreditSupportAnnexResponse list_credit_support_annexes()

[EXPERIMENTAL] ListCreditSupportAnnexes: List the set of Credit Support Annexes

List the set of Credit Support Annexes at the specified AsAt date/time

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.resource_list_of_get_credit_support_annex_response import ResourceListOfGetCreditSupportAnnexResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': "1970-01-01T00:00:00.00Z",
    }
    try:
        # [EXPERIMENTAL] ListCreditSupportAnnexes: List the set of Credit Support Annexes
        api_response = api_instance.list_credit_support_annexes(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->list_credit_support_annexes: %s\n" % e)
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


# AsAtSchema

The asAt datetime at which to list the Credit Support Annexes. Defaults to latest if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str, datetime,  | NoneClass, str,  | The asAt datetime at which to list the Credit Support Annexes. Defaults to latest if not specified. | value must conform to RFC-3339 date-time

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_credit_support_annexes.ApiResponseFor200) | The requested Credit Support Annexes
400 | [ApiResponseFor400](#list_credit_support_annexes.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#list_credit_support_annexes.ApiResponseForDefault) | Error response

#### list_credit_support_annexes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetCreditSupportAnnexResponse**](../../models/ResourceListOfGetCreditSupportAnnexResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetCreditSupportAnnexResponse**](../../models/ResourceListOfGetCreditSupportAnnexResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetCreditSupportAnnexResponse**](../../models/ResourceListOfGetCreditSupportAnnexResponse.md) |  | 


#### list_credit_support_annexes.ApiResponseFor400
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


#### list_credit_support_annexes.ApiResponseForDefault
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

# **upsert_counterparty_agreement**
<a name="upsert_counterparty_agreement"></a>
> UpsertSingleStructuredDataResponse upsert_counterparty_agreement(upsert_counterparty_agreement_request)

[EXPERIMENTAL] UpsertCounterpartyAgreement: Upsert Counterparty Agreement

Update or insert Counterparty Agreement in a single scope. An item will be updated if it already exists and inserted if it does not.                The response will return the successfully updated or inserted Counterparty Agreement or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_counterparty_agreement_request import UpsertCounterpartyAgreementRequest
from luisd.model.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only required values which don't have defaults set
    body = UpsertCounterpartyAgreementRequest(
        counterparty_agreement=CounterpartyAgreement(
            display_name="display_name_example",
            agreement_type="agreement_type_example",
            counterparty_signatory=CounterpartySignatory(
                name="name_example",
                legal_entity_identifier=TypedResourceId(
                    id_type_scope="z",
                    id_type_code="z",
                    code="z",
                ),
            ),
            dated_as_of="1970-01-01T00:00:00.00Z",
            credit_support_annex_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
,
        ),
    )
    try:
        # [EXPERIMENTAL] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
        api_response = api_instance.upsert_counterparty_agreement(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->upsert_counterparty_agreement: %s\n" % e)
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
[**UpsertCounterpartyAgreementRequest**](../../models/UpsertCounterpartyAgreementRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertCounterpartyAgreementRequest**](../../models/UpsertCounterpartyAgreementRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertCounterpartyAgreementRequest**](../../models/UpsertCounterpartyAgreementRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertCounterpartyAgreementRequest**](../../models/UpsertCounterpartyAgreementRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_counterparty_agreement.ApiResponseFor200) | The successfully updated or inserted Counterparty Agreement or any failure
400 | [ApiResponseFor400](#upsert_counterparty_agreement.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#upsert_counterparty_agreement.ApiResponseForDefault) | Error response

#### upsert_counterparty_agreement.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](../../models/UpsertSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](../../models/UpsertSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](../../models/UpsertSingleStructuredDataResponse.md) |  | 


#### upsert_counterparty_agreement.ApiResponseFor400
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


#### upsert_counterparty_agreement.ApiResponseForDefault
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

# **upsert_credit_support_annex**
<a name="upsert_credit_support_annex"></a>
> UpsertSingleStructuredDataResponse upsert_credit_support_annex(upsert_credit_support_annex_request)

[EXPERIMENTAL] UpsertCreditSupportAnnex: Upsert Credit Support Annex

Update or insert Credit Support Annex in a single scope. An item will be updated if it already exists and inserted if it does not.                The response will return the successfully updated or inserted Credit Support Annex or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import counterparties_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
from luisd.model.upsert_credit_support_annex_request import UpsertCreditSupportAnnexRequest
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
    api_instance = counterparties_api.CounterpartiesApi(api_client)

    # example passing only required values which don't have defaults set
    body = UpsertCreditSupportAnnexRequest(
        credit_support_annex=CreditSupportAnnex(
            reference_currency="reference_currency_example",
            collateral_currencies=[
                "collateral_currencies_example"
            ],
            isda_agreement_version="isda_agreement_version_example",
            margin_call_frequency="margin_call_frequency_example",
            valuation_agent="valuation_agent_example",
            threshold_amount=3.14,
            rounding_decimal_places=1,
            initial_margin_amount=3.14,
            minimum_transfer_amount=3.14,
            id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
        ),
    )
    try:
        # [EXPERIMENTAL] UpsertCreditSupportAnnex: Upsert Credit Support Annex
        api_response = api_instance.upsert_credit_support_annex(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling CounterpartiesApi->upsert_credit_support_annex: %s\n" % e)
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
[**UpsertCreditSupportAnnexRequest**](../../models/UpsertCreditSupportAnnexRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertCreditSupportAnnexRequest**](../../models/UpsertCreditSupportAnnexRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertCreditSupportAnnexRequest**](../../models/UpsertCreditSupportAnnexRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertCreditSupportAnnexRequest**](../../models/UpsertCreditSupportAnnexRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upsert_credit_support_annex.ApiResponseFor200) | The successfully updated or inserted item or any failure
400 | [ApiResponseFor400](#upsert_credit_support_annex.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#upsert_credit_support_annex.ApiResponseForDefault) | Error response

#### upsert_credit_support_annex.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](../../models/UpsertSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](../../models/UpsertSingleStructuredDataResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](../../models/UpsertSingleStructuredDataResponse.md) |  | 


#### upsert_credit_support_annex.ApiResponseFor400
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


#### upsert_credit_support_annex.ApiResponseForDefault
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

