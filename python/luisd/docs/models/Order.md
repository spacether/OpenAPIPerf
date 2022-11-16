# luisd.model.order.Order

An Order for a certain quantity of a specific instrument

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An Order for a certain quantity of a specific instrument | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**side** | str,  | str,  | The client&#x27;s representation of the order&#x27;s side (buy, sell, short, etc) | 
**portfolioId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | The quantity of given instrument ordered. | value must be a 32 bit integer
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument ordered. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**lusidInstrumentId** | str,  | str,  | The LUSID instrument id for the instrument ordered. | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this order. | [optional] 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**orderBookId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**state** | None, str,  | NoneClass, str,  | The order&#x27;s state (examples: New, PartiallyFilled, ...) | [optional] 
**type** | None, str,  | NoneClass, str,  | The order&#x27;s type (examples: Limit, Market, ...) | [optional] 
**timeInForce** | None, str,  | NoneClass, str,  | The order&#x27;s time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**date** | str, datetime,  | str,  | The date on which the order was made | [optional] value must conform to RFC-3339 date-time
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**orderInstructionId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**packageId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

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

