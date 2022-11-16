# luisd.model.data_type_summary.DataTypeSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  | The display name of the data type. | 
**valueType** | str,  | str,  | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel | must be one of ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel", ] 
**description** | str,  | str,  | The description of the data type. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**typeValueRange** | str,  | str,  | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | must be one of ["Open", "Closed", ] 
**[acceptableValues](#acceptableValues)** | list, tuple, None,  | tuple, NoneClass,  | The acceptable set of values for this data type. Only applies to &#x27;open&#x27; value type range. | [optional] 
**unitSchema** | str,  | str,  | The schema of the data type&#x27;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] must be one of ["NoUnits", "Basic", "Iso4217Currency", ] 
**[acceptableUnits](#acceptableUnits)** | list, tuple, None,  | tuple, NoneClass,  | The definitions of the acceptable units. | [optional] 

# acceptableValues

The acceptable set of values for this data type. Only applies to 'open' value type range.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The acceptable set of values for this data type. Only applies to &#x27;open&#x27; value type range. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# acceptableUnits

The definitions of the acceptable units.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The definitions of the acceptable units. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IUnitDefinitionDto**](IUnitDefinitionDto.md) | [**IUnitDefinitionDto**](IUnitDefinitionDto.md) | [**IUnitDefinitionDto**](IUnitDefinitionDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

