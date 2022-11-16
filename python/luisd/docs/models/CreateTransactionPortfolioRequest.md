# luisd.model.create_transaction_portfolio_request.CreateTransactionPortfolioRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The code of the transaction portfolio. Together with the scope this uniquely identifies the transaction portfolio. | 
**displayName** | str,  | str,  | The name of the transaction portfolio. | 
**baseCurrency** | str,  | str,  | The base currency of the transaction portfolio in ISO 4217 currency code format. | 
**description** | None, str,  | NoneClass, str,  | A description for the transaction portfolio. | [optional] 
**created** | None, str, datetime,  | NoneClass, str,  | The effective datetime at which to create the transaction portfolio. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified. | [optional] value must conform to RFC-3339 date-time
**corporateActionSourceId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**accountingMethod** | str,  | str,  | Determines the accounting treatment given to the transaction portfolio&#x27;s tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] must be one of ["Default", "AverageCost", "FirstInFirstOut", "LastInFirstOut", "HighestCostFirst", "LowestCostFirst", ] 
**[subHoldingKeys](#subHoldingKeys)** | list, tuple, None,  | tuple, NoneClass,  | A set of unique transaction properties to group the transaction portfolio&#x27;s holdings by, perhaps for strategy tagging. Each property must be from the &#x27;Transaction&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Transaction/strategies/quantsignal&#x27;. Note that sub-holding keys cannot currently be added after the transaction portfolio has been created; see https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**[properties](#properties)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the &#x27;Portfolio&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Portfolio/Manager/Id&#x27;. Note these properties must be pre-defined. | [optional] 
**[instrumentScopes](#instrumentScopes)** | list, tuple, None,  | tuple, NoneClass,  | The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio. | [optional] 

# subHoldingKeys

A set of unique transaction properties to group the transaction portfolio's holdings by, perhaps for strategy tagging. Each property must be from the 'Transaction' domain and identified by a key in the format {domain}/{scope}/{code}, for example 'Transaction/strategies/quantsignal'. Note that sub-holding keys cannot currently be added after the transaction portfolio has been created; see https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A set of unique transaction properties to group the transaction portfolio&#x27;s holdings by, perhaps for strategy tagging. Each property must be from the &#x27;Transaction&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Transaction/strategies/quantsignal&#x27;. Note that sub-holding keys cannot currently be added after the transaction portfolio has been created; see https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

# properties

A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the 'Portfolio' domain and identified by a key in the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. Note these properties must be pre-defined.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the &#x27;Portfolio&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Portfolio/Manager/Id&#x27;. Note these properties must be pre-defined. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | any string name can be used but the value must be the correct type | [optional] 

# instrumentScopes

The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

