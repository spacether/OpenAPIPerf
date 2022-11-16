# luisd.model.upsert_corporate_actions_response.UpsertCorporateActionsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**[values](#values)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The corporate actions which have been successfully updated or inserted. | [optional] 
**[failed](#failed)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The corporate actions that could not be updated or inserted along with a reason for their failure. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# values

The corporate actions which have been successfully updated or inserted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The corporate actions which have been successfully updated or inserted. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**CorporateAction**](CorporateAction.md) | [**CorporateAction**](CorporateAction.md) | any string name can be used but the value must be the correct type | [optional] 

# failed

The corporate actions that could not be updated or inserted along with a reason for their failure.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The corporate actions that could not be updated or inserted along with a reason for their failure. | 

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

