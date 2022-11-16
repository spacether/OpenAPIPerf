# luisd.model.upsert_quote_access_metadata_rule_request.UpsertQuoteAccessMetadataRuleRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The access control metadata to assign to quotes that match the identifier | 
**id** | [**QuoteAccessMetadataRuleId**](QuoteAccessMetadataRuleId.md) | [**QuoteAccessMetadataRuleId**](QuoteAccessMetadataRuleId.md) |  | 

# metadata

The access control metadata to assign to quotes that match the identifier

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The access control metadata to assign to quotes that match the identifier | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccessMetadataValue**](AccessMetadataValue.md) | [**AccessMetadataValue**](AccessMetadataValue.md) | [**AccessMetadataValue**](AccessMetadataValue.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

