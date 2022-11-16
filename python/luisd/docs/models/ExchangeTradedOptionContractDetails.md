# luisd.model.exchange_traded_option_contract_details.ExchangeTradedOptionContractDetails

Most, if not all, information about contracts is standardised. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.  There is a lot of overlap with this and FuturesContractDetails but as that is an established DTO we must duplicate a number of fields here

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Most, if not all, information about contracts is standardised. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.  There is a lot of overlap with this and FuturesContractDetails but as that is an established DTO we must duplicate a number of fields here | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | Country (code) for the exchange. | 
**domCcy** | str,  | str,  | Currency in which the contract is paid. | 
**exerciseType** | str,  | str,  | The exercise type, European, American or Bermudan.  Supported string (enumeration) values are: [European, Bermudan, American]. | 
**strike** | decimal.Decimal, int, float,  | decimal.Decimal,  | The option strike, this can be negative for some options. | value must be a 64 bit float
**deliveryType** | str,  | str,  | The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.  Supported string (enumeration) values are: [Cash, Physical]. | 
**description** | str,  | str,  | Description of contract | 
**exerciseDate** | str, datetime,  | str,  | Exercise Date. | value must conform to RFC-3339 date-time
**underlying** | [**LusidInstrument**](LusidInstrument.md) | [**LusidInstrument**](LusidInstrument.md) |  | 
**optionType** | str,  | str,  | The option type, Call or Put.  Supported string (enumeration) values are: [Call, Put]. | 
**underlyingCode** | str,  | str,  | Code of the underlying, for an option on futures this should be the futures code. | 
**optionCode** | str,  | str,  | Option Contract Code, typically one or two letters, e.g. OG &#x3D;&gt; Option on Gold. | 
**contractSize** | decimal.Decimal, int, float,  | decimal.Decimal,  | Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. | value must be a 64 bit float
**exchangeCode** | str,  | str,  | Exchange code for contract  Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE, NASDAQ, EEX, LME]. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

