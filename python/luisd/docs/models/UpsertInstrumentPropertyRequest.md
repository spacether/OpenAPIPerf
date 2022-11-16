# luisd.model.upsert_instrument_property_request.UpsertInstrumentPropertyRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**identifier** | str,  | str,  | A value of that type to identify the instrument to upsert properties for, for example &#x27;BBG000BLNNV0&#x27;. | 
**identifierType** | str,  | str,  | The unique identifier type to search for the instrument, for example &#x27;Figi&#x27;. | 
**[properties](#properties)** | list, tuple, None,  | tuple, NoneClass,  | A set of instrument properties and associated values to store for the instrument. Each property must be from the &#x27;Instrument&#x27; domain. | [optional] 

# properties

A set of instrument properties and associated values to store for the instrument. Each property must be from the 'Instrument' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A set of instrument properties and associated values to store for the instrument. Each property must be from the &#x27;Instrument&#x27; domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

