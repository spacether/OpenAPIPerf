# luisd.model.flow_convention_name.FlowConventionName

Representation of an abstract definition of a flow convention set consisting of currency, tenor and an index name (arbitrary string but likely something like \"IBOR\").

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Representation of an abstract definition of a flow convention set consisting of currency, tenor and an index name (arbitrary string but likely something like \&quot;IBOR\&quot;). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tenor** | str,  | str,  | Tenor for the convention name. | 
**currency** | str,  | str,  | Currency of the flow convention name. | 
**indexName** | None, str,  | NoneClass, str,  | The index, if present, that is required. e.g. \&quot;IBOR\&quot;, \&quot;OIS\&quot; or \&quot;SONIA\&quot;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

