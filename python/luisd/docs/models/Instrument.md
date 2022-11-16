# luisd.model.instrument.Instrument

A list of instruments.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of instruments. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[identifiers](#identifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of identifiers that can be used to identify the instrument. | 
**name** | str,  | str,  | The name of the instrument. | 
**state** | str,  | str,  | The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive | must be one of ["Active", "Inactive", ] 
**lusidInstrumentId** | str,  | str,  | The unique LUSID Instrument Identifier (LUID) of the instrument. | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | 
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**scope** | None, str,  | NoneClass, str,  | The scope in which the instrument lies. | [optional] 
**[properties](#properties)** | list, tuple, None,  | tuple, NoneClass,  | The requested instrument properties. These will be from the &#x27;Instrument&#x27; domain. | [optional] 
**lookthroughPortfolio** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrumentDefinition** | [**LusidInstrument**](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**assetClass** | str,  | str,  | The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown | [optional] must be one of ["InterestRates", "FX", "Inflation", "Equities", "Credit", "Commodities", "Money", "Unknown", ] 
**domCcy** | None, str,  | NoneClass, str,  | The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# identifiers

The set of identifiers that can be used to identify the instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of identifiers that can be used to identify the instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

The requested instrument properties. These will be from the 'Instrument' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The requested instrument properties. These will be from the &#x27;Instrument&#x27; domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

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

