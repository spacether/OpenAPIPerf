# luisd.model.quote.Quote

The quote id, value and lineage of the quotes all keyed by a unique correlation id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The quote id, value and lineage of the quotes all keyed by a unique correlation id. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**asAt** | str, datetime,  | str,  | The asAt datetime at which the quote was committed to LUSID. | value must conform to RFC-3339 date-time
**uploadedBy** | str,  | str,  | The unique id of the user that updated or inserted the quote. | 
**quoteId** | [**QuoteId**](QuoteId.md) | [**QuoteId**](QuoteId.md) |  | 
**metricValue** | [**MetricValue**](MetricValue.md) | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | None, str,  | NoneClass, str,  | Description of the quote&#x27;s lineage e.g. &#x27;FundAccountant_GreenQuality&#x27;. | [optional] 
**cutLabel** | None, str,  | NoneClass, str,  | The cut label that this quote was updated or inserted with. | [optional] 
**scaleFactor** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1. | [optional] value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

