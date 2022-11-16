# luisd.model.data_type.DataType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  |  | 
**valueType** | str,  | str,  | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel | must be one of ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel", ] 
**description** | str,  | str,  |  | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**typeValueRange** | str,  | str,  | The available values are: Open, Closed | must be one of ["Open", "Closed", ] 
**href** | None, str,  | NoneClass, str,  |  | [optional] 
**[acceptableValues](#acceptableValues)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**unitSchema** | str,  | str,  | The available values are: NoUnits, Basic, Iso4217Currency | [optional] must be one of ["NoUnits", "Basic", "Iso4217Currency", ] 
**[acceptableUnits](#acceptableUnits)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**referenceData** | [**ReferenceData**](ReferenceData.md) | [**ReferenceData**](ReferenceData.md) |  | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# acceptableValues

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# acceptableUnits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IUnitDefinitionDto**](IUnitDefinitionDto.md) | [**IUnitDefinitionDto**](IUnitDefinitionDto.md) | [**IUnitDefinitionDto**](IUnitDefinitionDto.md) |  | 

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

