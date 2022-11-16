# luisd.model.holding_adjustment.HoldingAdjustment

The target holdings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The target holdings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[taxLots](#taxLots)** | list, tuple,  | tuple,  | The tax-lots that together make up the target holding. | 
**instrumentUid** | str,  | str,  | The unqiue Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in. | 
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | [optional] 
**instrumentScope** | None, str,  | NoneClass, str,  | The scope of the instrument that the holding adjustment is in. | [optional] 
**[subHoldingKeys](#subHoldingKeys)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#x27;Transaction&#x27; domain. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#x27;Holding&#x27; domain. | [optional] 
**currency** | None, str,  | NoneClass, str,  | The Holding currency. | [optional] 

# taxLots

The tax-lots that together make up the target holding.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The tax-lots that together make up the target holding. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TargetTaxLot**](TargetTaxLot.md) | [**TargetTaxLot**](TargetTaxLot.md) | [**TargetTaxLot**](TargetTaxLot.md) |  | 

# instrumentIdentifiers

A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# subHoldingKeys

The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the 'Transaction' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#x27;Transaction&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

The set of unique holding properties and associated values stored with the target holding. Each property will be from the 'Holding' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#x27;Holding&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

