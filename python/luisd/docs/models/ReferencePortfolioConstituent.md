# luisd.model.reference_portfolio_constituent.ReferencePortfolioConstituent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**instrumentUid** | str,  | str,  | LUSID&#x27;s internal unique instrument identifier, resolved from the instrument identifiers | 
**weight** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float
**currency** | str,  | str,  |  | 
**[instrumentIdentifiers](#instrumentIdentifiers)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Unique instrument identifiers | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Properties associated with the constituent | [optional] 
**floatingWeight** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**instrumentScope** | None, str,  | NoneClass, str,  |  | [optional] 

# instrumentIdentifiers

Unique instrument identifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Unique instrument identifiers | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# properties

Properties associated with the constituent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Properties associated with the constituent | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

