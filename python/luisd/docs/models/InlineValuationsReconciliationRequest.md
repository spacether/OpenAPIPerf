# luisd.model.inline_valuations_reconciliation_request.InlineValuationsReconciliationRequest

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a inline set of instruments  using an inline aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based  difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a set of instruments.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a inline set of instruments  using an inline aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based  difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a set of instruments. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**left** | [**InlineValuationRequest**](InlineValuationRequest.md) | [**InlineValuationRequest**](InlineValuationRequest.md) |  | 
**right** | [**InlineValuationRequest**](InlineValuationRequest.md) | [**InlineValuationRequest**](InlineValuationRequest.md) |  | 
**[leftToRightMapping](#leftToRightMapping)** | list, tuple, None,  | tuple, NoneClass,  | The mapping from property keys requested by left aggregation to property keys on right hand side | [optional] 
**[preserveKeys](#preserveKeys)** | list, tuple, None,  | tuple, NoneClass,  | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping | [optional] 

# leftToRightMapping

The mapping from property keys requested by left aggregation to property keys on right hand side

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The mapping from property keys requested by left aggregation to property keys on right hand side | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReconciliationLeftRightAddressKeyPair**](ReconciliationLeftRightAddressKeyPair.md) | [**ReconciliationLeftRightAddressKeyPair**](ReconciliationLeftRightAddressKeyPair.md) | [**ReconciliationLeftRightAddressKeyPair**](ReconciliationLeftRightAddressKeyPair.md) |  | 

# preserveKeys

List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies a queryable address in Lusid. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

