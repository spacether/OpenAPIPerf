# luisd.model.corporate_action_transition_component.CorporateActionTransitionComponent

A single transition component, when grouped with other components a corporate action transition is formed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A single transition component, when grouped with other components a corporate action transition is formed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**instrumentScope** | str,  | str,  | The scope in which the instrument lies. | 
**instrumentUid** | str,  | str,  | LUSID&#x27;s internal unique instrument identifier, resolved from the instrument identifiers | 
**costFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  | The factor to scale cost by | value must be a 64 bit float
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Unique instrument identifiers | 
**unitsFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  | The factor to scale units by | value must be a 64 bit float

# instrumentIdentifiers

Unique instrument identifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Unique instrument identifiers | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

