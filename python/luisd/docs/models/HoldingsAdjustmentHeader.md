# luisd.model.holdings_adjustment_header.HoldingsAdjustmentHeader

A record of holdings adjustments made on the transaction portfolio.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A record of holdings adjustments made on the transaction portfolio. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**unmatchedHoldingMethod** | str,  | str,  | Describes how the holdings were adjusted. If &#x27;PositionToZero&#x27; the entire transaction portfolio&#x27;s holdings were set via a call to &#x27;Set holdings&#x27;. If &#x27;KeepTheSame&#x27; only the specified holdings were adjusted via a call to &#x27;Adjust holdings&#x27;. The available values are: PositionToZero, KeepTheSame | must be one of ["PositionToZero", "KeepTheSame", ] 
**effectiveAt** | str, datetime,  | str,  | The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment. | value must conform to RFC-3339 date-time
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# links

Collection of links.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of links. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

