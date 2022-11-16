# luisd.model.compounding.Compounding

The compounding settings used on interest rate.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The compounding settings used on interest rate. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**compoundingMethod** | str,  | str,  | If the interest rate is simple or compounded.  Supported string (enumeration) values are: [Average, Compounded, None]. | 
**resetFrequency** | str,  | str,  | The interest payment frequency. | 
**spreadCompoundingMethod** | str,  | str,  | Defines how the computed leg spread is applied to compounded rate.  It applies only when CompoundingMethod &#x3D; ‘Compounded‘.  Supported string (enumeration) values are: [IsdaCompounding, NoCompounding, IsdaFlatCompounding]. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

