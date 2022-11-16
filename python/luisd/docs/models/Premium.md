# luisd.model.premium.Premium

A class containing information for a given premium payment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A class containing information for a given premium payment. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | Date when premium paid. | value must conform to RFC-3339 date-time
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Premium amount. | value must be a 64 bit float
**currency** | str,  | str,  | Premium currency. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

