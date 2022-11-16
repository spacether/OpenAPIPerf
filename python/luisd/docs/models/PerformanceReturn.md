# luisd.model.performance_return.PerformanceReturn

A list of Returns.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of Returns. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**rateOfReturn** | decimal.Decimal, int, float,  | decimal.Decimal,  | The return number. | value must be a 64 bit float
**effectiveAt** | str, datetime,  | str,  | The effectiveAt for the return. | value must conform to RFC-3339 date-time
**openingMarketValue** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The opening market value. | [optional] value must be a 64 bit float
**closingMarketValue** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The closing market value. | [optional] value must be a 64 bit float
**period** | None, str,  | NoneClass, str,  | Upsert the returns on a Daily or Monthly period. Defaults to Daily. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

