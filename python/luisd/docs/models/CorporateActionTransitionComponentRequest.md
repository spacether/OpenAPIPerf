# luisd.model.corporate_action_transition_component_request.CorporateActionTransitionComponentRequest

A single transition component request, when grouped with other transition component requests a corporate action  transition request is formed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A single transition component request, when grouped with other transition component requests a corporate action  transition request is formed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
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

