# luisd.model.relation.Relation

Representation of a Relation between a requested entity with the stated entity as RelationedEntityId

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Representation of a Relation between a requested entity with the stated entity as RelationedEntityId | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**traversalDirection** | str,  | str,  |  | 
**relationDefinitionId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**[relatedEntityId](#relatedEntityId)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**traversalDescription** | str,  | str,  |  | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**effectiveFrom** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time

# relatedEntityId

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

