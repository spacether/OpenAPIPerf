# luisd.model.create_corporate_action_source_request.CreateCorporateActionSourceRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The code of the corporate action source | 
**displayName** | str,  | str,  | The name of the corporate action source | 
**scope** | str,  | str,  | The scope of the corporate action source | 
**description** | None, str,  | NoneClass, str,  | The description of the corporate action source | [optional] 
**[instrumentScopes](#instrumentScopes)** | list, tuple, None,  | tuple, NoneClass,  | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | [optional] 

# instrumentScopes

The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

