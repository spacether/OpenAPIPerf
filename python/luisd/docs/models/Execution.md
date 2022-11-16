# luisd.model.execution.Execution

The record of a number of executions against a single Placement (directly analogous to  a partial or full fill against a street order).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The record of a number of executions against a single Placement (directly analogous to  a partial or full fill against a street order). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**side** | str,  | str,  | The side (Buy, Sell, ...) of this execution. | 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The quantity of given instrument ordered. | value must be a 64 bit float
**placementId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**settlementCurrencyFxRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The exectuion&#x27;s settlement currency rate. | value must be a 64 bit float
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument ordered. | 
**type** | str,  | str,  | The type of this execution (Market, Limit, etc). | 
**createdDate** | str, datetime,  | str,  | The active date of this execution. | value must conform to RFC-3339 date-time
**settlementCurrency** | str,  | str,  | The execution&#x27;s settlement currency. | 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**counterparty** | str,  | str,  | The market entity this placement is placed with. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**state** | str,  | str,  | The state of this execution (typically a FIX state; Open, Filled, etc). | 
**lusidInstrumentId** | str,  | str,  | The LUSID instrument id for the instrument execution. | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this execution. | [optional] 
**settlementDate** | str, datetime,  | str,  | The (optional) settlement date for this execution | [optional] value must conform to RFC-3339 date-time
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
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

Client-defined properties associated with this execution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this execution. | 

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

