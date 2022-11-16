# luisd.model.model_property.ModelProperty

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key** | str,  | str,  | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#x27;Instrument/system/Name&#x27; or &#x27;Transaction/strategy/quantsignal&#x27;. | 
**value** | [**PropertyValue**](PropertyValue.md) | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effectiveFrom** | None, str, datetime,  | NoneClass, str,  | The effective datetime from which the property is valid. | [optional] value must conform to RFC-3339 date-time
**effectiveUntil** | None, str, datetime,  | NoneClass, str,  | The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next &#x27;effectiveFrom&#x27; datetime of the property. | [optional] value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

