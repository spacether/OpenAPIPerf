# luisd.model.access_controlled_resource.AccessControlledResource

A resource to which access can be controlled

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A resource to which access can be controlled | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | The description of the resource | 
**[actions](#actions)** | list, tuple,  | tuple,  | The actions acceptable for this type of resource | 
**application** | None, str,  | NoneClass, str,  | The application to which this resource belongs | [optional] 
**name** | None, str,  | NoneClass, str,  | The display name of the resource | [optional] 
**[identifierParts](#identifierParts)** | list, tuple, None,  | tuple, NoneClass,  | The constituent parts of a valid identifier for this resource | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# actions

The actions acceptable for this type of resource

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The actions acceptable for this type of resource | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccessControlledAction**](AccessControlledAction.md) | [**AccessControlledAction**](AccessControlledAction.md) | [**AccessControlledAction**](AccessControlledAction.md) |  | 

# identifierParts

The constituent parts of a valid identifier for this resource

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The constituent parts of a valid identifier for this resource | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IdentifierPartSchema**](IdentifierPartSchema.md) | [**IdentifierPartSchema**](IdentifierPartSchema.md) | [**IdentifierPartSchema**](IdentifierPartSchema.md) |  | 

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

