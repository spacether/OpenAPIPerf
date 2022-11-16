# luisd.model.block.Block

A block of orders for the same instrument, intended to record for example a trader's aggregation  of outstanding orders at a given time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A block of orders for the same instrument, intended to record for example a trader&#x27;s aggregation  of outstanding orders at a given time. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**side** | str,  | str,  | The client&#x27;s representation of the block&#x27;s side (buy, sell, short, etc) | 
**createdDate** | str, datetime,  | str,  | The date on which the block was made | value must conform to RFC-3339 date-time
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total quantity of given instrument ordered. | value must be a 64 bit float
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument ordered. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**[orderIds](#orderIds)** | list, tuple,  | tuple,  | The related order ids. | 
**type** | str,  | str,  | The block order&#x27;s type (examples: Limit, Market, ...) | 
**lusidInstrumentId** | str,  | str,  | The LUSID instrument id for the instrument ordered. | 
**timeInForce** | str,  | str,  | The block orders&#x27; time in force (examples: Day, GoodTilCancel, ...) | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this block. | [optional] 
**limitPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stopPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# orderIds

The related order ids.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The related order ids. | 

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

Client-defined properties associated with this block.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this block. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# links

Collection of links.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of links. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

