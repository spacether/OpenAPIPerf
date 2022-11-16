# luisd.model.performance_returns_metric.PerformanceReturnsMetric

The request used in the AggregatedReturns.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request used in the AggregatedReturns. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | None, str,  | NoneClass, str,  | The type of the metric. Default to Return | [optional] 
**window** | None, str,  | NoneClass, str,  | The given metric for the calculation i.e. 1Y, 1D. | [optional] 
**allowPartial** | bool,  | BoolClass,  | Bool if the metric is allowed partial results. Deafult to false. | [optional] 
**annualised** | bool,  | BoolClass,  | Bool if the metric is annualized. Default to false. | [optional] 
**withFee** | bool,  | BoolClass,  | Bool if the metric should consider the fees when is calculated. Default to false. | [optional] 
**seedAmount** | None, str,  | NoneClass, str,  | The given seed amount for the calculation of the indicative amount metrics. | [optional] 
**alias** | None, str,  | NoneClass, str,  | The alias for the metric. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

