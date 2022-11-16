# luisd.model.complex_market_data_id.ComplexMarketDataId

An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**provider** | str,  | str,  | The platform or vendor that provided the complex market data, e.g. &#x27;DataScope&#x27;, &#x27;LUSID&#x27;, &#x27;ISDA&#x27; etc. | 
**priceSource** | None, str,  | NoneClass, str,  | The source or originator of the complex market data, e.g. a bank or financial institution. | [optional] 
**lineage** | None, str,  | NoneClass, str,  | Description of the complex market data&#x27;s lineage e.g. &#x27;FundAccountant_GreenQuality&#x27;. | [optional] 
**effectiveAt** | None, str,  | NoneClass, str,  | The effectiveAt or cut label that this item of complex market data is/was updated/inserted with. | [optional] 
**marketAsset** | None, str,  | NoneClass, str,  | The name of the market entity that the document represents | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

