# luisd.model.transaction_request.TransactionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of instrument identifiers that can resolve the transaction to a unique instrument. | 
**settlementDate** | str,  | str,  | The settlement date of the transaction. | 
**units** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the transacted instrument. | value must be a 64 bit float
**totalConsideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transactionDate** | str,  | str,  | The date of the transaction. | 
**type** | str,  | str,  | The type of the transaction, for example &#x27;Buy&#x27; or &#x27;Sell&#x27;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction. | 
**transactionId** | str,  | str,  | The unique identifier of the transaction. | 
**transactionPrice** | [**TransactionPrice**](TransactionPrice.md) | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**exchangeRate** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The exchange rate between the transaction and settlement currency (settlement currency being represented by TotalConsideration.Currency). For example, if the transaction currency is USD and the settlement currency is GBP, this would be the appropriate USD/GBP rate. | [optional] value must be a 64 bit float
**transactionCurrency** | None, str,  | NoneClass, str,  | The transaction currency. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#x27;Transaction&#x27; domain. | [optional] 
**counterpartyId** | None, str,  | NoneClass, str,  | The identifier for the counterparty of the transaction. | [optional] 
**source** | None, str,  | NoneClass, str,  | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 

# instrumentIdentifiers

A set of instrument identifiers that can resolve the transaction to a unique instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of instrument identifiers that can resolve the transaction to a unique instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

A list of unique transaction properties and associated values to store for the transaction. Each property must be from the 'Transaction' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#x27;Transaction&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

