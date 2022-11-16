# luisd.model.corporate_action_transition.CorporateActionTransition

A 'transition' within a corporate action, representing a set of output movements paired to a single input position

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A &#x27;transition&#x27; within a corporate action, representing a set of output movements paired to a single input position | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inputTransition** | [**CorporateActionTransitionComponent**](CorporateActionTransitionComponent.md) | [**CorporateActionTransitionComponent**](CorporateActionTransitionComponent.md) |  | [optional] 
**[outputTransitions](#outputTransitions)** | list, tuple, None,  | tuple, NoneClass,  | What will be generated relative to the input transition | [optional] 

# outputTransitions

What will be generated relative to the input transition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | What will be generated relative to the input transition | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CorporateActionTransitionComponent**](CorporateActionTransitionComponent.md) | [**CorporateActionTransitionComponent**](CorporateActionTransitionComponent.md) | [**CorporateActionTransitionComponent**](CorporateActionTransitionComponent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

