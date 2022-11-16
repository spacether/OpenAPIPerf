# luisd.model.virtual_document.VirtualDocument

Virtual document consists of (potentially several) upserted documents.                The documents get parsed according to the provided data map on upsert, the collection of resulting values in  aggregated in a virtual document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Virtual document consists of (potentially several) upserted documents.                The documents get parsed according to the provided data map on upsert, the collection of resulting values in  aggregated in a virtual document | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**documentId** | [**StructuredResultDataId**](StructuredResultDataId.md) | [**StructuredResultDataId**](StructuredResultDataId.md) |  | [optional] 
**[data](#data)** | list, tuple, None,  | tuple, NoneClass,  | The data inside the document | [optional] 

# data

The data inside the document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The data inside the document | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VirtualDocumentRow**](VirtualDocumentRow.md) | [**VirtualDocumentRow**](VirtualDocumentRow.md) | [**VirtualDocumentRow**](VirtualDocumentRow.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

