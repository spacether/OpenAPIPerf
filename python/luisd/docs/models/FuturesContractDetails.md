# luisd.model.futures_contract_details.FuturesContractDetails

Most, if not all, information about contracts is standardized. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Most, if not all, information about contracts is standardized. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**convention** | str,  | str,  | If appropriate, the day count convention method used in pricing (rates futures).  Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | 
**country** | str,  | str,  | Country (code) for the exchange. | 
**domCcy** | str,  | str,  | Currency in which the contract is paid. | 
**description** | str,  | str,  | Description of contract. | 
**tickerStep** | decimal.Decimal, int, float,  | decimal.Decimal,  | Minimal step size change in ticker. | value must be a 64 bit float
**contractSize** | decimal.Decimal, int, float,  | decimal.Decimal,  | Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. | value must be a 64 bit float
**exchangeName** | str,  | str,  | Exchange name (for when code is not automatically recognised). | 
**contractMonth** | str,  | str,  | Which month does the contract trade for.  Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z]. | 
**contractCode** | str,  | str,  | The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc. | 
**exchangeCode** | str,  | str,  | Exchange code for contract  Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE, NASDAQ, EEX, LME]. | 
**unitValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | The value in the currency of a 1 unit change in the contract price. | value must be a 64 bit float
**assetClass** | None, str,  | NoneClass, str,  | The asset class of the underlying. Optional and will default to Unknown if not set.  Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money]. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

