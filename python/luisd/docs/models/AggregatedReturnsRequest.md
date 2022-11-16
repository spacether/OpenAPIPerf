# luisd.model.aggregated_returns_request.AggregatedReturnsRequest

The request used in the AggregatedReturns.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request used in the AggregatedReturns. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metrics](#metrics)** | list, tuple,  | tuple,  | A list of metrics to calculate in the AggregatedReturns. | 
**recipeId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**compositeMethod** | None, str,  | NoneClass, str,  | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**period** | None, str,  | NoneClass, str,  | The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
**outputFrequency** | None, str,  | NoneClass, str,  | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
**alternativeInceptionDate** | None, str,  | NoneClass, str,  | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. | [optional] 

# metrics

A list of metrics to calculate in the AggregatedReturns.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of metrics to calculate in the AggregatedReturns. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PerformanceReturnsMetric**](PerformanceReturnsMetric.md) | [**PerformanceReturnsMetric**](PerformanceReturnsMetric.md) | [**PerformanceReturnsMetric**](PerformanceReturnsMetric.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

