# luisd.model.a2_b_breakdown.A2BBreakdown

A2B Breakdown - Shows the total, and each sub-element within an A2B Category

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A2B Breakdown - Shows the total, and each sub-element within an A2B Category | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total value of all the components within this category. | [optional] value must be a 64 bit float
**currency** | None, str,  | NoneClass, str,  | The currency. Applies to the Total, as well as all the componenents. | [optional] 
**[components](#components)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components. | [optional] 

# components

The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int, float,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

