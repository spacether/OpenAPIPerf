# luisd.model.access_controlled_action.AccessControlledAction

An action that can be access controlled

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An action that can be access controlled | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**action** | [**ActionId**](ActionId.md) | [**ActionId**](ActionId.md) |  | 
**description** | str,  | str,  | The description of the action | 
**[limitedSet](#limitedSet)** | list, tuple, None,  | tuple, NoneClass,  | When populated, the provided values are the limited set of resources that are allowed to be specified for  access control for this action | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# limitedSet

When populated, the provided values are the limited set of resources that are allowed to be specified for  access control for this action

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | When populated, the provided values are the limited set of resources that are allowed to be specified for  access control for this action | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IdSelectorDefinition**](IdSelectorDefinition.md) | [**IdSelectorDefinition**](IdSelectorDefinition.md) | [**IdSelectorDefinition**](IdSelectorDefinition.md) |  | 

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

