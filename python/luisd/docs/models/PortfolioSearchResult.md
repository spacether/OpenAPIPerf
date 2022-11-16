# luisd.model.portfolio_search_result.PortfolioSearchResult

A list of portfolios.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of portfolios. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str, datetime,  | str,  | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | value must conform to RFC-3339 date-time
**displayName** | str,  | str,  | The name of the portfolio. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**type** | str,  | str,  | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | must be one of ["Transaction", "Reference", "DerivedTransaction", ] 
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | None, str,  | NoneClass, str,  | The long form description of the portfolio. | [optional] 
**isDerived** | bool,  | BoolClass,  | Whether or not this is a derived portfolio. | [optional] 
**parentPortfolioId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**baseCurrency** | None, str,  | NoneClass, str,  | The base currency of the portfolio. This will be an empty string for reference portfolios. | [optional] 
**[properties](#properties)** | list, tuple, None,  | tuple, NoneClass,  | The requested portfolio properties. These will be from the &#x27;Portfolio&#x27; domain. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# properties

The requested portfolio properties. These will be from the 'Portfolio' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The requested portfolio properties. These will be from the &#x27;Portfolio&#x27; domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

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

