# luisd.model.error_detail.ErrorDetail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | None, str,  | NoneClass, str,  | The id of the failed item that this error relates to. | [optional] 
**type** | None, str,  | NoneClass, str,  | The type of failure that occurred. | [optional] 
**detail** | None, str,  | NoneClass, str,  | Description of the failure that occurred. | [optional] 
**[errorDetails](#errorDetails)** | list, tuple, None,  | tuple, NoneClass,  | Information about the particular instance of the failure (supplied information depends on the type of failure). | [optional] 

# errorDetails

Information about the particular instance of the failure (supplied information depends on the type of failure).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Information about the particular instance of the failure (supplied information depends on the type of failure). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

