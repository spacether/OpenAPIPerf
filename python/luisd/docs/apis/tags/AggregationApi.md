<a name="__pageTop"></a>
# luisd.apis.tags.aggregation_api.AggregationApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_configuration_recipe**](#generate_configuration_recipe) | **post** /api/aggregation/{scope}/{code}/$generateconfigurationrecipe | [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
[**get_queryable_keys**](#get_queryable_keys) | **get** /api/results/queryable/keys | [EXPERIMENTAL] GetQueryableKeys: Query the set of supported \&quot;addresses\&quot; that can be queried from the aggregation endpoint.
[**get_valuation**](#get_valuation) | **post** /api/aggregation/$valuation | [BETA] GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
[**get_valuation_of_weighted_instruments**](#get_valuation_of_weighted_instruments) | **post** /api/aggregation/$valuationinlined | [BETA] GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio

# **generate_configuration_recipe**
<a name="generate_configuration_recipe"></a>
> ConfigurationRecipe generate_configuration_recipe(scopecode)

[EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.

Given a set of scopes, a portfolio Id and a basic recipe, this endpoint generates a configuration recipe with relevant rules that can value the instruments in the portfolio.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import aggregation_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.create_recipe_request import CreateRecipeRequest
from luisd.model.configuration_recipe import ConfigurationRecipe
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
    api_instance = aggregation_api.AggregationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    try:
        # [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
        api_response = api_instance.generate_configuration_recipe(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->generate_configuration_recipe: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    body = CreateRecipeRequest(
        recipe_creation_market_data_scopes=[
            "recipe_creation_market_data_scopes_example"
        ],
        recipe_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        inline_recipe=ConfigurationRecipe(
            scope="z",
            code="z",
            market=MarketContext(
                market_rules=[
                    MarketDataKeyRule(
                        key="key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        quote_type="Price",
                        field="field_example",
                        quote_interval="quote_interval_example",
                        as_at="1970-01-01T00:00:00.00Z",
                        price_source="price_source_example",
                        mask="mask_example",
                    )
                ],
                suppliers=dict(
                    commodity="commodity_example",
                    credit="credit_example",
                    equity="equity_example",
                    fx="fx_example",
                    rates="rates_example",
                ),
                options=MarketOptions(
                    default_supplier="default_supplier_example",
                    default_instrument_code_type="default_instrument_code_type_example",
                    default_scope="z",
                    attempt_to_infer_missing_fx=True,
                    calendar_scope="z",
                    convention_scope="z",
                ),
            ),
            pricing=PricingContext(
                model_rules=[
                    VendorModelRule(
                        supplier="Lusid",
                        model_name="model_name_example",
                        instrument_type="instrument_type_example",
                        parameters="parameters_example",
                        model_options=ModelOptions(),
                        instrument_id="instrument_id_example",
                    )
                ],
                model_choice=dict(
                    "key": ModelSelection(
                        library="Lusid",
                        model="SimpleStatic",
                    ),
                ),
                options=PricingOptions(
                    model_selection=ModelSelection(),
                    use_instrument_type_to_determine_pricer=True,
                    allow_any_instruments_with_sec_uid_to_price_off_lookup=True,
                    allow_partially_successful_evaluation=True,
                    produce_separate_result_for_linear_otc_legs=True,
                    enable_use_of_cached_unit_results=True,
                    window_valuation_on_instrument_start_end=True,
                    remove_contingent_cashflows_in_payment_diary=True,
                    use_child_sub_holding_keys_for_portfolio_expansion=True,
                    validate_domestic_and_quote_currencies_are_consistent=True,
                ),
                result_data_rules=[
                    ResultDataKeyRule(
                        resource_key="resource_key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        document_code="document_code_example",
                        quote_interval="quote_interval_example",
                        as_at="1970-01-01T00:00:00.00Z",
                    )
                ],
            ),
            aggregation=AggregationContext(
                options=AggregationOptions(
                    use_ansi_like_syntax=True,
                    allow_partial_entitlement_success=True,
                ),
            ),
            inherited_recipes=[
                ResourceId()
            ],
            description="Aa6w77ikCX*cKCmv|`K/V",
            holding=HoldingContext(
                tax_lot_level_holdings=True,
            ),
        ),
        as_at="1970-01-01T00:00:00.00Z",
        effective_at="effective_at_example",
    )
    try:
        # [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
        api_response = api_instance.generate_configuration_recipe(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->generate_configuration_recipe: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
[**CreateRecipeRequest**](../../models/CreateRecipeRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateRecipeRequest**](../../models/CreateRecipeRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateRecipeRequest**](../../models/CreateRecipeRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateRecipeRequest**](../../models/CreateRecipeRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

# ScopeSchema

The scope of the portfolio

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The scope of the portfolio | 

# CodeSchema

The code of the portfolio

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The code of the portfolio | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#generate_configuration_recipe.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#generate_configuration_recipe.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#generate_configuration_recipe.ApiResponseForDefault) | Error response

#### generate_configuration_recipe.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationRecipe**](../../models/ConfigurationRecipe.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationRecipe**](../../models/ConfigurationRecipe.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationRecipe**](../../models/ConfigurationRecipe.md) |  | 


#### generate_configuration_recipe.ApiResponseFor400
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


#### generate_configuration_recipe.ApiResponseForDefault
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

# **get_queryable_keys**
<a name="get_queryable_keys"></a>
> ResourceListOfAggregationQuery get_queryable_keys()

[EXPERIMENTAL] GetQueryableKeys: Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.

When a request is made for aggregation, the user needs to know what keys can be passed to it for queryable data. This endpoint allows to queries to provide the set of keys,  what they are and what they return.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import aggregation_api
from luisd.model.resource_list_of_aggregation_query import ResourceListOfAggregationQuery
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
    api_instance = aggregation_api.AggregationApi(api_client)

    # example passing only optional values
    query_params = {
        'page': "zA9LCSLv1C1ylmgd0/Y2TA",
        'limit': 1,
        'filter': "Aa6w77ikCX*cKCmv|`K/V",
    }
    try:
        # [EXPERIMENTAL] GetQueryableKeys: Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.
        api_response = api_instance.get_queryable_keys(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->get_queryable_keys: %s\n" % e)
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
page | PageSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional


# PageSchema

The pagination token to use to continue listing queryable keys from a previous call to list queryable keys.              This value is returned from the previous call.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The pagination token to use to continue listing queryable keys from a previous call to list queryable keys.              This value is returned from the previous call. | 

# LimitSchema

When paginating, limit the number of returned results to this many.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | When paginating, limit the number of returned results to this many. | value must be a 32 bit integer

# FilterSchema

Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_queryable_keys.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#get_queryable_keys.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_queryable_keys.ApiResponseForDefault) | Error response

#### get_queryable_keys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfAggregationQuery**](../../models/ResourceListOfAggregationQuery.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfAggregationQuery**](../../models/ResourceListOfAggregationQuery.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfAggregationQuery**](../../models/ResourceListOfAggregationQuery.md) |  | 


#### get_queryable_keys.ApiResponseFor400
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


#### get_queryable_keys.ApiResponseForDefault
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

# **get_valuation**
<a name="get_valuation"></a>
> ListAggregationResponse get_valuation()

[BETA] GetValuation: Perform valuation for a list of portfolios and/or portfolio groups

Perform valuation on specified list of portfolio and/or portfolio groups for a set of dates.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import aggregation_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.valuation_request import ValuationRequest
from luisd.model.list_aggregation_response import ListAggregationResponse
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
    api_instance = aggregation_api.AggregationApi(api_client)

    # example passing only optional values
    body = ValuationRequest(
        recipe_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        as_at="1970-01-01T00:00:00.00Z",
        metrics=[
            AggregateSpec(
                key="key_example",
                op="Sum",
            )
        ],
        group_by=[
            "group_by_example"
        ],
        filters=[
            PropertyFilter(
                left="left_example",
                operator="Equals",
                right=dict(),
                right_operand_type="Absolute",
            )
        ],
        sort=[
            OrderBySpec(
                key="key_example",
                sort_order="Ascending",
            )
        ],
        report_currency="report_currency_example",
        equip_with_subtotals=True,
        portfolio_entity_ids=[
            PortfolioEntityId(
                scope="z",
                code="z",
                portfolio_entity_type="portfolio_entity_type_example",
            )
        ],
        valuation_schedule=ValuationSchedule(
            effective_from="effective_from_example",
            effective_at="effective_at_example",
            tenor="tenor_example",
            roll_convention="roll_convention_example",
            holiday_calendars=[
                "holiday_calendars_example"
            ],
            valuation_date_times=[
                "valuation_date_times_example"
            ],
        ),
    )
    try:
        # [BETA] GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
        api_response = api_instance.get_valuation(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->get_valuation: %s\n" % e)
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
[**ValuationRequest**](../../models/ValuationRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationRequest**](../../models/ValuationRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationRequest**](../../models/ValuationRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationRequest**](../../models/ValuationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_valuation.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#get_valuation.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_valuation.ApiResponseForDefault) | Error response

#### get_valuation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationResponse**](../../models/ListAggregationResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationResponse**](../../models/ListAggregationResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationResponse**](../../models/ListAggregationResponse.md) |  | 


#### get_valuation.ApiResponseFor400
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


#### get_valuation.ApiResponseForDefault
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

# **get_valuation_of_weighted_instruments**
<a name="get_valuation_of_weighted_instruments"></a>
> ListAggregationResponse get_valuation_of_weighted_instruments()

[BETA] GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio

Perform valuation on the portfolio that is defined by the weighted set of instruments passed to the request.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.apis.tags import aggregation_api
from luisd.model.inline_valuation_request import InlineValuationRequest
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.list_aggregation_response import ListAggregationResponse
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
    api_instance = aggregation_api.AggregationApi(api_client)

    # example passing only optional values
    body = InlineValuationRequest(
        recipe_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        as_at="1970-01-01T00:00:00.00Z",
        metrics=[
            AggregateSpec(
                key="key_example",
                op="Sum",
            )
        ],
        group_by=[
            "group_by_example"
        ],
        filters=[
            PropertyFilter(
                left="left_example",
                operator="Equals",
                right=dict(),
                right_operand_type="Absolute",
            )
        ],
        sort=[
            OrderBySpec(
                key="key_example",
                sort_order="Ascending",
            )
        ],
        report_currency="report_currency_example",
        equip_with_subtotals=True,
        valuation_schedule=ValuationSchedule(
            effective_from="effective_from_example",
            effective_at="effective_at_example",
            tenor="tenor_example",
            roll_convention="roll_convention_example",
            holiday_calendars=[
                "holiday_calendars_example"
            ],
            valuation_date_times=[
                "valuation_date_times_example"
            ],
        ),
        instruments=[
            WeightedInstrument(
                quantity=3.14,
                holding_identifier="holding_identifier_example",
                instrument=LusidInstrument(),
            )
        ],
    )
    try:
        # [BETA] GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio
        api_response = api_instance.get_valuation_of_weighted_instruments(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->get_valuation_of_weighted_instruments: %s\n" % e)
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
[**InlineValuationRequest**](../../models/InlineValuationRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationRequest**](../../models/InlineValuationRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationRequest**](../../models/InlineValuationRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationRequest**](../../models/InlineValuationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_valuation_of_weighted_instruments.ApiResponseFor200) | Success
400 | [ApiResponseFor400](#get_valuation_of_weighted_instruments.ApiResponseFor400) | The details of the input related failure
default | [ApiResponseForDefault](#get_valuation_of_weighted_instruments.ApiResponseForDefault) | Error response

#### get_valuation_of_weighted_instruments.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationResponse**](../../models/ListAggregationResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationResponse**](../../models/ListAggregationResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationResponse**](../../models/ListAggregationResponse.md) |  | 


#### get_valuation_of_weighted_instruments.ApiResponseFor400
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


#### get_valuation_of_weighted_instruments.ApiResponseForDefault
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

