# luisd.model.reconciliation_break.ReconciliationBreak

A reconciliation break

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A reconciliation break | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instrumentProperties](#instrumentProperties)** | list, tuple,  | tuple,  | Additional features relating to the instrument | 
**leftCost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**[subHoldingKeys](#subHoldingKeys)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Any other properties that comprise the Sub-Holding Key | 
**differenceCost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**instrumentUid** | str,  | str,  | Unique instrument identifier | 
**rightCost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**rightUnits** | decimal.Decimal, int, float,  | decimal.Decimal,  | Units from the right hand side | value must be a 64 bit float
**leftUnits** | decimal.Decimal, int, float,  | decimal.Decimal,  | Units from the left hand side | value must be a 64 bit float
**differenceUnits** | decimal.Decimal, int, float,  | decimal.Decimal,  | Difference in units | value must be a 64 bit float

# subHoldingKeys

Any other properties that comprise the Sub-Holding Key

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Any other properties that comprise the Sub-Holding Key | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# instrumentProperties

Additional features relating to the instrument

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional features relating to the instrument | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

