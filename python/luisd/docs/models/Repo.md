# luisd.model.repo.Repo

IL Repo Instrument; Lusid-ibor internal representation of a Repo instrument  The repurchase (repo) agreement involves the transfer of instruments (the collateral) from the seller to the buyer.  Ownership is transferred and returns to the seller upon completion of the contract. If the collateral depreciates sharply, it is possible that additional  margin/collateral will be required depending upon the terms of the agreement. The buyer agrees not to sell the securities unless there is some condition of default  in the repo contract.  Repurchase of the securities is at the purchase price plus the agreed upon fixed repo rate, this is the Repurchase price, which can be passed directly or calculated.  On the start date, the buyer receives the collateral and pays Cash (PurchasePrice).  On the maturity date, the buyer returns the collateral and receives Cash (RepurchasePrice).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | IL Repo Instrument; Lusid-ibor internal representation of a Repo instrument  The repurchase (repo) agreement involves the transfer of instruments (the collateral) from the seller to the buyer.  Ownership is transferred and returns to the seller upon completion of the contract. If the collateral depreciates sharply, it is possible that additional  margin/collateral will be required depending upon the terms of the agreement. The buyer agrees not to sell the securities unless there is some condition of default  in the repo contract.  Repurchase of the securities is at the purchase price plus the agreed upon fixed repo rate, this is the Repurchase price, which can be passed directly or calculated.  On the start date, the buyer receives the collateral and pays Cash (PurchasePrice).  On the maturity date, the buyer returns the collateral and receives Cash (RepurchasePrice). | 

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
**instrumentType** | str,  | str,  | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | must be one of ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", ] 
**domCcy** | str,  | str,  | The domestic currency of the instrument. | 
**maturityDate** | str, datetime,  | str,  | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | value must conform to RFC-3339 date-time
**accrualBasis** | str,  | str,  | For calculation of interest, the accrual basis to be used.  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**startDate** | str, datetime,  | str,  | The start date of the instrument. This is normally synonymous with the trade-date. | value must conform to RFC-3339 date-time
**[collateral](#collateral)** | list, tuple, None,  | tuple, NoneClass,  | The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected. | [optional] 
**collateralValue** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The full market value of the collateral in domestic currency, before any margin or haircut is applied. | [optional] value must be a 64 bit float
**haircut** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The haircut (or margin percentage) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05.  This is defined as (CollateralValue - PurchasePrice) / CollateralValue.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified. | [optional] value must be a 64 bit float
**margin** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The initial margin (or margin ratio) applied to the collateral, this should be a number greater than or equal to 1.0,  i.e. for a 102% margin this should be 1.02. A value of 1.0 means no margin (100%).  This is defined as CollateralValue / PurchasePrice.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified. | [optional] value must be a 64 bit float
**purchasePrice** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The price the collateral is initially purchased for, this property can be used to explicitly set the purchase price and not require  collateral value and a margin or haircut.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified. | [optional] value must be a 64 bit float
**repoRate** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | the rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity.  This field is used to calculate the Repurchase price.  While this property is optional, one, and only one, of the RepoRate and RepurchasePrice must be specified. | [optional] value must be a 64 bit float
**repurchasePrice** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The price at which the collateral is repurchased, this field is optional and can be explicitly set here or will be calculated  from the PurchasePrice and RepoRate.  One, and only one, of the RepoRate and RepurchasePrice must be specified. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collateral

The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LusidInstrument**](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

