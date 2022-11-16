# luisd.model.sequence_definition.SequenceDefinition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**minValue** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum value of the sequence | value must be a 64 bit integer
**maxValue** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum value of the sequence | value must be a 64 bit integer
**start** | decimal.Decimal, int,  | decimal.Decimal,  | The start value of the sequence | value must be a 64 bit integer
**increment** | decimal.Decimal, int,  | decimal.Decimal,  | The Resource Id of the sequence definition | value must be a 64 bit integer
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**cycle** | bool,  | BoolClass,  | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. | 
**value** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The last used value of the sequence | [optional] value must be a 64 bit integer
**pattern** | None, str,  | NoneClass, str,  | The pattern to be used to generate next values in the sequence. | [optional] 
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

