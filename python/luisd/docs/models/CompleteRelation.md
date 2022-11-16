# luisd.model.complete_relation.CompleteRelation

Representation of a relation containing details of source and target entities, and both outward and inward descriptions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Representation of a relation containing details of source and target entities, and both outward and inward descriptions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[targetEntityId](#targetEntityId)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**outwardDescription** | str,  | str,  |  | 
**inwardDescription** | str,  | str,  |  | 
**[sourceEntityId](#sourceEntityId)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**relationDefinitionId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**href** | None, str,  | NoneClass, str,  |  | [optional] 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**effectiveFrom** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time

# sourceEntityId

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# targetEntityId

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

