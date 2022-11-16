# luisd.model.virtual_document_row.VirtualDocumentRow

Rows identified by the composite id, based on the data maps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rows identified by the composite id, based on the data maps | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[rowId](#rowId)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. | [optional] 
**rowData** | [**GroupedResultOfAddressKey**](GroupedResultOfAddressKey.md) | [**GroupedResultOfAddressKey**](GroupedResultOfAddressKey.md) |  | [optional] 

# rowId

The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

