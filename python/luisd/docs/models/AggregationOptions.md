# luisd.model.aggregation_options.AggregationOptions

Options for controlling the default aspects and behaviour of the aggregation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Options for controlling the default aspects and behaviour of the aggregation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**useAnsiLikeSyntax** | bool,  | BoolClass,  | Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \&quot;select a,sum(a) from results\&quot;;  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a). | [optional] 
**allowPartialEntitlementSuccess** | bool,  | BoolClass,  | In the case of valuing a portfolio group where some, but not all entitlements fail, should the aggregation return the valuations  applied only to those portfolios where entitlements checks succeeded. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

