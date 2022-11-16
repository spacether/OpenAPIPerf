# luisd.model.get_structured_result_data_response.GetStructuredResultDataResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**[values](#values)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of values that were successfully retrieved. | [optional] 
**[failed](#failed)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# values

The set of values that were successfully retrieved.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of values that were successfully retrieved. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**StructuredResultData**](StructuredResultData.md) | [**StructuredResultData**](StructuredResultData.md) | any string name can be used but the value must be the correct type | [optional] 

# failed

The set of values that could not be retrieved due along with a reason for this, e.g badly formed request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ErrorDetail**](ErrorDetail.md) | [**ErrorDetail**](ErrorDetail.md) | any string name can be used but the value must be the correct type | [optional] 

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

