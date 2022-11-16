# luisd.model.structured_result_data_id.StructuredResultDataId

An identifier that uniquely describes an item of structured result data such as the risk to an interest curve or a set of yields or analytics on an index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An identifier that uniquely describes an item of structured result data such as the risk to an interest curve or a set of yields or analytics on an index. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**source** | str,  | str,  | The platform or vendor that provided the structured result data, e.g. &#x27;client&#x27;. This is primarily of interest when data could have been sourced from multiple sources | 
**code** | None, str,  | NoneClass, str,  | The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data | [optional] 
**effectiveAt** | None, str,  | NoneClass, str,  | The effectiveAt or cut label that this item of structured result data is/was updated/inserted with. | [optional] 
**resultType** | None, str,  | NoneClass, str,  | An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as &#x27;risk result&#x27;, &#x27;cashflow&#x27;, &#x27;index&#x27; or similar. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

