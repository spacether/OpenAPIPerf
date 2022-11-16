# luisd.model.a2_b_data_record.A2BDataRecord

A2B Record - shows values on, and changes between two dates: A and B

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A2B Record - shows values on, and changes between two dates: A and B | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**portfolioId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**holdingType** | None, str,  | NoneClass, str,  | The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | [optional] 
**instrumentScope** | None, str,  | NoneClass, str,  | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**instrumentUid** | None, str,  | NoneClass, str,  | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**[subHoldingKeys](#subHoldingKeys)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | [optional] 
**currency** | None, str,  | NoneClass, str,  | The holding currency. | [optional] 
**transactionId** | None, str,  | NoneClass, str,  | The unique identifier for the transaction. | [optional] 
**start** | [**A2BCategory**](A2BCategory.md) | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**flows** | [**A2BCategory**](A2BCategory.md) | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**gains** | [**A2BCategory**](A2BCategory.md) | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**carry** | [**A2BCategory**](A2BCategory.md) | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**end** | [**A2BCategory**](A2BCategory.md) | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties which have been requested to be decorated onto the holding. These will be from the &#x27;Instrument&#x27; domain. | [optional] 
**groupId** | None, str,  | NoneClass, str,  | Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon. | [optional] 

# subHoldingKeys

The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**PerpetualProperty**](PerpetualProperty.md) | [**PerpetualProperty**](PerpetualProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# properties

The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The properties which have been requested to be decorated onto the holding. These will be from the &#x27;Instrument&#x27; domain. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

