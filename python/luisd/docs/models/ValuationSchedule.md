# luisd.model.valuation_schedule.ValuationSchedule

Specification object for the valuation schedule, how do we determine which days we wish to perform a valuation upon.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specification object for the valuation schedule, how do we determine which days we wish to perform a valuation upon. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**effectiveAt** | str,  | str,  | The market data time, i.e. the time to run the valuation request effective of. | 
**effectiveFrom** | None, str,  | NoneClass, str,  | If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range. | [optional] 
**tenor** | None, str,  | NoneClass, str,  | Tenor, e.g \&quot;1D\&quot;, \&quot;1M\&quot; to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same. | [optional] 
**rollConvention** | None, str,  | NoneClass, str,  | When Tenor is given and is not equal to \&quot;1D\&quot;, there may be cases where \&quot;date + tenor\&quot; land on non-business days around month end.  In that case, the RollConvention, e.g. modified following \&quot;MF\&quot; would be applied to determine the next GBD. | [optional] 
**[holidayCalendars](#holidayCalendars)** | list, tuple, None,  | tuple, NoneClass,  | The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \&quot;CoppClarke\&quot;.   Note that when the calendars are not available (e.g. when the user has insufficient permissions),   a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. | [optional] 
**[valuationDateTimes](#valuationDateTimes)** | list, tuple, None,  | tuple, NoneClass,  | If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given. | [optional] 

# holidayCalendars

The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \"CoppClarke\".   Note that when the calendars are not available (e.g. when the user has insufficient permissions),   a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \&quot;CoppClarke\&quot;.   Note that when the calendars are not available (e.g. when the user has insufficient permissions),   a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# valuationDateTimes

If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

