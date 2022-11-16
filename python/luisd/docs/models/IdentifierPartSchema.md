# luisd.model.identifier_part_schema.IdentifierPartSchema

The schema of an contributing part of a valid LUSID resource identifier

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The schema of an contributing part of a valid LUSID resource identifier | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  | The display name of the identifier part | 
**name** | str,  | str,  | The name of the identifier part that can/should be provided for this resource type | 
**description** | str,  | str,  | A brief description of the point of this identifier part | 
**index** | decimal.Decimal, int,  | decimal.Decimal,  | The typical index in the identifier in which this part appears | value must be a 32 bit integer
**required** | bool,  | BoolClass,  | Whether a value is required to be provided | 
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

