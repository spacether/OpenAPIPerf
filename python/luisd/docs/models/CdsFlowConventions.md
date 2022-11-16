# luisd.model.cds_flow_conventions.CdsFlowConventions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[resetCalendars](#resetCalendars)** | list, tuple,  | tuple,  | An array of strings denoting holiday calendars that apply to generation of reset schedules. | 
**settleDays** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Good Business Days between the trade date and the effective or settlement date of the instrument. | value must be a 32 bit integer
**[paymentCalendars](#paymentCalendars)** | list, tuple,  | tuple,  | An array of strings denoting holiday calendars that apply to generation of payment schedules. | 
**dayCountConvention** | str,  | str,  | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**currency** | str,  | str,  | Currency of the flow convention. | 
**paymentFrequency** | str,  | str,  | When generating a multiperiod flow, or when the maturity of the flow is not given but the start date is,  the tenor is the time-step from the anchor-date to the nominal maturity of the flow prior to any adjustment. | 
**rollConvention** | str,  | str,  | When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day.  Supported string (enumeration) values are: [NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, EndOfMonth, EOM, EndOfMonthPrevious, EOMP, EndOfMonthFollowing, EOMF, HalfMonthModifiedFollowing]. | 
**resetDays** | decimal.Decimal, int,  | decimal.Decimal,  | The number of Good Business Days between determination and payment of reset. | value must be a 32 bit integer
**rollFrequency** | None, str,  | NoneClass, str,  | The frequency at which the reference bonds are updated, this defaults to 6M, but can be 3M, exp for historically issued products | [optional] 
**scope** | None, str,  | NoneClass, str,  | The scope used when updating or inserting the convention. | [optional] 
**code** | None, str,  | NoneClass, str,  | The code of the convention. | [optional] 

# paymentCalendars

An array of strings denoting holiday calendars that apply to generation of payment schedules.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of strings denoting holiday calendars that apply to generation of payment schedules. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# resetCalendars

An array of strings denoting holiday calendars that apply to generation of reset schedules.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of strings denoting holiday calendars that apply to generation of reset schedules. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

