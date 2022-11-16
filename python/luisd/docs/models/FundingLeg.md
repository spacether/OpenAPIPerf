# luisd.model.funding_leg.FundingLeg

IL FundingLeg Instrument; Lusid-ibor internal representation of a funding leg with variable notional.  This instrument is a hybrid between a single leg swap and a bank account, in that the notional is not fixed but  can be changed over it's life. The use case for this is to represent the funding leg of a basket of instruments  (e.g. equities) where the contents of the basket can change over time.  The actual notional history is stored in the FundingLegHistory object (implements IHistory) and this can be updated  externally or in some circumstances automatically by LUSID.  The main analytic calculated for this instrument is Accrual rather than PV.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | IL FundingLeg Instrument; Lusid-ibor internal representation of a funding leg with variable notional.  This instrument is a hybrid between a single leg swap and a bank account, in that the notional is not fixed but  can be changed over it&#x27;s life. The use case for this is to represent the funding leg of a basket of instruments  (e.g. equities) where the contents of the basket can change over time.  The actual notional history is stored in the FundingLegHistory object (implements IHistory) and this can be updated  externally or in some circumstances automatically by LUSID.  The main analytic calculated for this instrument is Accrual rather than PV. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[InstrumentLeg](InstrumentLeg.md) | [**InstrumentLeg**](InstrumentLeg.md) | [**InstrumentLeg**](InstrumentLeg.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**instrumentType** | str,  | str,  | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | must be one of ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", ] 
**notional** | decimal.Decimal, int, float,  | decimal.Decimal,  | Scaling factor to apply to leg quantities. | value must be a 64 bit float
**maturityDate** | str, datetime,  | str,  | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | value must conform to RFC-3339 date-time
**legDefinition** | [**LegDefinition**](LegDefinition.md) | [**LegDefinition**](LegDefinition.md) |  | 
**startDate** | str, datetime,  | str,  | The start date of the instrument. This is normally synonymous with the trade-date. | value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

