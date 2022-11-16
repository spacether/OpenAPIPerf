# luisd.model.upsert_reference_portfolio_constituents_request.UpsertReferencePortfolioConstituentsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**weightType** | str,  | str,  | The available values are: Static, Floating, Periodical | must be one of ["Static", "Floating", "Periodical", ] 
**[constituents](#constituents)** | list, tuple,  | tuple,  | Set of constituents (instrument/weight pairings) | 
**effectiveFrom** | str,  | str,  | The first date from which the weights will apply | 
**periodType** | None, str,  | NoneClass, str,  | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] must be one of ["Daily", "Weekly", "Monthly", "Quarterly", "Annually", ] 
**periodCount** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 32 bit integer

# constituents

Set of constituents (instrument/weight pairings)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set of constituents (instrument/weight pairings) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReferencePortfolioConstituentRequest**](ReferencePortfolioConstituentRequest.md) | [**ReferencePortfolioConstituentRequest**](ReferencePortfolioConstituentRequest.md) | [**ReferencePortfolioConstituentRequest**](ReferencePortfolioConstituentRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

