# luisd.model.instrument_definition.InstrumentDefinition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[identifiers](#identifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. | 
**name** | str,  | str,  | The name of the instrument. | 
**[properties](#properties)** | list, tuple, None,  | tuple, NoneClass,  | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#x27;Instrument&#x27; domain. | [optional] 
**lookThroughPortfolioId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**LusidInstrument**](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 

# identifiers

A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**InstrumentIdValue**](InstrumentIdValue.md) | [**InstrumentIdValue**](InstrumentIdValue.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#x27;Instrument&#x27; domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

