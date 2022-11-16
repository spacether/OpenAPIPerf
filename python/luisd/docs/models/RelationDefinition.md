# luisd.model.relation_definition.RelationDefinition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**relationDefinitionId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**sourceEntityDomain** | None, str,  | NoneClass, str,  | The entity domain of the source entity object. | [optional] 
**targetEntityDomain** | None, str,  | NoneClass, str,  | The entity domain of the target entity object. | [optional] 
**displayName** | None, str,  | NoneClass, str,  | The display name of the relation. | [optional] 
**outwardDescription** | None, str,  | NoneClass, str,  | The description to relate source entity object and target entity object | [optional] 
**inwardDescription** | None, str,  | NoneClass, str,  | The description to relate target entity object and source entity object | [optional] 
**lifeTime** | None, str,  | NoneClass, str,  | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraintStyle** | None, str,  | NoneClass, str,  | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 
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

