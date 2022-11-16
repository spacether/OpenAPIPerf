# luisd.model.fx_forward.FxForward

IL Fx-Forward Instrument; Lusid-ibor internal representation of a Fx Forward instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | IL Fx-Forward Instrument; Lusid-ibor internal representation of a Fx Forward instrument. | 

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
**fgnCcy** | str,  | str,  | The foreign (other) currency of the instrument. In the NDF case, only payments are made in the domestic currency.  For the outright forward, currencies are exchanged. By domestic is then that of the portfolio. | 
**instrumentType** | str,  | str,  | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | must be one of ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", ] 
**domCcy** | str,  | str,  | The domestic currency of the instrument. | 
**maturityDate** | str, datetime,  | str,  | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | value must conform to RFC-3339 date-time
**fgnAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount that is to be paid in the foreign currency on the maturity date. | value must be a 64 bit float
**domAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount that is to be paid in the domestic currency on the maturity date. | value must be a 64 bit float
**startDate** | str, datetime,  | str,  | The start date of the instrument. This is normally synonymous with the trade-date. | value must conform to RFC-3339 date-time
**refSpotRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The reference Fx Spot rate for currency pair Foreign-Domestic that was seen on the trade start date (time). | [optional] value must be a 64 bit float
**isNdf** | bool,  | BoolClass,  | Is the contract an Fx-Forward of \&quot;Non-Deliverable\&quot; type, meaning a single payment in the domestic currency based on the change in fx-rate vs  a reference rate is used. | [optional] 
**fixingDate** | str, datetime,  | str,  | The fixing date. | [optional] value must conform to RFC-3339 date-time
**settlementCcy** | None, str,  | NoneClass, str,  | The settlement currency.  If provided, present value will be calculated in settlement currency, otherwise the domestic currency. Applies only to non-deliverable FX Forwards. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

