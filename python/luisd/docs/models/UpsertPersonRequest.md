# luisd.model.upsert_person_request.UpsertPersonRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  | The display name of the Person | 
**[identifiers](#identifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of properties associated to the Person. There can be multiple properties associated with a property key. | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the Person | [optional] 

# identifiers

The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

A set of properties associated to the Person. There can be multiple properties associated with a property key.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of properties associated to the Person. There can be multiple properties associated with a property key. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

