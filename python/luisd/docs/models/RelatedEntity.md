# luisd.model.related_entity.RelatedEntity

Information about the other related entity in the relationship

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the other related entity in the relationship | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  | The display name of the entity. | 
**entityType** | str,  | str,  | The type of the entity. | 
**[entityId](#entityId)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The identifier of the other related entity in the relationship. It contains &#x27;scope&#x27; and &#x27;code&#x27; as keys for identifiers of a Portfolio or Portfolio Group, or &#x27;idTypeScope&#x27;, &#x27;idTypeCode&#x27;, &#x27;code&#x27; as keys for identifiers of a Person or Legal Entity. | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties of the entity. This field is empty until further notice. | [optional] 

# entityId

The identifier of the other related entity in the relationship. It contains 'scope' and 'code' as keys for identifiers of a Portfolio or Portfolio Group, or 'idTypeScope', 'idTypeCode', 'code' as keys for identifiers of a Person or Legal Entity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The identifier of the other related entity in the relationship. It contains &#x27;scope&#x27; and &#x27;code&#x27; as keys for identifiers of a Portfolio or Portfolio Group, or &#x27;idTypeScope&#x27;, &#x27;idTypeCode&#x27;, &#x27;code&#x27; as keys for identifiers of a Person or Legal Entity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

The properties of the entity. This field is empty until further notice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties of the entity. This field is empty until further notice. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

