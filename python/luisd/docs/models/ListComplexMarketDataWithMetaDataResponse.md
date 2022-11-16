# luisd.model.list_complex_market_data_with_meta_data_response.ListComplexMarketDataWithMetaDataResponse

Wraps a Finbourne.WebApi.Interface.Dto.ComplexMarketData.ComplexMarketData object with information that was retrieved from storage with it.  In particular,  the scope that the data was stored in,  and a <seealso cref=\"T:Finbourne.WebApi.Interface.Dto.ComplexMarketData.ComplexMarketDataId\" /> object identifying the market data in that scope.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Wraps a Finbourne.WebApi.Interface.Dto.ComplexMarketData.ComplexMarketData object with information that was retrieved from storage with it.  In particular,  the scope that the data was stored in,  and a &lt;seealso cref&#x3D;\&quot;T:Finbourne.WebApi.Interface.Dto.ComplexMarketData.ComplexMarketDataId\&quot; /&gt; object identifying the market data in that scope. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**scope** | None, str,  | NoneClass, str,  | The scope that the listed ComplexMarketData entity is stored in. | [optional] 
**marketDataId** | [**ComplexMarketDataId**](ComplexMarketDataId.md) | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | [optional] 
**marketData** | [**ComplexMarketData**](ComplexMarketData.md) | [**ComplexMarketData**](ComplexMarketData.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

