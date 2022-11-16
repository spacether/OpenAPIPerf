# luisd.model.create_relation_definition_request.CreateRelationDefinitionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**outwardDescription** | str,  | str,  | The description to relate source entity object and target entity object. | 
**code** | str,  | str,  | The code of the relation. Together with the scope this uniquely defines the relation. | 
**displayName** | str,  | str,  | The display name of the relation. | 
**inwardDescription** | str,  | str,  | The description to relate target entity object and source entity object. | 
**scope** | str,  | str,  | The scope that the relation exists in. | 
**sourceEntityDomain** | str,  | str,  | The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**targetEntityDomain** | str,  | str,  | The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**lifeTime** | None, str,  | NoneClass, str,  | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraintStyle** | None, str,  | NoneClass, str,  | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

