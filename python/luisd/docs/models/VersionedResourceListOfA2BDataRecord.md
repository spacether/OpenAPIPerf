# luisd.model.versioned_resource_list_of_a2_b_data_record.VersionedResourceListOfA2BDataRecord

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[values](#values)** | list, tuple,  | tuple,  | The resources to list. | 
**version** | [**Version**](Version.md) | [**Version**](Version.md) |  | 
**href** | None, str,  | NoneClass, str,  | The URI of the resource list. | [optional] 
**nextPage** | None, str,  | NoneClass, str,  | The next page of results. | [optional] 
**previousPage** | None, str,  | NoneClass, str,  | The previous page of results. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# values

The resources to list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The resources to list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**A2BDataRecord**](A2BDataRecord.md) | [**A2BDataRecord**](A2BDataRecord.md) | [**A2BDataRecord**](A2BDataRecord.md) |  | 

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

