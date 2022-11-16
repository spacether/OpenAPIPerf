# luisd.model.update_instrument_identifier_request.UpdateInstrumentIdentifierRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The allowable instrument identifier to update, insert or remove e.g. &#x27;Figi&#x27;. | 
**value** | None, str,  | NoneClass, str,  | The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument. | [optional] 
**effectiveAt** | None, str,  | NoneClass, str,  | The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

