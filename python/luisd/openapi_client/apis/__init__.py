# coding: utf-8

# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.aggregation_api import AggregationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.aggregation_api import AggregationApi
from openapi_client.api.allocations_api import AllocationsApi
from openapi_client.api.application_metadata_api import ApplicationMetadataApi
from openapi_client.api.blocks_api import BlocksApi
from openapi_client.api.calendars_api import CalendarsApi
from openapi_client.api.complex_market_data_api import ComplexMarketDataApi
from openapi_client.api.compliance_api import ComplianceApi
from openapi_client.api.configuration_recipe_api import ConfigurationRecipeApi
from openapi_client.api.conventions_api import ConventionsApi
from openapi_client.api.corporate_action_sources_api import CorporateActionSourcesApi
from openapi_client.api.counterparties_api import CounterpartiesApi
from openapi_client.api.custom_entities_api import CustomEntitiesApi
from openapi_client.api.custom_entity_definitions_api import CustomEntityDefinitionsApi
from openapi_client.api.cut_label_definitions_api import CutLabelDefinitionsApi
from openapi_client.api.data_types_api import DataTypesApi
from openapi_client.api.derived_transaction_portfolios_api import DerivedTransactionPortfoliosApi
from openapi_client.api.entities_api import EntitiesApi
from openapi_client.api.executions_api import ExecutionsApi
from openapi_client.api.fees_and_commissions_api import FeesAndCommissionsApi
from openapi_client.api.instruments_api import InstrumentsApi
from openapi_client.api.legal_entities_api import LegalEntitiesApi
from openapi_client.api.order_graph_api import OrderGraphApi
from openapi_client.api.order_instructions_api import OrderInstructionsApi
from openapi_client.api.orders_api import OrdersApi
from openapi_client.api.packages_api import PackagesApi
from openapi_client.api.participations_api import ParticipationsApi
from openapi_client.api.persons_api import PersonsApi
from openapi_client.api.placements_api import PlacementsApi
from openapi_client.api.portfolio_groups_api import PortfolioGroupsApi
from openapi_client.api.portfolios_api import PortfoliosApi
from openapi_client.api.property_definitions_api import PropertyDefinitionsApi
from openapi_client.api.quotes_api import QuotesApi
from openapi_client.api.reconciliations_api import ReconciliationsApi
from openapi_client.api.reference_portfolio_api import ReferencePortfolioApi
from openapi_client.api.relation_definitions_api import RelationDefinitionsApi
from openapi_client.api.relations_api import RelationsApi
from openapi_client.api.relationship_definitions_api import RelationshipDefinitionsApi
from openapi_client.api.relationships_api import RelationshipsApi
from openapi_client.api.schemas_api import SchemasApi
from openapi_client.api.scopes_api import ScopesApi
from openapi_client.api.search_api import SearchApi
from openapi_client.api.sequences_api import SequencesApi
from openapi_client.api.structured_result_data_api import StructuredResultDataApi
from openapi_client.api.system_configuration_api import SystemConfigurationApi
from openapi_client.api.transaction_portfolios_api import TransactionPortfoliosApi
from openapi_client.api.translation_api import TranslationApi
