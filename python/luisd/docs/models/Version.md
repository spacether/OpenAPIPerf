# luisd.model.version.Version

The version metadata.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The version metadata. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**effectiveFrom** | str, datetime,  | str,  | The effective datetime at which this version became valid. Only applies when a single entity is being interacted with. | value must conform to RFC-3339 date-time
**asAtDate** | str, datetime,  | str,  | The asAt datetime at which the data was committed to LUSID. | value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

