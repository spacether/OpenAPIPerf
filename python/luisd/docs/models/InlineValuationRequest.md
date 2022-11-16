# luisd.model.inline_valuation_request.InlineValuationRequest

Specification object for the parameters of an inline valuation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specification object for the parameters of an inline valuation | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instruments](#instruments)** | list, tuple,  | tuple,  | The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case. | 
**[metrics](#metrics)** | list, tuple,  | tuple,  | The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#x27;Holding/default/PV&#x27;,&#x27;Sum&#x27;) for returning the PV (present value) of holdings  AggregateSpec(&#x27;Holding/default/Units&#x27;,&#x27;Sum&#x27;) for returning the units of holidays  AggregateSpec(&#x27;Instrument/default/LusidInstrumentId&#x27;,&#x27;Value&#x27;) for returning the Lusid Instrument identifier | 
**recipeId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**asAt** | None, str, datetime,  | NoneClass, str,  | The asAt date to use | [optional] value must conform to RFC-3339 date-time
**[groupBy](#groupBy)** | list, tuple, None,  | tuple, NoneClass,  | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | [optional] 
**[filters](#filters)** | list, tuple, None,  | tuple, NoneClass,  | A set of filters to use to reduce the data found in a request. Equivalent to the &#x27;where ...&#x27; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value. | [optional] 
**[sort](#sort)** | list, tuple, None,  | tuple, NoneClass,  | A (possibly empty/null) set of specifications for how to order the results. | [optional] 
**reportCurrency** | None, str,  | NoneClass, str,  | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place. | [optional] 
**equipWithSubtotals** | bool,  | BoolClass,  | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 
**valuationSchedule** | [**ValuationSchedule**](ValuationSchedule.md) | [**ValuationSchedule**](ValuationSchedule.md) |  | [optional] 

# metrics

The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec('Holding/default/PV','Sum') for returning the PV (present value) of holdings  AggregateSpec('Holding/default/Units','Sum') for returning the units of holidays  AggregateSpec('Instrument/default/LusidInstrumentId','Value') for returning the Lusid Instrument identifier

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#x27;Holding/default/PV&#x27;,&#x27;Sum&#x27;) for returning the PV (present value) of holdings  AggregateSpec(&#x27;Holding/default/Units&#x27;,&#x27;Sum&#x27;) for returning the units of holidays  AggregateSpec(&#x27;Instrument/default/LusidInstrumentId&#x27;,&#x27;Value&#x27;) for returning the Lusid Instrument identifier | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AggregateSpec**](AggregateSpec.md) | [**AggregateSpec**](AggregateSpec.md) | [**AggregateSpec**](AggregateSpec.md) |  | 

# instruments

The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WeightedInstrument**](WeightedInstrument.md) | [**WeightedInstrument**](WeightedInstrument.md) | [**WeightedInstrument**](WeightedInstrument.md) |  | 

# groupBy

The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies a queryable address in Lusid. | 

# filters

A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A set of filters to use to reduce the data found in a request. Equivalent to the &#x27;where ...&#x27; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PropertyFilter**](PropertyFilter.md) | [**PropertyFilter**](PropertyFilter.md) | [**PropertyFilter**](PropertyFilter.md) |  | 

# sort

A (possibly empty/null) set of specifications for how to order the results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A (possibly empty/null) set of specifications for how to order the results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderBySpec**](OrderBySpec.md) | [**OrderBySpec**](OrderBySpec.md) | [**OrderBySpec**](OrderBySpec.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

