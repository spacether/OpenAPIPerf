# luisd.model.instrument_match.InstrumentMatch

A collection of instrument search results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A collection of instrument search results | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[masteredInstruments](#masteredInstruments)** | list, tuple, None,  | tuple, NoneClass,  | The collection of instruments found by the search which have been mastered within LUSID. | [optional] 
**[externalInstruments](#externalInstruments)** | list, tuple, None,  | tuple, NoneClass,  | The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI. | [optional] 

# masteredInstruments

The collection of instruments found by the search which have been mastered within LUSID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The collection of instruments found by the search which have been mastered within LUSID. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentDefinition**](InstrumentDefinition.md) | [**InstrumentDefinition**](InstrumentDefinition.md) | [**InstrumentDefinition**](InstrumentDefinition.md) |  | 

# externalInstruments

The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InstrumentDefinition**](InstrumentDefinition.md) | [**InstrumentDefinition**](InstrumentDefinition.md) | [**InstrumentDefinition**](InstrumentDefinition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

