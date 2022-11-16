# luisd.model.adjust_holding_request.AdjustHoldingRequest

This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create &#x27;true-up&#x27; adjustments on the fly. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[taxLots](#taxLots)** | list, tuple,  | tuple,  | The tax-lots that together make up the target holding. | 
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 
**[subHoldingKeys](#subHoldingKeys)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#x27;Transaction&#x27; domain. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#x27;Holding&#x27; domain. | [optional] 
**currency** | None, str,  | NoneClass, str,  | The Holding currency. This needs to be equal with the one on the TaxLot -&gt; cost if one is specified | [optional] 

# instrumentIdentifiers

A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# taxLots

The tax-lots that together make up the target holding.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The tax-lots that together make up the target holding. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TargetTaxLotRequest**](TargetTaxLotRequest.md) | [**TargetTaxLotRequest**](TargetTaxLotRequest.md) | [**TargetTaxLotRequest**](TargetTaxLotRequest.md) |  | 

# subHoldingKeys

Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the 'Transaction' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#x27;Transaction&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

Set of unique holding properties and associated values to store with the target holding. Each property must be from the 'Holding' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#x27;Holding&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

