# luisd.model.level_step.LevelStep

Item which is stepped in level/quantity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Item which is stepped in level/quantity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | The date from which the level should apply. | value must conform to RFC-3339 date-time
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The quantity which is applied. This might be an absolute, percentage, fractional or other value. | value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

