# luisd.model.expanded_group.ExpandedGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  | The name of the portfolio group. | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | None, str,  | NoneClass, str,  | The long form description of the portfolio group. | [optional] 
**[values](#values)** | list, tuple, None,  | tuple, NoneClass,  | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**[subGroups](#subGroups)** | list, tuple, None,  | tuple, NoneClass,  | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# values

The collection of resource identifiers for the portfolios contained in the portfolio group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The collection of resource identifiers for the portfolios contained in the portfolio group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CompletePortfolio**](CompletePortfolio.md) | [**CompletePortfolio**](CompletePortfolio.md) | [**CompletePortfolio**](CompletePortfolio.md) |  | 

# subGroups

The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExpandedGroup**](ExpandedGroup.md) | [**ExpandedGroup**](ExpandedGroup.md) | [**ExpandedGroup**](ExpandedGroup.md) |  | 

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

