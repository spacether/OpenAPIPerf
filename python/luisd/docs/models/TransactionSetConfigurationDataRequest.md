# luisd.model.transaction_set_configuration_data_request.TransactionSetConfigurationDataRequest

A bundle of requests to configure a set of transaction types.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A bundle of requests to configure a set of transaction types. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[transactionConfigRequests](#transactionConfigRequests)** | list, tuple,  | tuple,  | Collection of transaction type models | 
**[sideConfigRequests](#sideConfigRequests)** | list, tuple, None,  | tuple, NoneClass,  | Collection of side definition requests. | [optional] 

# transactionConfigRequests

Collection of transaction type models

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Collection of transaction type models | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md) | [**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md) | [**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md) |  | 

# sideConfigRequests

Collection of side definition requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of side definition requests. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SideConfigurationDataRequest**](SideConfigurationDataRequest.md) | [**SideConfigurationDataRequest**](SideConfigurationDataRequest.md) | [**SideConfigurationDataRequest**](SideConfigurationDataRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

