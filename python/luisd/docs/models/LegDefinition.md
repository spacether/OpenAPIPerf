# luisd.model.leg_definition.LegDefinition

Definition of the set of flow and index conventions along with other miscellaneous information required to generate an instrument leg.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of the set of flow and index conventions along with other miscellaneous information required to generate an instrument leg. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payReceive** | str,  | str,  | Is the leg to be paid or received  Supported string (enumeration) values are: [Pay, Receive]. | 
**notionalExchangeType** | str,  | str,  | what type of notional exchange does the leg have  Supported string (enumeration) values are: [None, Initial, Final, Both]. | 
**stubType** | str,  | str,  | If a stub is required should it be at the front or back of the leg.  Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both]. | 
**rateOrSpread** | decimal.Decimal, int, float,  | decimal.Decimal,  | Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. | value must be a 64 bit float
**conventionName** | [**FlowConventionName**](FlowConventionName.md) | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**conventions** | [**FlowConventions**](FlowConventions.md) | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**indexConvention** | [**IndexConvention**](IndexConvention.md) | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**indexConventionName** | [**FlowConventionName**](FlowConventionName.md) | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**resetConvention** | None, str,  | NoneClass, str,  | Control how resets are generated relative to swap payment convention(s).  Supported string (enumeration) values are: [InAdvance, InArrears]. | [optional] 
**compounding** | [**Compounding**](Compounding.md) | [**Compounding**](Compounding.md) |  | [optional] 
**amortisation** | [**StepSchedule**](StepSchedule.md) | [**StepSchedule**](StepSchedule.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

