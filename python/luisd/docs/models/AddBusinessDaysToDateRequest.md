# luisd.model.add_business_days_to_date_request.AddBusinessDaysToDateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**businessDayOffset** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**[holidayCodes](#holidayCodes)** | list, tuple,  | tuple,  |  | 
**startDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**asAt** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time

# holidayCodes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

