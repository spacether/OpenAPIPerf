# luisd.model.upsert_corporate_action_request.UpsertCorporateActionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**corporateActionCode** | str,  | str,  | The unique identifier of this corporate action | 
**exDate** | str, datetime,  | str,  | The ex date of the corporate action | value must conform to RFC-3339 date-time
**announcementDate** | str, datetime,  | str,  | The announcement date of the corporate action | value must conform to RFC-3339 date-time
**recordDate** | str, datetime,  | str,  | The record date of the corporate action | value must conform to RFC-3339 date-time
**paymentDate** | str, datetime,  | str,  | The payment date of the corporate action | value must conform to RFC-3339 date-time
**[transitions](#transitions)** | list, tuple,  | tuple,  | The transitions that result from this corporate action | 
**description** | None, str,  | NoneClass, str,  | The description of the corporate action. | [optional] 

# transitions

The transitions that result from this corporate action

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The transitions that result from this corporate action | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CorporateActionTransitionRequest**](CorporateActionTransitionRequest.md) | [**CorporateActionTransitionRequest**](CorporateActionTransitionRequest.md) | [**CorporateActionTransitionRequest**](CorporateActionTransitionRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

