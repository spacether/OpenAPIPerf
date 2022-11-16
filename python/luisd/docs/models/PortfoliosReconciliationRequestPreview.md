# luisd.model.portfolios_reconciliation_request_preview.PortfoliosReconciliationRequestPreview

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**left** | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) |  | 
**[instrumentPropertyKeys](#instrumentPropertyKeys)** | list, tuple,  | tuple,  | Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio | 
**right** | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) |  | 
**[tolerance](#tolerance)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Tolerance to be included for the units and cost. | [optional] 

# instrumentPropertyKeys

Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

# tolerance

Tolerance to be included for the units and cost.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Tolerance to be included for the units and cost. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**Tolerance**](Tolerance.md) | [**Tolerance**](Tolerance.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

