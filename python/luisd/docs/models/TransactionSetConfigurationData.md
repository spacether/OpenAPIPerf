# luisd.model.transaction_set_configuration_data.TransactionSetConfigurationData

A collection of the data required to configure transaction types..

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A collection of the data required to configure transaction types.. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[transactionConfigs](#transactionConfigs)** | list, tuple,  | tuple,  | Collection of transaction type models | 
**[sideDefinitions](#sideDefinitions)** | list, tuple, None,  | tuple, NoneClass,  | Collection of side definitions | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# transactionConfigs

Collection of transaction type models

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Collection of transaction type models | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionConfigurationData**](TransactionConfigurationData.md) | [**TransactionConfigurationData**](TransactionConfigurationData.md) | [**TransactionConfigurationData**](TransactionConfigurationData.md) |  | 

# sideDefinitions

Collection of side definitions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of side definitions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SideConfigurationData**](SideConfigurationData.md) | [**SideConfigurationData**](SideConfigurationData.md) | [**SideConfigurationData**](SideConfigurationData.md) |  | 

# links

Collection of links.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of links. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

