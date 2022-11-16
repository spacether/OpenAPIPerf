# luisd.model.create_portfolio_group_request.CreatePortfolioGroupRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. | 
**displayName** | str,  | str,  | The name of the portfolio group. | 
**created** | None, str, datetime,  | NoneClass, str,  | The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified. | [optional] value must conform to RFC-3339 date-time
**[values](#values)** | list, tuple, None,  | tuple, NoneClass,  | The resource identifiers of the portfolios to be contained within the portfolio group. | [optional] 
**[subGroups](#subGroups)** | list, tuple, None,  | tuple, NoneClass,  | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of unique group properties to add to the portfolio group. Each property must be from the &#x27;PortfolioGroup&#x27; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#x27;PortfolioGroup/Manager/Id&#x27;. These properties must be pre-defined. | [optional] 
**description** | None, str,  | NoneClass, str,  | A long form description of the portfolio group. | [optional] 

# values

The resource identifiers of the portfolios to be contained within the portfolio group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The resource identifiers of the portfolios to be contained within the portfolio group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# subGroups

The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

# properties

A set of unique group properties to add to the portfolio group. Each property must be from the 'PortfolioGroup' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'PortfolioGroup/Manager/Id'. These properties must be pre-defined.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of unique group properties to add to the portfolio group. Each property must be from the &#x27;PortfolioGroup&#x27; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#x27;PortfolioGroup/Manager/Id&#x27;. These properties must be pre-defined. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

