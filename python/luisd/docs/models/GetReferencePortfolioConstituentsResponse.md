# luisd.model.get_reference_portfolio_constituents_response.GetReferencePortfolioConstituentsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**weightType** | str,  | str,  | The available values are: Static, Floating, Periodical | must be one of ["Static", "Floating", "Periodical", ] 
**[constituents](#constituents)** | list, tuple,  | tuple,  | Set of constituents (instrument/weight pairings) | 
**effectiveFrom** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**periodType** | None, str,  | NoneClass, str,  | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] must be one of ["Daily", "Weekly", "Monthly", "Quarterly", "Annually", ] 
**periodCount** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**href** | None, str,  | NoneClass, str,  | The Uri that returns the same result as the original request,  but may include resolved as at time(s). | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# constituents

Set of constituents (instrument/weight pairings)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set of constituents (instrument/weight pairings) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReferencePortfolioConstituent**](ReferencePortfolioConstituent.md) | [**ReferencePortfolioConstituent**](ReferencePortfolioConstituent.md) | [**ReferencePortfolioConstituent**](ReferencePortfolioConstituent.md) |  | 

# links

Collection of links.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of links. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

