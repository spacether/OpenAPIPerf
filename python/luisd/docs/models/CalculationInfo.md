# luisd.model.calculation_info.CalculationInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**calculationMethod** | str,  | str,  | Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. The available values are: Rate, BasisPoints, Percentage, Flat | must be one of ["Rate", "BasisPoints", "Percentage", "Flat", ] 
**multiplier** | str,  | str,  | . The available values are: None, Quantity, Value | must be one of ["None", "Quantity", "Value", ] 
**calculationDescription** | str,  | str,  | Description of what the calculation applies to eg. Fee, MinFee, MaxFee | 
**calculationAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Numerical fee amount | value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

