# luisd.model.complete_relationship.CompleteRelationship

Representation of a relationship containing details of source and target entities, and both outward and inward descriptions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Representation of a relationship containing details of source and target entities, and both outward and inward descriptions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**outwardDescription** | str,  | str,  | Description of the relationship based on relationship definition&#x27;s outward description. | 
**sourceEntity** | [**RelatedEntity**](RelatedEntity.md) | [**RelatedEntity**](RelatedEntity.md) |  | 
**targetEntity** | [**RelatedEntity**](RelatedEntity.md) | [**RelatedEntity**](RelatedEntity.md) |  | 
**inwardDescription** | str,  | str,  | Description of the relationship based on relationship definition&#x27;s inward description. | 
**relationshipDefinitionId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**effectiveFrom** | str, datetime,  | str,  | The effective datetime from which the relationship is valid. | [optional] value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

