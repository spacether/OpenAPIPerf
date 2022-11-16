# luisd.model.get_quotes_response.GetQuotesResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**[values](#values)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The quotes which have been successfully retrieved. | [optional] 
**[notFound](#notFound)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The quotes that could not be found along with a reason why. | [optional] 
**[failed](#failed)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The quotes that could not be retrieved due to an error along with a reason for their failure. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# values

The quotes which have been successfully retrieved.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The quotes which have been successfully retrieved. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**Quote**](Quote.md) | [**Quote**](Quote.md) | any string name can be used but the value must be the correct type | [optional] 

# notFound

The quotes that could not be found along with a reason why.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The quotes that could not be found along with a reason why. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ErrorDetail**](ErrorDetail.md) | [**ErrorDetail**](ErrorDetail.md) | any string name can be used but the value must be the correct type | [optional] 

# failed

The quotes that could not be retrieved due to an error along with a reason for their failure.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The quotes that could not be retrieved due to an error along with a reason for their failure. | 

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

