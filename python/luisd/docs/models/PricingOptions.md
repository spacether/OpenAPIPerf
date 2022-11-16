# luisd.model.pricing_options.PricingOptions

Options for controlling the default aspects and behaviour of the pricing engine.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Options for controlling the default aspects and behaviour of the pricing engine. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modelSelection** | [**ModelSelection**](ModelSelection.md) | [**ModelSelection**](ModelSelection.md) |  | [optional] 
**useInstrumentTypeToDeterminePricer** | bool,  | BoolClass,  | If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis. | [optional] 
**allowAnyInstrumentsWithSecUidToPriceOffLookup** | bool,  | BoolClass,  | By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true. | [optional] 
**allowPartiallySuccessfulEvaluation** | bool,  | BoolClass,  | If true then a failure in task evaluation doesn&#x27;t cause overall failure.  results will be returned where they succeeded and annotation elsewhere | [optional] 
**produceSeparateResultForLinearOtcLegs** | bool,  | BoolClass,  | If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs. | [optional] 
**enableUseOfCachedUnitResults** | bool,  | BoolClass,  | If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off. | [optional] 
**windowValuationOnInstrumentStartEnd** | bool,  | BoolClass,  | If true, when valuing an instrument outside the period where it is &#x27;alive&#x27; (the start-maturity window) it will return a valuation of zero | [optional] 
**removeContingentCashflowsInPaymentDiary** | bool,  | BoolClass,  | When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not. | [optional] 
**useChildSubHoldingKeysForPortfolioExpansion** | bool,  | BoolClass,  | Should fund constituents inherit subholding keys from the parent subholding keyb | [optional] 
**validateDomesticAndQuoteCurrenciesAreConsistent** | bool,  | BoolClass,  | Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

