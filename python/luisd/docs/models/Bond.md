# luisd.model.bond.Bond

IL Bond Instrument; Lusid-ibor internal representation of a Bond instrument

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | IL Bond Instrument; Lusid-ibor internal representation of a Bond instrument | 

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
**flowConventions** | [**FlowConventions**](FlowConventions.md) | [**FlowConventions**](FlowConventions.md) |  | 
**principal** | decimal.Decimal, int, float,  | decimal.Decimal,  | The face-value or principal for the bond at outset.  This might be reduced through its lifetime in the event of amortization or similar. | value must be a 64 bit float
**instrumentType** | str,  | str,  | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | must be one of ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", ] 
**couponRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | Simple coupon rate. | value must be a 64 bit float
**domCcy** | str,  | str,  | The domestic currency of the instrument. | 
**maturityDate** | str, datetime,  | str,  | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | value must conform to RFC-3339 date-time
**startDate** | str, datetime,  | str,  | The start date of the instrument. This is normally synonymous with the trade-date. If settle days &#x3D; 0 then this is the initial accrual date of the bond. | value must conform to RFC-3339 date-time
**[identifiers](#identifiers)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | External market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**exDividendDays** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend. This means that if the settlement date falls in the ex-dividend period  then the coupon paid is zero and the accrued interest is negative. The ex-dividend  period is (Next Coupon Payment Date - ExDividendDays, Next Coupon Payment Date). | [optional] value must be a 32 bit integer
**initialCouponDate** | None, str, datetime,  | NoneClass, str,  | The initial coupon date applies to ex-dividends bonds with effectiveAt date before the initial accrual start date. In this case, the initial coupon date is used as an anchor to  generate a bond schedule that allows the computation of the ex-dividend date and hence the right coupon amount and accrued interest. | [optional] value must conform to RFC-3339 date-time
**firstCouponPayDate** | None, str, datetime,  | NoneClass, str,  | The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period. | [optional] value must conform to RFC-3339 date-time
**calculationType** | None, str,  | NoneClass, str,  | The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  The default CalculationType is &#x60;Standard&#x60;, which returns a coupon amount equal to Principal * Coupon Rate / Coupon Frequency. Coupon Frequency is 12M / Payment Frequency.  Payment Frequency can be 1M, 3M, 6M, 12M etc. So Coupon Frequency can be 12, 4, 2, 1 respectively.  Supported string (enumeration) values are: [Standard, DayCountCoupon, NoCalculationFloater, BrazilFixedCoupon]. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# identifiers

External market codes and identifiers for the bond, e.g. ISIN.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | External market codes and identifiers for the bond, e.g. ISIN. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

