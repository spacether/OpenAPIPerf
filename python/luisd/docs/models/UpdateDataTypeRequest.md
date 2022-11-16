# luisd.model.update_data_type_request.UpdateDataTypeRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | None, str,  | NoneClass, str,  | The display name of the data type. | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the data type. | [optional] 
**[acceptableValues](#acceptableValues)** | list, tuple, None,  | tuple, NoneClass,  | The acceptable set of values for this data type. Only applies to &#x27;open&#x27; value type range. | [optional] 
**[acceptableUnits](#acceptableUnits)** | list, tuple, None,  | tuple, NoneClass,  | The definitions of the acceptable units. | [optional] 

# acceptableValues

The acceptable set of values for this data type. Only applies to 'open' value type range.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The acceptable set of values for this data type. Only applies to &#x27;open&#x27; value type range. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# acceptableUnits

The definitions of the acceptable units.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The definitions of the acceptable units. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UpdateUnitRequest**](UpdateUnitRequest.md) | [**UpdateUnitRequest**](UpdateUnitRequest.md) | [**UpdateUnitRequest**](UpdateUnitRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

