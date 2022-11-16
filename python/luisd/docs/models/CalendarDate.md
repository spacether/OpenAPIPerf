# luisd.model.calendar_date.CalendarDate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timezone** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**fromUtc** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**dateIdentifier** | str,  | str,  |  | 
**localDate** | str,  | str,  |  | 
**type** | str,  | str,  |  | 
**toUtc** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**href** | None, str,  | NoneClass, str,  |  | [optional] 
**attributes** | [**DateAttributes**](DateAttributes.md) | [**DateAttributes**](DateAttributes.md) |  | [optional] 
**[sourceData](#sourceData)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 

# sourceData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

