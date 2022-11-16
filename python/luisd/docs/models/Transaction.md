# luisd.model.transaction.Transaction

A list of transactions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of transactions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**instrumentUid** | str,  | str,  | The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in. | 
**settlementDate** | str, datetime,  | str,  | The settlement date of the transaction. | value must conform to RFC-3339 date-time
**units** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units transacted in the associated instrument. | value must be a 64 bit float
**totalConsideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transactionDate** | str, datetime,  | str,  | The date of the transaction. | value must conform to RFC-3339 date-time
**type** | str,  | str,  | The type of the transaction e.g. &#x27;Buy&#x27;, &#x27;Sell&#x27;. The transaction type should have been pre-configured via the System Configuration API endpoint. | 
**transactionId** | str,  | str,  | The unique identifier for the transaction. | 
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of instrument identifiers that can resolve the transaction to a unique instrument. | [optional] 
**instrumentScope** | None, str,  | NoneClass, str,  | The scope in which the transaction&#x27;s instrument lies. | [optional] 
**transactionPrice** | [**TransactionPrice**](TransactionPrice.md) | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**exchangeRate** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] value must be a 64 bit float
**transactionCurrency** | None, str,  | NoneClass, str,  | The transaction currency. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#x27;Transaction&#x27; domain. | [optional] 
**counterpartyId** | None, str,  | NoneClass, str,  | The identifier for the counterparty of the transaction. | [optional] 
**source** | None, str,  | NoneClass, str,  | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**entryDateTime** | str, datetime,  | str,  | The asAt datetime that the transaction was added to LUSID. | [optional] value must conform to RFC-3339 date-time
**otcConfirmation** | [**OtcConfirmation**](OtcConfirmation.md) | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 

# instrumentIdentifiers

A set of instrument identifiers that can resolve the transaction to a unique instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of instrument identifiers that can resolve the transaction to a unique instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#x27;Transaction&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

