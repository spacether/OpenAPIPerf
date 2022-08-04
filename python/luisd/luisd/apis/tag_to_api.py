import typing

from luisd.apis.tags import TagValues
from luisd.apis.tags.aggregation_api import AggregationApi
from luisd.apis.tags.allocations_api import AllocationsApi
from luisd.apis.tags.application_metadata_api import ApplicationMetadataApi
from luisd.apis.tags.blocks_api import BlocksApi
from luisd.apis.tags.calendars_api import CalendarsApi
from luisd.apis.tags.complex_market_data_api import ComplexMarketDataApi
from luisd.apis.tags.compliance_api import ComplianceApi
from luisd.apis.tags.configuration_recipe_api import ConfigurationRecipeApi
from luisd.apis.tags.conventions_api import ConventionsApi
from luisd.apis.tags.corporate_action_sources_api import CorporateActionSourcesApi
from luisd.apis.tags.counterparties_api import CounterpartiesApi
from luisd.apis.tags.custom_entities_api import CustomEntitiesApi
from luisd.apis.tags.custom_entity_definitions_api import CustomEntityDefinitionsApi
from luisd.apis.tags.cut_label_definitions_api import CutLabelDefinitionsApi
from luisd.apis.tags.data_types_api import DataTypesApi
from luisd.apis.tags.derived_transaction_portfolios_api import DerivedTransactionPortfoliosApi
from luisd.apis.tags.entities_api import EntitiesApi
from luisd.apis.tags.executions_api import ExecutionsApi
from luisd.apis.tags.fees_and_commissions_api import FeesAndCommissionsApi
from luisd.apis.tags.instruments_api import InstrumentsApi
from luisd.apis.tags.legal_entities_api import LegalEntitiesApi
from luisd.apis.tags.order_graph_api import OrderGraphApi
from luisd.apis.tags.order_instructions_api import OrderInstructionsApi
from luisd.apis.tags.orders_api import OrdersApi
from luisd.apis.tags.packages_api import PackagesApi
from luisd.apis.tags.participations_api import ParticipationsApi
from luisd.apis.tags.persons_api import PersonsApi
from luisd.apis.tags.placements_api import PlacementsApi
from luisd.apis.tags.portfolio_groups_api import PortfolioGroupsApi
from luisd.apis.tags.portfolios_api import PortfoliosApi
from luisd.apis.tags.property_definitions_api import PropertyDefinitionsApi
from luisd.apis.tags.quotes_api import QuotesApi
from luisd.apis.tags.reconciliations_api import ReconciliationsApi
from luisd.apis.tags.reference_portfolio_api import ReferencePortfolioApi
from luisd.apis.tags.relation_definitions_api import RelationDefinitionsApi
from luisd.apis.tags.relations_api import RelationsApi
from luisd.apis.tags.relationship_definitions_api import RelationshipDefinitionsApi
from luisd.apis.tags.relationships_api import RelationshipsApi
from luisd.apis.tags.schemas_api import SchemasApi
from luisd.apis.tags.scopes_api import ScopesApi
from luisd.apis.tags.search_api import SearchApi
from luisd.apis.tags.sequences_api import SequencesApi
from luisd.apis.tags.structured_result_data_api import StructuredResultDataApi
from luisd.apis.tags.system_configuration_api import SystemConfigurationApi
from luisd.apis.tags.transaction_portfolios_api import TransactionPortfoliosApi
from luisd.apis.tags.translation_api import TranslationApi

