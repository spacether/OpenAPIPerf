# luisd.model.cap_floor.CapFloor

Interest rate Cap, Floor or Collar  Derivative instrument on an underlying interest rate index.  Cap Type: Buyer will receive payments at the end of each period when floating rate is above the CapStrike level.  Floor Type: Buyer will receive payments at the end of each period when floating rate is below the FloorStrike level.  Collar Type: Strategy of buying one Cap and selling one Floor where FloorStrike is less than CapStrike.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Interest rate Cap, Floor or Collar  Derivative instrument on an underlying interest rate index.  Cap Type: Buyer will receive payments at the end of each period when floating rate is above the CapStrike level.  Floor Type: Buyer will receive payments at the end of each period when floating rate is below the FloorStrike level.  Collar Type: Strategy of buying one Cap and selling one Floor where FloorStrike is less than CapStrike. | 

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
**floorStrike** | decimal.Decimal, int, float,  | decimal.Decimal,  | Strike rate of the Floor. | value must be a 64 bit float
**capFloorType** | str,  | str,  | Determine if it&#x27;s CAP, FLOOR, or COLLAR.  Supported string (enumeration) values are: [Cap, Floor, Collar]. | 
**capStrike** | decimal.Decimal, int, float,  | decimal.Decimal,  | Strike rate of the Cap. | value must be a 64 bit float
**includeFirstCaplet** | bool,  | BoolClass,  | Include first caplet flag. | 
**underlyingFloatingLeg** | [**FloatingLeg**](FloatingLeg.md) | [**FloatingLeg**](FloatingLeg.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

