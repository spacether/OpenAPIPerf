# luisd.model.target_tax_lot_request.TargetTaxLotRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**units** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the instrument in this tax-lot. | value must be a 64 bit float
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**portfolioCost** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The total cost of the tax-lot in the transaction portfolio&#x27;s base currency. | [optional] value must be a 64 bit float
**price** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] value must be a 64 bit float
**purchaseDate** | None, str, datetime,  | NoneClass, str,  | The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] value must conform to RFC-3339 date-time
**settlementDate** | None, str, datetime,  | NoneClass, str,  | The settlement date of the tax-lot&#x27;s opening transaction. | [optional] value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

