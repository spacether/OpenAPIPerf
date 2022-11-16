# luisd.model.equity_swap.EquitySwap

Lusid-ibor internal representation of an Equity Swap instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Lusid-ibor internal representation of an Equity Swap instrument. | 

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
**equityFlowConventions** | [**FlowConventions**](FlowConventions.md) | [**FlowConventions**](FlowConventions.md) |  | 
**includeDividends** | bool,  | BoolClass,  | Dividend inclusion flag, if true dividends are included in the equity leg (total return). | 
**instrumentType** | str,  | str,  | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | must be one of ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", ] 
**code** | str,  | str,  | The code of the underlying. | 
**notionalReset** | bool,  | BoolClass,  | Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity). | 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The quantity or number of shares in the Equity Swap. | value must be a 64 bit float
**fundingLeg** | [**InstrumentLeg**](InstrumentLeg.md) | [**InstrumentLeg**](InstrumentLeg.md) |  | 
**initialPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | The initial equity price of the Equity Swap. | value must be a 64 bit float
**maturityDate** | str, datetime,  | str,  | The maturity date of the EquitySwap. | value must conform to RFC-3339 date-time
**startDate** | str, datetime,  | str,  | The start date of the EquitySwap. | value must conform to RFC-3339 date-time
**underlyingIdentifier** | str,  | str,  | external market codes and identifiers for the EquitySwap, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

