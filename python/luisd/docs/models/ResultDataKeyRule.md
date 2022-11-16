# luisd.model.result_data_key_rule.ResultDataKeyRule

A rule that describes how we resolve (unit) result data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A rule that describes how we resolve (unit) result data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**documentCode** | str,  | str,  | document code that defines which document is desired | 
**resourceKey** | str,  | str,  | The result data key that identifies the address pattern that this is a rule for | 
**supplier** | str,  | str,  | the result resource supplier (where the data comes from) | 
**dataScope** | str,  | str,  | which is the scope in which the data should be found | 
**quoteInterval** | None, str,  | NoneClass, str,  | Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#x27;5D.0D&#x27; to look back 5 days from today (0 days ago). | [optional] 
**asAt** | None, str, datetime,  | NoneClass, str,  | The AsAt predicate specification. | [optional] value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

