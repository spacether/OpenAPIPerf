# luisd.model.create_derived_property_definition_request.CreateDerivedPropertyDefinitionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**displayName** | str,  | str,  | The display name of the property. | 
**domain** | str,  | str,  | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | must be one of ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "CustomEntity", ] 
**scope** | str,  | str,  | The scope that the property exists in. | 
**dataTypeId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | 
**propertyDescription** | None, str,  | NoneClass, str,  | Describes the property | [optional] 
**derivationFormula** | None, str,  | NoneClass, str,  | The rule that defines how data is composed for a derived property. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

