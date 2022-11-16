# luisd.model.transaction_configuration_type_alias.TransactionConfigurationTypeAlias

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**transactionRoles** | str,  | str,  | . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles | must be one of ["None", "LongLonger", "LongShorter", "ShortShorter", "Shorter", "ShortLonger", "Longer", "AllRoles", ] 
**transactionClass** | str,  | str,  | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**description** | str,  | str,  | Brief description of the transaction | 
**type** | str,  | str,  | The transaction type | 
**transactionGroup** | None, str,  | NoneClass, str,  | Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead | [optional] 
**source** | None, str,  | NoneClass, str,  | Used to group a set of transaction types | [optional] 
**isDefault** | bool,  | BoolClass,  | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

