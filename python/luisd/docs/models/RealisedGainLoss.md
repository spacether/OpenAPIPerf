# luisd.model.realised_gain_loss.RealisedGainLoss

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**realisedTotal** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**instrumentUid** | str,  | str,  | The unqiue Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with. | 
**costTradeCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**units** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the associated instrument against which the gain or loss has been realised. | value must be a 64 bit float
**costPortfolioCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realisedTradeCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**purchaseTradeDate** | None, str, datetime,  | NoneClass, str,  | The effective datetime that the units associated with this gain or loss where originally purchased. | [optional] value must conform to RFC-3339 date-time
**purchaseSettlementDate** | None, str, datetime,  | NoneClass, str,  | The effective datetime that the units associated with this gain or loss where originally settled. | [optional] value must conform to RFC-3339 date-time
**purchasePrice** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The purchase price of each unit associated with this gain or loss. | [optional] value must be a 64 bit float
**realisedMarket** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**realisedCurrency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

