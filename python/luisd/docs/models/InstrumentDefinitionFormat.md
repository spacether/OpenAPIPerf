# luisd.model.instrument_definition_format.InstrumentDefinitionFormat

What is the provenance of an instrument. This defines who creates/owns it, what format it is in (e.g. a proprietary format or a common and known one)              and what the version of that is.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | What is the provenance of an instrument. This defines who creates/owns it, what format it is in (e.g. a proprietary format or a common and known one)              and what the version of that is. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceSystem** | str,  | str,  | which source system does the format originate from | 
**vendor** | str,  | str,  | An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID&#x27;s), some won&#x27;t.              The provenance of an instrument indicates who \&quot;owns\&quot; the associated format. | 
**version** | str,  | str,  | Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations&#x27; trade formats. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

