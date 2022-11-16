# luisd.model.create_sequence_request.CreateSequenceRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The code of the sequence definition to create | 
**increment** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The value to increment between each value in the sequence | [optional] value must be a 64 bit integer
**minValue** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The minimum value of the sequence | [optional] value must be a 64 bit integer
**maxValue** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum value of the sequence | [optional] value must be a 64 bit integer
**start** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The start value of the sequence | [optional] value must be a 64 bit integer
**cycle** | bool,  | BoolClass,  | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. Default to false. | [optional] 
**pattern** | None, str,  | NoneClass, str,  | The pattern to be used to generate next values in the sequence. Default to null. Please provide a null value until further notice. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

