# luisd.model.complete_portfolio.CompletePortfolio

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | 
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | None, str,  | NoneClass, str,  | The long form description of the portfolio. | [optional] 
**displayName** | None, str,  | NoneClass, str,  | The name of the portfolio. | [optional] 
**created** | str, datetime,  | str,  | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | [optional] value must conform to RFC-3339 date-time
**parentPortfolioId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**isDerived** | bool,  | BoolClass,  | Whether or not this is a derived portfolio. | [optional] 
**type** | str,  | str,  | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | [optional] must be one of ["Transaction", "Reference", "DerivedTransaction", ] 
**[properties](#properties)** | list, tuple, None,  | tuple, NoneClass,  | The requested portfolio properties. These will be from the &#x27;Portfolio&#x27; domain. | [optional] 
**baseCurrency** | None, str,  | NoneClass, str,  | If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio. | [optional] 
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

