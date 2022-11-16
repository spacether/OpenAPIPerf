# luisd.model.configuration_recipe_snippet.ConfigurationRecipeSnippet

If it is desired to have multiple recipes, there is a strong likelihood that they will share various components.  A configuration recipe snippet allows a user to define a set of rules that can then be included into a parent recipe.  This allows sharing of common blocks of the recipe.                For example, a user might define a set of rules for resolving Fx and then include them into every recipe used firm-wide, thereby  enforcing consistency. As the rules can be permissioned differently using Shrine, it is possible to enable users to   read but not alter such a rule set.                The same applies to a set of pricing rules.                A configuration snippet must only contain one entry from the available set.                 Recipes are compiled from the set of snippets through a model that is analogous to inheritance.  A recipe can have a set of 'parent' recipes from which it inherits. These are specified in the inheritance section of a recipe.  Upon loading, the recipe will fall back on these recipe components for any options or rules that are not explicitly specified in the  named recipe for the request.                This allows control of pricing to be harmonised across a set of desks within an institution. Suppose that, e.g.  there are four desks looking after products under the areas of Fx, Rates, Credit and Exotics.  The model and market data for pricing given asset types would potentially be controlled by the appropriate desk; e.g. rules for Fx market data resolution being  controlled by the Fx desk. The exotics desk would likely depend upon rules for all the other asset classes as well as, say, correlation rules of its own.  It could inherit the market data and model rules from the other desks for finding the appropriate institution-standard data and then overlay that with the correlation rules.                Note that permissioning of the store means that one could decide that only a particular desk or control function could update certain rules. That would assist the abilitiy  to ensure that pricing is performed consistently and provide an audit of changes made to it along with restricting changes to appropriate authorised functions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If it is desired to have multiple recipes, there is a strong likelihood that they will share various components.  A configuration recipe snippet allows a user to define a set of rules that can then be included into a parent recipe.  This allows sharing of common blocks of the recipe.                For example, a user might define a set of rules for resolving Fx and then include them into every recipe used firm-wide, thereby  enforcing consistency. As the rules can be permissioned differently using Shrine, it is possible to enable users to   read but not alter such a rule set.                The same applies to a set of pricing rules.                A configuration snippet must only contain one entry from the available set.                 Recipes are compiled from the set of snippets through a model that is analogous to inheritance.  A recipe can have a set of &#x27;parent&#x27; recipes from which it inherits. These are specified in the inheritance section of a recipe.  Upon loading, the recipe will fall back on these recipe components for any options or rules that are not explicitly specified in the  named recipe for the request.                This allows control of pricing to be harmonised across a set of desks within an institution. Suppose that, e.g.  there are four desks looking after products under the areas of Fx, Rates, Credit and Exotics.  The model and market data for pricing given asset types would potentially be controlled by the appropriate desk; e.g. rules for Fx market data resolution being  controlled by the Fx desk. The exotics desk would likely depend upon rules for all the other asset classes as well as, say, correlation rules of its own.  It could inherit the market data and model rules from the other desks for finding the appropriate institution-standard data and then overlay that with the correlation rules.                Note that permissioning of the store means that one could decide that only a particular desk or control function could update certain rules. That would assist the abilitiy  to ensure that pricing is performed consistently and provide an audit of changes made to it along with restricting changes to appropriate authorised functions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | User given string name (code) to identify the recipe. | 
**scope** | str,  | str,  | The scope used when updating or inserting the Configuration Recipe snippet | 
**aggregationOptions** | [**AggregationOptions**](AggregationOptions.md) | [**AggregationOptions**](AggregationOptions.md) |  | [optional] 
**[modelRules](#modelRules)** | list, tuple, None,  | tuple, NoneClass,  | The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options. | [optional] 
**pricingOptions** | [**PricingOptions**](PricingOptions.md) | [**PricingOptions**](PricingOptions.md) |  | [optional] 
**[marketRules](#marketRules)** | list, tuple, None,  | tuple, NoneClass,  | The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible. | [optional] 
**marketOptions** | [**MarketOptions**](MarketOptions.md) | [**MarketOptions**](MarketOptions.md) |  | [optional] 
**recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 

# modelRules

The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VendorModelRule**](VendorModelRule.md) | [**VendorModelRule**](VendorModelRule.md) | [**VendorModelRule**](VendorModelRule.md) |  | 

# marketRules

The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MarketDataKeyRule**](MarketDataKeyRule.md) | [**MarketDataKeyRule**](MarketDataKeyRule.md) | [**MarketDataKeyRule**](MarketDataKeyRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

