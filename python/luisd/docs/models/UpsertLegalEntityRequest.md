# luisd.model.upsert_legal_entity_request.UpsertLegalEntityRequest

Request to create or update an legal entity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request to create or update an legal entity | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  | The display name of the Legal Entity | 
**[identifiers](#identifiers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of properties associated to the Legal Entity. | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the Legal Entity | [optional] 
**counterpartyRiskInformation** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 

# identifiers

The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

A set of properties associated to the Legal Entity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of properties associated to the Legal Entity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

