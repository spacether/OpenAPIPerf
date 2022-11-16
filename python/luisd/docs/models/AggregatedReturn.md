# luisd.model.aggregated_return.AggregatedReturn

A list of Aggregated Returns.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of Aggregated Returns. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metricsValue](#metricsValue)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The value for the specified metric. | 
**effectiveAt** | str, datetime,  | str,  | The effectiveAt for the return. | value must conform to RFC-3339 date-time
**openingMarketValue** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The opening market value. | [optional] value must be a 64 bit float
**closingMarketValue** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The closing market value. | [optional] value must be a 64 bit float
**frequency** | None, str,  | NoneClass, str,  | Show the aggregated output returns on a Daily or Monthly period. | [optional] 
**compositeMembers** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of members in the Composite on the given day. | [optional] value must be a 32 bit integer
**[compositeMembersWithoutReturn](#compositeMembersWithoutReturn)** | list, tuple, None,  | tuple, NoneClass,  | List containing Composite members which post no return on the given day. | [optional] 

# metricsValue

The value for the specified metric.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The value for the specified metric. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int, float,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] value must be a 64 bit float

# compositeMembersWithoutReturn

List containing Composite members which post no return on the given day.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List containing Composite members which post no return on the given day. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

