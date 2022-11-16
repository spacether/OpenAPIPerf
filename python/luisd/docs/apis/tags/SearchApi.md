<a name="__pageTop"></a>
# luisd.apis.tags.search_api.SearchApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_search**](#instruments_search) | **post** /api/search/instruments | [EXPERIMENTAL] InstrumentsSearch: Instruments search
[**search_portfolio_groups**](#search_portfolio_groups) | **get** /api/search/portfoliogroups | [EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups
[**search_portfolios**](#search_portfolios) | **get** /api/search/portfolios | [EARLY ACCESS] SearchPortfolios: Search Portfolios
[**search_properties**](#search_properties) | **get** /api/search/propertydefinitions | [EARLY ACCESS] SearchProperties: Search Property Definitions

# **instruments_search**
<a name="instruments_search"></a>
> [InstrumentMatch] instruments_search(instrument_search_property)

[EXPERIMENTAL] InstrumentsSearch: Instruments search

Search across all instruments that have been mastered in LUSID. Optionally augment the results with instruments from an external symbology service,  currently OpenFIGI.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import search_api
from luisd.model.instrument_search_property import InstrumentSearchProperty
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.instrument_match import InstrumentMatch
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [{"key":"Instrument/default/Isin","value":"US0378331005"}]
    try:
        # [EXPERIMENTAL] InstrumentsSearch: Instruments search
        api_response = api_instance.instruments_search(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling SearchApi->instruments_search: %s\n" % e)

    # example passing only optional values
    query_params = {
        'masteredEffectiveAt': "masteredEffectiveAt_example",
        'masteredOnly': False,
        'scope': "z",
    }
    body = [{"key":"Instrument/default/Isin","value":"US0378331005"}]
    try:
        # [EXPERIMENTAL] InstrumentsSearch: Instruments search
        api_response = api_instance.instruments_search(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling SearchApi->instruments_search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

A collection of instrument properties to search for. LUSID will return instruments for any matched              properties.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) |  | 

# SchemaForRequestBodyApplicationJson

A collection of instrument properties to search for. LUSID will return instruments for any matched              properties.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) |  | 

# SchemaForRequestBodyTextJson

A collection of instrument properties to search for. LUSID will return instruments for any matched              properties.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) |  | 

# SchemaForRequestBodyApplicationJson

A collection of instrument properties to search for. LUSID will return instruments for any matched              properties.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) | [**InstrumentSearchProperty**]({{complexTypePrefix}}InstrumentSearchProperty.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
masteredEffectiveAt | MasteredEffectiveAtSchema | | optional
masteredOnly | MasteredOnlySchema | | optional
scope | ScopeSchema | | optional


# MasteredEffectiveAtSchema

The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified. | 

# MasteredOnlySchema

If set to true, only search over instruments that have been mastered within LUSID. Defaults to false.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | If set to true, only search over instruments that have been mastered within LUSID. Defaults to false. | if omitted the server will use the default value of False

# ScopeSchema

The scope in which the instrument lies.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope in which the instrument lies. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#instruments_search.ApiResponseFor200) | The instruments found by the search
400 | [ApiResponseFor400](#instruments_search.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#instruments_search.ApiResponseForDefault) | Error response

#### instruments_search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) | [**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) | [**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) | [**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) | [**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) | [**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) | [**InstrumentMatch**]({{complexTypePrefix}}InstrumentMatch.md) |  | 

#### instruments_search.ApiResponseFor400
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


#### instruments_search.ApiResponseForDefault
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

# **search_portfolio_groups**
<a name="search_portfolio_groups"></a>
> PagedResourceListOfPortfolioGroupSearchResult search_portfolio_groups()

[EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups

Search through all portfolio groups

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import search_api
from luisd.model.paged_resource_list_of_portfolio_group_search_result import PagedResourceListOfPortfolioGroupSearchResult
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'search': "search_example",
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'sortBy': "Aa6w77ikCX*cKCmv|`K/V",
        'limit': 1,
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
    }
    try:
        # [EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups
        api_response = api_instance.search_portfolio_groups(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling SearchApi->search_portfolio_groups: %s\n" % e)
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
search | SearchSchema | | optional
filter | FilterSchema | | optional
sortBy | SortBySchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional


# SearchSchema

A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. &#x27;Port*&#x27;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# FilterSchema

Expression to filter the result set.   For example, to filter on the Scope, use \"id.scope eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the result set.   For example, to filter on the Scope, use \&quot;id.scope eq &#x27;string&#x27;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# SortBySchema

Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Order the results by these fields. Use use the &#x27;-&#x27; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | 

# LimitSchema

When paginating, only return this number of records

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | When paginating, only return this number of records | value must be a 32 bit integer

# PageSchema

Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_portfolio_groups.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#search_portfolio_groups.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#search_portfolio_groups.ApiResponseForDefault) | Error response

#### search_portfolio_groups.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPortfolioGroupSearchResult**](../../models/PagedResourceListOfPortfolioGroupSearchResult.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPortfolioGroupSearchResult**](../../models/PagedResourceListOfPortfolioGroupSearchResult.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPortfolioGroupSearchResult**](../../models/PagedResourceListOfPortfolioGroupSearchResult.md) |  | 


#### search_portfolio_groups.ApiResponseFor400
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


#### search_portfolio_groups.ApiResponseForDefault
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

# **search_portfolios**
<a name="search_portfolios"></a>
> PagedResourceListOfPortfolioSearchResult search_portfolios()

[EARLY ACCESS] SearchPortfolios: Search Portfolios

Search through all portfolios

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import search_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.paged_resource_list_of_portfolio_search_result import PagedResourceListOfPortfolioSearchResult
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'search': "search_example",
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'sortBy': "Aa6w77ikCX*cKCmv|`K/V",
        'limit': 1,
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
    }
    try:
        # [EARLY ACCESS] SearchPortfolios: Search Portfolios
        api_response = api_instance.search_portfolios(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling SearchApi->search_portfolios: %s\n" % e)
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
search | SearchSchema | | optional
filter | FilterSchema | | optional
sortBy | SortBySchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional


# SearchSchema

A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. &#x27;Port*&#x27;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# FilterSchema

Expression to filter the result set.   For example, to filter on the portfolio Type, use \"type eq 'Transaction'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the result set.   For example, to filter on the portfolio Type, use \&quot;type eq &#x27;Transaction&#x27;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# SortBySchema

Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Order the results by these fields. Use use the &#x27;-&#x27; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | 

# LimitSchema

When paginating, only return this number of records

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | When paginating, only return this number of records | value must be a 32 bit integer

# PageSchema

Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_portfolios.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#search_portfolios.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#search_portfolios.ApiResponseForDefault) | Error response

#### search_portfolios.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPortfolioSearchResult**](../../models/PagedResourceListOfPortfolioSearchResult.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPortfolioSearchResult**](../../models/PagedResourceListOfPortfolioSearchResult.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPortfolioSearchResult**](../../models/PagedResourceListOfPortfolioSearchResult.md) |  | 


#### search_portfolios.ApiResponseFor400
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


#### search_portfolios.ApiResponseForDefault
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

# **search_properties**
<a name="search_properties"></a>
> PagedResourceListOfPropertyDefinitionSearchResult search_properties()

[EARLY ACCESS] SearchProperties: Search Property Definitions

Search through all Property Definitions

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import search_api
from luisd.model.paged_resource_list_of_property_definition_search_result import PagedResourceListOfPropertyDefinitionSearchResult
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'search': "search_example",
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
        'sortBy': "Aa6w77ikCX*cKCmv|`K/V",
        'limit': 1,
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
    }
    try:
        # [EARLY ACCESS] SearchProperties: Search Property Definitions
        api_response = api_instance.search_properties(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling SearchApi->search_properties: %s\n" % e)
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
search | SearchSchema | | optional
filter | FilterSchema | | optional
sortBy | SortBySchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional


# SearchSchema

A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. &#x27;Port*&#x27;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# FilterSchema

Expression to filter the result set.   For example, to filter on the Value Type, use \"valueType eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the result set.   For example, to filter on the Value Type, use \&quot;valueType eq &#x27;string&#x27;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

# SortBySchema

Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Order the results by these fields. Use use the &#x27;-&#x27; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | 

# LimitSchema

When paginating, only return this number of records

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | When paginating, only return this number of records | value must be a 32 bit integer

# PageSchema

Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_properties.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#search_properties.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#search_properties.ApiResponseForDefault) | Error response

#### search_properties.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPropertyDefinitionSearchResult**](../../models/PagedResourceListOfPropertyDefinitionSearchResult.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPropertyDefinitionSearchResult**](../../models/PagedResourceListOfPropertyDefinitionSearchResult.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPropertyDefinitionSearchResult**](../../models/PagedResourceListOfPropertyDefinitionSearchResult.md) |  | 


#### search_properties.ApiResponseFor400
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


#### search_properties.ApiResponseForDefault
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

