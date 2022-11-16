# luisd.model.corporate_action_source.CorporateActionSource

A corporate action source

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A corporate action source | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**displayName** | None, str,  | NoneClass, str,  | The name of the corporate action source | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the corporate action source | [optional] 
**[instrumentScopes](#instrumentScopes)** | list, tuple, None,  | tuple, NoneClass,  | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

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

