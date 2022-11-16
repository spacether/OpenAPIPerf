# luisd.model.upsert_quote_request.UpsertQuoteRequest

The details of the quote including its unique identifier, value and lineage.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details of the quote including its unique identifier, value and lineage. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**quoteId** | [**QuoteId**](QuoteId.md) | [**QuoteId**](QuoteId.md) |  | 
**metricValue** | [**MetricValue**](MetricValue.md) | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | None, str,  | NoneClass, str,  | Description of the quote&#x27;s lineage e.g. &#x27;FundAccountant_GreenQuality&#x27;. | [optional] 
**scaleFactor** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1. | [optional] value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

