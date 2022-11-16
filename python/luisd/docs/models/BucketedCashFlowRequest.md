# luisd.model.bucketed_cash_flow_request.BucketedCashFlowRequest

Specification class consisting of parameters for BucketedCashFlow endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specification class consisting of parameters for BucketedCashFlow endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**roundingMethod** | str,  | str,  | When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod    Supported string (enumeration) values are: [RoundDown, RoundUp]. | 
**[bucketingDates](#bucketingDates)** | list, tuple, None,  | tuple, NoneClass,  | A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty. | [optional] 
**[bucketTenors](#bucketTenors)** | list, tuple, None,  | tuple, NoneClass,  | A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty. | [optional] 
**effectiveAt** | None, str,  | NoneClass, str,  | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | [optional] 
**windowStart** | None, str,  | NoneClass, str,  | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified. | [optional] 
**windowEnd** | None, str,  | NoneClass, str,  | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to &#x27;today&#x27; if it is not specified | [optional] 
**recipeId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**reportCurrency** | None, str,  | NoneClass, str,  | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place. | [optional] 
**asAt** | None, str, datetime,  | NoneClass, str,  | The asAt date to use | [optional] value must conform to RFC-3339 date-time

# bucketingDates

A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# bucketTenors

A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

