# luisd.model.transaction_configuration_movement_data_request.TransactionConfigurationMovementDataRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**side** | str,  | str,  | The movement side | 
**movementTypes** | str,  | str,  | . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes, Carry, CarryAsPnl | must be one of ["Settlement", "Traded", "StockMovement", "FutureCash", "Commitment", "Receivable", "CashSettlement", "CashForward", "CashCommitment", "CashReceivable", "Accrual", "CashAccrual", "ForwardFx", "CashFxForward", "UnsettledCashTypes", "Carry", "CarryAsPnl", ] 
**direction** | decimal.Decimal, int,  | decimal.Decimal,  | The movement direction | value must be a 32 bit integer
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties associated with the underlying Movement. | [optional] 
**[mappings](#mappings)** | list, tuple, None,  | tuple, NoneClass,  | This allows you to map a transaction property to a property on the underlying holding. | [optional] 
**name** | None, str,  | NoneClass, str,  | The movement name (optional) | [optional] 

# properties

The properties associated with the underlying Movement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties associated with the underlying Movement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# mappings

This allows you to map a transaction property to a property on the underlying holding.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | This allows you to map a transaction property to a property on the underlying holding. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionPropertyMappingRequest**](TransactionPropertyMappingRequest.md) | [**TransactionPropertyMappingRequest**](TransactionPropertyMappingRequest.md) | [**TransactionPropertyMappingRequest**](TransactionPropertyMappingRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