TagToApi = typing.TypedDict(
    'TagToApi',
    {
        TagValues.AGGREGATION: AggregationApi,
        TagValues.ALLOCATIONS: AllocationsApi,
        TagValues.APPLICATION_METADATA: ApplicationMetadataApi,
        TagValues.BLOCKS: BlocksApi,
        TagValues.CALENDARS: CalendarsApi,
        TagValues.COMPLEX_MARKET_DATA: ComplexMarketDataApi,
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.CONFIGURATION_RECIPE: ConfigurationRecipeApi,
        TagValues.CONVENTIONS: ConventionsApi,
        TagValues.CORPORATE_ACTION_SOURCES: CorporateActionSourcesApi,
        TagValues.COUNTERPARTIES: CounterpartiesApi,
        TagValues.CUSTOM_ENTITIES: CustomEntitiesApi,
        TagValues.CUSTOM_ENTITY_DEFINITIONS: CustomEntityDefinitionsApi,
        TagValues.CUT_LABEL_DEFINITIONS: CutLabelDefinitionsApi,
        TagValues.DATA_TYPES: DataTypesApi,
        TagValues.DERIVED_TRANSACTION_PORTFOLIOS: DerivedTransactionPortfoliosApi,
        TagValues.ENTITIES: EntitiesApi,
        TagValues.EXECUTIONS: ExecutionsApi,
        TagValues.FEES_AND_COMMISSIONS: FeesAndCommissionsApi,
        TagValues.INSTRUMENTS: InstrumentsApi,
        TagValues.LEGAL_ENTITIES: LegalEntitiesApi,
        TagValues.ORDER_GRAPH: OrderGraphApi,
        TagValues.ORDER_INSTRUCTIONS: OrderInstructionsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.PACKAGES: PackagesApi,
        TagValues.PARTICIPATIONS: ParticipationsApi,
        TagValues.PERSONS: PersonsApi,
        TagValues.PLACEMENTS: PlacementsApi,
        TagValues.PORTFOLIO_GROUPS: PortfolioGroupsApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.PROPERTY_DEFINITIONS: PropertyDefinitionsApi,
        TagValues.QUOTES: QuotesApi,
        TagValues.RECONCILIATIONS: ReconciliationsApi,
        TagValues.REFERENCE_PORTFOLIO: ReferencePortfolioApi,
        TagValues.RELATION_DEFINITIONS: RelationDefinitionsApi,
        TagValues.RELATIONS: RelationsApi,
        TagValues.RELATIONSHIP_DEFINITIONS: RelationshipDefinitionsApi,
        TagValues.RELATIONSHIPS: RelationshipsApi,
        TagValues.SCHEMAS: SchemasApi,
        TagValues.SCOPES: ScopesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SEQUENCES: SequencesApi,
        TagValues.STRUCTURED_RESULT_DATA: StructuredResultDataApi,
        TagValues.SYSTEM_CONFIGURATION: SystemConfigurationApi,
        TagValues.TRANSACTION_PORTFOLIOS: TransactionPortfoliosApi,
        TagValues.TRANSLATION: TranslationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AGGREGATION: AggregationApi,
        TagValues.ALLOCATIONS: AllocationsApi,
        TagValues.APPLICATION_METADATA: ApplicationMetadataApi,
        TagValues.BLOCKS: BlocksApi,
        TagValues.CALENDARS: CalendarsApi,
        TagValues.COMPLEX_MARKET_DATA: ComplexMarketDataApi,
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.CONFIGURATION_RECIPE: ConfigurationRecipeApi,
        TagValues.CONVENTIONS: ConventionsApi,
        TagValues.CORPORATE_ACTION_SOURCES: CorporateActionSourcesApi,
        TagValues.COUNTERPARTIES: CounterpartiesApi,
        TagValues.CUSTOM_ENTITIES: CustomEntitiesApi,
        TagValues.CUSTOM_ENTITY_DEFINITIONS: CustomEntityDefinitionsApi,
        TagValues.CUT_LABEL_DEFINITIONS: CutLabelDefinitionsApi,
        TagValues.DATA_TYPES: DataTypesApi,
        TagValues.DERIVED_TRANSACTION_PORTFOLIOS: DerivedTransactionPortfoliosApi,
        TagValues.ENTITIES: EntitiesApi,
        TagValues.EXECUTIONS: ExecutionsApi,
        TagValues.FEES_AND_COMMISSIONS: FeesAndCommissionsApi,
        TagValues.INSTRUMENTS: InstrumentsApi,
        TagValues.LEGAL_ENTITIES: LegalEntitiesApi,
        TagValues.ORDER_GRAPH: OrderGraphApi,
        TagValues.ORDER_INSTRUCTIONS: OrderInstructionsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.PACKAGES: PackagesApi,
        TagValues.PARTICIPATIONS: ParticipationsApi,
        TagValues.PERSONS: PersonsApi,
        TagValues.PLACEMENTS: PlacementsApi,
        TagValues.PORTFOLIO_GROUPS: PortfolioGroupsApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.PROPERTY_DEFINITIONS: PropertyDefinitionsApi,
        TagValues.QUOTES: QuotesApi,
        TagValues.RECONCILIATIONS: ReconciliationsApi,
        TagValues.REFERENCE_PORTFOLIO: ReferencePortfolioApi,
        TagValues.RELATION_DEFINITIONS: RelationDefinitionsApi,
        TagValues.RELATIONS: RelationsApi,
        TagValues.RELATIONSHIP_DEFINITIONS: RelationshipDefinitionsApi,
        TagValues.RELATIONSHIPS: RelationshipsApi,
        TagValues.SCHEMAS: SchemasApi,
        TagValues.SCOPES: ScopesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SEQUENCES: SequencesApi,
        TagValues.STRUCTURED_RESULT_DATA: StructuredResultDataApi,
        TagValues.SYSTEM_CONFIGURATION: SystemConfigurationApi,
        TagValues.TRANSACTION_PORTFOLIOS: TransactionPortfoliosApi,
        TagValues.TRANSLATION: TranslationApi,
    }
)
