# luisd.model.order_graph_block.OrderGraphBlock

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ordered** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**[executionIds](#executionIds)** | list, tuple,  | tuple,  | Identifiers of all executions against placements in the block. | 
**placed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**derivedState** | str,  | str,  | A simple description of the overall state of a block. | 
**[allocationIds](#allocationIds)** | list, tuple,  | tuple,  | Identifiers for all allocations of placements to orders in the block. | 
**block** | [**Block**](Block.md) | [**Block**](Block.md) |  | 
**executed** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 
**[placementIds](#placementIds)** | list, tuple,  | tuple,  | Identifiers of all placements for the block. | 
**[orderIds](#orderIds)** | list, tuple,  | tuple,  | Identifiers for all the orders in this block. | 
**allocated** | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) | [**OrderGraphSynopsis**](OrderGraphSynopsis.md) |  | 

# orderIds

Identifiers for all the orders in this block.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers for all the orders in this block. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# placementIds

Identifiers of all placements for the block.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers of all placements for the block. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# allocationIds

Identifiers for all allocations of placements to orders in the block.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers for all allocations of placements to orders in the block. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# executionIds

Identifiers of all executions against placements in the block.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers of all executions against placements in the block. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

