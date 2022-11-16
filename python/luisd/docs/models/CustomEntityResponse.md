# luisd.model.custom_entity_response.CustomEntityResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customEntityId** | str,  | str,  | A unique identifier for the CustomEntity | 
**effectiveRange** | [**DateRange**](DateRange.md) | [**DateRange**](DateRange.md) |  | 
**asAtRange** | [**DateRange**](DateRange.md) | [**DateRange**](DateRange.md) |  | 
**displayName** | str,  | str,  | The display name of the CustomEntity | 
**entityType** | str,  | str,  | The EntityType to be used when relations are created to the CustomEntity | 
**[identifiers](#identifiers)** | list, tuple,  | tuple,  | A collection of CustomEntityIdentifiers that can identify the CustomEntity | 
**[fields](#fields)** | list, tuple,  | tuple,  | A collection of CustomEntityFields that decorate the CustomEntity | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | 
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the CustomEntity | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# identifiers

A collection of CustomEntityIdentifiers that can identify the CustomEntity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of CustomEntityIdentifiers that can identify the CustomEntity | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomEntityIdResponse**](CustomEntityIdResponse.md) | [**CustomEntityIdResponse**](CustomEntityIdResponse.md) | [**CustomEntityIdResponse**](CustomEntityIdResponse.md) |  | 

# fields

A collection of CustomEntityFields that decorate the CustomEntity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of CustomEntityFields that decorate the CustomEntity | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomEntityField**](CustomEntityField.md) | [**CustomEntityField**](CustomEntityField.md) | [**CustomEntityField**](CustomEntityField.md) |  | 

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

