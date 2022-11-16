# luisd.model.structured_result_data.StructuredResultData

An item of structured result data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of result data appropriate to a specific entity such as an instrument or potentially an index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An item of structured result data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of result data appropriate to a specific entity such as an instrument or potentially an index. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**document** | str,  | str,  | The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields | 
**documentFormat** | str,  | str,  | The format of the accompanying document. | 
**version** | None, str,  | NoneClass, str,  | The semantic version of the document format; MAJOR.MINOR.PATCH | [optional] 
**name** | None, str,  | NoneClass, str,  | The name or description for the document | [optional] 
**dataMapKey** | [**DataMapKey**](DataMapKey.md) | [**DataMapKey**](DataMapKey.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

