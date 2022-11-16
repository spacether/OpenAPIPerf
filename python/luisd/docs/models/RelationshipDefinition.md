# luisd.model.relationship_definition.RelationshipDefinition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**outwardDescription** | str,  | str,  | The description to relate source entity object and target entity object | 
**sourceEntityType** | str,  | str,  | The entity type of the source entity object. | 
**targetEntityType** | str,  | str,  | The entity type of the target entity object. | 
**displayName** | str,  | str,  | The display name of the relationship. | 
**inwardDescription** | str,  | str,  | The description to relate target entity object and source entity object | 
**relationshipCardinality** | str,  | str,  | Describes the cardinality of the relationship between source entity and target entity. | 
**lifeTime** | str,  | str,  | Describes how the relationships can change over time. | 
**relationshipDefinitionId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
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

