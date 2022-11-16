# luisd.model.equity_option.EquityOption

Lusid-ibor internal representation of a plain vanilla equity option instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Lusid-ibor internal representation of a plain vanilla equity option instrument. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[LusidInstrument](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**optionMaturityDate** | str, datetime,  | str,  | The maturity date of the option. | value must conform to RFC-3339 date-time
**optionType** | str,  | str,  | The available values are: None, Call, Put | must be one of ["None", "Call", "Put", ] 
**instrumentType** | str,  | str,  | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | must be one of ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", ] 
**code** | str,  | str,  | The identifying code for the equity underlying, e.g. &#x27;IBM.N&#x27;. | 
**domCcy** | str,  | str,  | The domestic currency of the instrument. | 
**strike** | decimal.Decimal, int, float,  | decimal.Decimal,  | The strike of the option. | value must be a 64 bit float
**deliveryType** | str,  | str,  | The available values are: Cash, Physical | must be one of ["Cash", "Physical", ] 
**optionSettlementDate** | str, datetime,  | str,  | The settlement date of the option. | value must conform to RFC-3339 date-time
**startDate** | str, datetime,  | str,  | The start date of the instrument. This is normally synonymous with the trade-date. | value must conform to RFC-3339 date-time
**underlyingIdentifier** | str,  | str,  | The available values are: LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode | must be one of ["LusidInstrumentId", "Isin", "Sedol", "Cusip", "ClientInternal", "Figi", "RIC", "QuotePermId", "REDCode", "BBGId", "ICECode", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

