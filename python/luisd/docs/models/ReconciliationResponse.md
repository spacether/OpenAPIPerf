# luisd.model.reconciliation_response.ReconciliationResponse

Class representing the set of comparisons that result from comparing holdings and their valuations between two separate evaluations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Class representing the set of comparisons that result from comparing holdings and their valuations between two separate evaluations. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[comparisons](#comparisons)** | list, tuple, None,  | tuple, NoneClass,  | List of comparisons of left to right hand sides. | [optional] 
**dataSchema** | [**ResultDataSchema**](ResultDataSchema.md) | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 

# comparisons

List of comparisons of left to right hand sides.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of comparisons of left to right hand sides. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReconciliationLine**](ReconciliationLine.md) | [**ReconciliationLine**](ReconciliationLine.md) | [**ReconciliationLine**](ReconciliationLine.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

