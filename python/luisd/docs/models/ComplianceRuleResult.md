# luisd.model.compliance_rule_result.ComplianceRuleResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resultValue** | decimal.Decimal, int, float,  | decimal.Decimal,  | The calculation result that was used to confirm a pass/fail | value must be a 64 bit float
**ruleUpperLimit** | decimal.Decimal, int,  | decimal.Decimal,  | The upper limit of the rule | value must be a 32 bit integer
**ruleLowerLimit** | decimal.Decimal, int,  | decimal.Decimal,  | The lower limit of the rule | value must be a 32 bit integer
**portfolio** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**ruleInformationKey** | str,  | str,  | The property key matched by the rule | 
**ruleName** | str,  | str,  | The User-given name of the rule | 
**ruleInformationMatch** | str,  | str,  | The value matched by the rule | 
**passed** | bool,  | BoolClass,  | The result of an individual compliance run, true if passed | 
**ruleId** | str,  | str,  | The unique identifierof a compliance rule | 
**ruleDescription** | str,  | str,  | The User-given description of the rule | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

