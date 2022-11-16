# luisd.model.allocation.Allocation

An Allocation of a certain quantity of a specific instrument against an originating  Order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An Allocation of a certain quantity of a specific instrument against an originating  Order. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allocatedOrderId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**portfolioId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | The quantity of given instrument allocated. | value must be a 32 bit integer
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument allocated. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**lusidInstrumentId** | str,  | str,  | The LUSID instrument id for the instrument allocated. | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this allocation. | [optional] 
**[placementIds](#placementIds)** | list, tuple, None,  | tuple, NoneClass,  | A placement - also known as an order placed in the market - associated with this allocation. | [optional] 
**state** | None, str,  | NoneClass, str,  | The state of this allocation. | [optional] 
**side** | None, str,  | NoneClass, str,  | The side of this allocation (examples: Buy, Sell, ...). | [optional] 
**type** | None, str,  | NoneClass, str,  | The type of order associated with this allocation (examples: Limit, Market, ...). | [optional] 
**settlementDate** | str, datetime,  | str,  | The settlement date for this allocation. | [optional] value must conform to RFC-3339 date-time
**date** | str, datetime,  | str,  | The date of this allocation. | [optional] value must conform to RFC-3339 date-time
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**settlementCurrency** | None, str,  | NoneClass, str,  | The settlement currency of this allocation. | [optional] 
**settlementCurrencyFxRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The settlement currency to allocation currency FX rate. | [optional] value must be a 64 bit float
**counterparty** | None, str,  | NoneClass, str,  | The counterparty for this allocation. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# instrumentIdentifiers

The instrument allocated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument allocated. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

Client-defined properties associated with this allocation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this allocation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# placementIds

A placement - also known as an order placed in the market - associated with this allocation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A placement - also known as an order placed in the market - associated with this allocation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

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

