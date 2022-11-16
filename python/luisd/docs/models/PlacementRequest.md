# luisd.model.placement_request.PlacementRequest

A request to create or update a Placement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A request to create or update a Placement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**side** | str,  | str,  | The side (Buy, Sell, ...) of this placement. | 
**createdDate** | str, datetime,  | str,  | The active date of this placement. | value must conform to RFC-3339 date-time
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The quantity of given instrument ordered. | value must be a 64 bit float
**[blockIds](#blockIds)** | list, tuple,  | tuple,  | IDs of Blocks associated with this placement. | 
**counterparty** | str,  | str,  | The market entity this placement is placed with. | 
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument ordered. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**state** | str,  | str,  | The state of this placement (typically a FIX state; Open, Filled, etc). | 
**type** | str,  | str,  | The type of this placement (Market, Limit, etc). | 
**timeInForce** | str,  | str,  | The time in force applicable to this placement (GTC, FOK, Day, etc) | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this order. | [optional] 
**limitPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stopPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

# blockIds

IDs of Blocks associated with this placement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | IDs of Blocks associated with this placement. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# instrumentIdentifiers

The instrument ordered.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument ordered. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

Client-defined properties associated with this order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this order. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

