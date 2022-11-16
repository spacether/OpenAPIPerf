# luisd.model.create_recipe_request.CreateRecipeRequest

Specification class to request for the creation/supplementing of a configuration recipe

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specification class to request for the creation/supplementing of a configuration recipe | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**effectiveAt** | str,  | str,  | The market data time, i.e. the recipe generated will look for rules with this effectiveAt. | 
**[recipeCreationMarketDataScopes](#recipeCreationMarketDataScopes)** | list, tuple,  | tuple,  | The scopes in which the recipe creation would look for quotes/data. | 
**recipeId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**inlineRecipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**asAt** | None, str, datetime,  | NoneClass, str,  | The asAt date to use | [optional] value must conform to RFC-3339 date-time

# recipeCreationMarketDataScopes

The scopes in which the recipe creation would look for quotes/data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The scopes in which the recipe creation would look for quotes/data. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

