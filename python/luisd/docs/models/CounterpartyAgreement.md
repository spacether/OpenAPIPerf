# luisd.model.counterparty_agreement.CounterpartyAgreement

Represents the legal agreement between two parties engaged in an OTC transaction.  A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents the legal agreement between two parties engaged in an OTC transaction.  A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**agreementType** | str,  | str,  | A user-defined field to capture the type of agreement this represents. Examples might be \&quot;ISDA 2002 Master Agreement\&quot; or \&quot;ISDA 1992 Master Agreement\&quot;. | 
**datedAsOf** | str, datetime,  | str,  | The date on which the CounterpartyAgreement was signed by both parties. | value must conform to RFC-3339 date-time
**displayName** | str,  | str,  | A user-defined display label for the Counterparty Agreement. | 
**counterpartySignatory** | [**CounterpartySignatory**](CounterpartySignatory.md) | [**CounterpartySignatory**](CounterpartySignatory.md) |  | 
**creditSupportAnnexId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

