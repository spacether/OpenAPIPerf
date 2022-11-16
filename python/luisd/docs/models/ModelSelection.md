# luisd.model.model_selection.ModelSelection

The combination of a library to use and a model in that library that defines which pricing code will evaluate instruments  having a particular type/class. This allows us to control the model type and library for a given instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The combination of a library to use and a model in that library that defines which pricing code will evaluate instruments  having a particular type/class. This allows us to control the model type and library for a given instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**library** | str,  | str,  | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds | must be one of ["Lusid", "RefinitivQps", "RefinitivTracsWeb", "VolMaster", "IsdaCds", ] 
**model** | str,  | str,  | The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted | must be one of ["SimpleStatic", "Discounting", "VendorDefault", "BlackScholes", "ConstantTimeValueOfMoney", "Bachelier", "ForwardWithPoints", "ForwardWithPointsUndiscounted", "ForwardSpecifiedRate", "ForwardSpecifiedRateUndiscounted", "IndexNav", "IndexPrice", "InlinedIndex", "ForwardFromCurve", "ForwardFromCurveUndiscounted", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

