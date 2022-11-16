# luisd.model.property_definition.PropertyDefinition

A list of property definitions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of property definitions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | None, str,  | NoneClass, str,  | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**key** | None, str,  | NoneClass, str,  | The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#x27;Portfolio/Manager/Id&#x27;. | [optional] 
**valueType** | str,  | str,  | The type of values that can be associated with this property. This is defined by the property&#x27;s data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel | [optional] must be one of ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel", ] 
**displayName** | None, str,  | NoneClass, str,  | The display name of the property. | [optional] 
**dataTypeId** | [**ResourceId**](ResourceId.md) | [**ResourceId**](ResourceId.md) |  | [optional] 
**type** | str,  | str,  | The type of the property. The available values are: Label, Metric, Information | [optional] must be one of ["Label", "Metric", "Information", ] 
**unitSchema** | str,  | str,  | The units that can be associated with the property&#x27;s values. This is defined by the property&#x27;s data type. The available values are: NoUnits, Basic, Iso4217Currency | [optional] must be one of ["NoUnits", "Basic", "Iso4217Currency", ] 
**domain** | str,  | str,  | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | [optional] must be one of ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "CustomEntity", ] 
**scope** | None, str,  | NoneClass, str,  | The scope that the property exists in. | [optional] 
**code** | None, str,  | NoneClass, str,  | The code of the property. Together with the domain and scope this uniquely identifies the property. | [optional] 
**valueRequired** | bool,  | BoolClass,  | Whether or not a value is always required for this property. | [optional] 
**lifeTime** | str,  | str,  | Describes how the property&#x27;s values can change over time. The available values are: Perpetual, TimeVariant | [optional] must be one of ["Perpetual", "TimeVariant", ] 
**constraintStyle** | None, str,  | NoneClass, str,  | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. | [optional] 
**propertyDefinitionType** | str,  | str,  | The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition | [optional] must be one of ["ValueProperty", "DerivedDefinition", ] 
**propertyDescription** | None, str,  | NoneClass, str,  | A brief description of what a property of this property definition contains. | [optional] 
**derivationFormula** | None, str,  | NoneClass, str,  | The rule that defines how data is composed for a derived property. | [optional] 
**[links](#links)** | list, tuple, None,  | tuple, NoneClass,  | Collection of links. | [optional] 

# links

Collection of links.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Collection of links. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

