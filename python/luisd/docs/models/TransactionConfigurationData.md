# luisd.model.transaction_configuration_data.TransactionConfigurationData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[aliases](#aliases)** | list, tuple,  | tuple,  | List of transaction codes that map to this specific transaction model | 
**[movements](#movements)** | list, tuple,  | tuple,  | Movement data for the transaction code | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Properties attached to the underlying holding. | [optional] 

# aliases

List of transaction codes that map to this specific transaction model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of transaction codes that map to this specific transaction model | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionConfigurationTypeAlias**](TransactionConfigurationTypeAlias.md) | [**TransactionConfigurationTypeAlias**](TransactionConfigurationTypeAlias.md) | [**TransactionConfigurationTypeAlias**](TransactionConfigurationTypeAlias.md) |  | 

# movements

Movement data for the transaction code

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Movement data for the transaction code | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionConfigurationMovementData**](TransactionConfigurationMovementData.md) | [**TransactionConfigurationMovementData**](TransactionConfigurationMovementData.md) | [**TransactionConfigurationMovementData**](TransactionConfigurationMovementData.md) |  | 

# properties

Properties attached to the underlying holding.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Properties attached to the underlying holding. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

