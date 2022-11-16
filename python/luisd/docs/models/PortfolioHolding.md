# luisd.model.portfolio_holding.PortfolioHolding

A list of holdings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of holdings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**holdingType** | str,  | str,  | The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | 
**instrumentUid** | str,  | str,  | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**units** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of units of the holding. | value must be a 64 bit float
**costPortfolioCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**settledUnits** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of settled units of the holding. | value must be a 64 bit float
**instrumentScope** | None, str,  | NoneClass, str,  | The scope in which the holding&#x27;s instrument is in. | [optional] 
**[subHoldingKeys](#subHoldingKeys)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties which have been requested to be decorated onto the holding. These will be from the &#x27;Instrument&#x27; or &#x27;Holding&#x27; domain. | [optional] 
**transaction** | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | [optional] 
**currency** | None, str,  | NoneClass, str,  | The holding currency. | [optional] 

# subHoldingKeys

The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' or 'Holding' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties which have been requested to be decorated onto the holding. These will be from the &#x27;Instrument&#x27; or &#x27;Holding&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

