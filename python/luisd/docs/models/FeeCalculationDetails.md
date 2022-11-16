# luisd.model.fee_calculation_details.FeeCalculationDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**propertyKey** | str,  | str,  | The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#x27;Portfolio/Manager/Id&#x27;. | 
**[additionalInformation](#additionalInformation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other property keys populated for the fee | 
**fee** | [**CalculationInfo**](CalculationInfo.md) | [**CalculationInfo**](CalculationInfo.md) |  | 
**ruleType** | str,  | str,  | Rule Type | 
**ruleInformation** | str,  | str,  | Rule Sub Type | 
**maxFee** | [**CalculationInfo**](CalculationInfo.md) | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**minFee** | [**CalculationInfo**](CalculationInfo.md) | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 

# additionalInformation

Other property keys populated for the fee

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other property keys populated for the fee | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

