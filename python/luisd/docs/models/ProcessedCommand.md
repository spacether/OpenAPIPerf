# luisd.model.processed_command.ProcessedCommand

The list of commands.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of commands. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | The description of the command issued. | 
**userId** | [**User**](User.md) | [**User**](User.md) |  | 
**processedTime** | str, datetime,  | str,  | The asAt datetime that the events published by the processing of this command were committed to LUSID. | value must conform to RFC-3339 date-time
**path** | None, str,  | NoneClass, str,  | The unique identifier for the command including the request id. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

