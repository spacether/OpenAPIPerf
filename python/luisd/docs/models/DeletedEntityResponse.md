# luisd.model.deleted_entity_response.DeletedEntityResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**asAt** | str, datetime,  | str,  | The asAt datetime at which the deletion was committed to LUSID. | value must conform to RFC-3339 date-time
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**effectiveFrom** | None, str, datetime,  | NoneClass, str,  | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. | [optional] value must conform to RFC-3339 date-time
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

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

