# luisd.model.vendor_model_rule.VendorModelRule

A rule that identifies the set of preferences to be used for a given library, model and instrument type.  There can be many such rules, though only the first found for a given combination would be used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A rule that identifies the set of preferences to be used for a given library, model and instrument type.  There can be many such rules, though only the first found for a given combination would be used. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modelName** | str,  | str,  | The vendor library model name | 
**instrumentType** | str,  | str,  | The vendor library instrument type | 
**supplier** | str,  | str,  | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds | must be one of ["Lusid", "RefinitivQps", "RefinitivTracsWeb", "VolMaster", "IsdaCds", ] 
**parameters** | None, str,  | NoneClass, str,  | THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood. | [optional] 
**modelOptions** | [**ModelOptions**](ModelOptions.md) | [**ModelOptions**](ModelOptions.md) |  | [optional] 
**instrumentId** | None, str,  | NoneClass, str,  | This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

