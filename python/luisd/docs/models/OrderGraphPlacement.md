# luisd.model.order_graph_placement.OrderGraphPlacement

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**blockId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**[executionIds](#executionIds)** | list, tuple,  | tuple,  | Identifiers of all executions against this placement. | 
**placed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**derivedState** | str,  | str,  | A simple description of the overall state of a placement. | 
**[allocationIds](#allocationIds)** | list, tuple,  | tuple,  | Identifiers for all allocations relating to this placement. | 
**executed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**[orderIds](#orderIds)** | list, tuple,  | tuple,  | Identifiers for all orders in the block. | 
**placement** | [**Placement**](Placement.md) | [**Placement**](Placement.md) |  | 
**allocated** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 

# orderIds

Identifiers for all orders in the block.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers for all orders in the block. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# allocationIds

Identifiers for all allocations relating to this placement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers for all allocations relating to this placement. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# executionIds

Identifiers of all executions against this placement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers of all executions against this placement. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

