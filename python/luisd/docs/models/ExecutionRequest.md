# luisd.model.execution_request.ExecutionRequest

A request to create or update a Execution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A request to create or update a Execution. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**side** | str,  | str,  | The side (Buy, Sell, ...) of this execution. | 
**createdDate** | str, datetime,  | str,  | The active date of this execution. | value must conform to RFC-3339 date-time
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The quantity of given instrument ordered. | value must be a 64 bit float
**settlementCurrency** | str,  | str,  | The execution&#x27;s settlement currency. | 
**placementId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**settlementCurrencyFxRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The exectuion&#x27;s settlement currency rate. | value must be a 64 bit float
**counterparty** | str,  | str,  | The market entity this placement is placed with. | 
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The instrument ordered. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**state** | str,  | str,  | The state of this execution (typically a FIX state; Open, Filled, etc). | 
**type** | str,  | str,  | The type of this execution (Market, Limit, etc). | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Client-defined properties associated with this execution. | [optional] 
**settlementDate** | str, datetime,  | str,  | The (optional) settlement date for this execution | [optional] value must conform to RFC-3339 date-time

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

