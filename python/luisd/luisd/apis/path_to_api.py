import typing

from luisd.paths import PathValues
from luisd.apis.paths.api_aggregation_valuation import ApiAggregationValuation
from luisd.apis.paths.api_aggregation_valuationinlined import ApiAggregationValuationinlined
from luisd.apis.paths.api_aggregation_scope_code_generateconfigurationrecipe import ApiAggregationScopeCodeGenerateconfigurationrecipe
from luisd.apis.paths.api_allocations import ApiAllocations
from luisd.apis.paths.api_allocations_scope_code import ApiAllocationsScopeCode
from luisd.apis.paths.api_blocks import ApiBlocks
from luisd.apis.paths.api_blocks_scope_code import ApiBlocksScopeCode
from luisd.apis.paths.api_calendars_businessday_scope_add import ApiCalendarsBusinessdayScopeAdd
from luisd.apis.paths.api_calendars_businessday_scope_code import ApiCalendarsBusinessdayScopeCode
from luisd.apis.paths.api_calendars_generic import ApiCalendarsGeneric
from luisd.apis.paths.api_calendars_generic_scope import ApiCalendarsGenericScope
from luisd.apis.paths.api_calendars_generic_scope_code import ApiCalendarsGenericScopeCode
from luisd.apis.paths.api_calendars_generic_scope_code_dates import ApiCalendarsGenericScopeCodeDates
from luisd.apis.paths.api_calendars_generic_scope_code_dates_date_id import ApiCalendarsGenericScopeCodeDatesDateId
from luisd.apis.paths.api_calendars_schedule_scope import ApiCalendarsScheduleScope
from luisd.apis.paths.api_complexmarketdata import ApiComplexmarketdata
from luisd.apis.paths.api_complexmarketdata_scope import ApiComplexmarketdataScope
from luisd.apis.paths.api_complexmarketdata_scope_delete import ApiComplexmarketdataScopeDelete
from luisd.apis.paths.api_complexmarketdata_scope_get import ApiComplexmarketdataScopeGet
from luisd.apis.paths.api_compliance import ApiCompliance
from luisd.apis.paths.api_compliance_run import ApiComplianceRun
from luisd.apis.paths.api_compliance_run_id import ApiComplianceRunId
from luisd.apis.paths.api_conventions_credit_conventions import ApiConventionsCreditConventions
from luisd.apis.paths.api_conventions_credit_conventions_scope_code import ApiConventionsCreditConventionsScopeCode
from luisd.apis.paths.api_conventions_rates_flowconventions import ApiConventionsRatesFlowconventions
from luisd.apis.paths.api_conventions_rates_flowconventions_scope_code import ApiConventionsRatesFlowconventionsScopeCode
from luisd.apis.paths.api_conventions_rates_indexconventions import ApiConventionsRatesIndexconventions
from luisd.apis.paths.api_conventions_rates_indexconventions_scope_code import ApiConventionsRatesIndexconventionsScopeCode
from luisd.apis.paths.api_corporateactionsources import ApiCorporateactionsources
from luisd.apis.paths.api_corporateactionsources_scope_code import ApiCorporateactionsourcesScopeCode
from luisd.apis.paths.api_corporateactionsources_scope_code_corporateactions import ApiCorporateactionsourcesScopeCodeCorporateactions
from luisd.apis.paths.api_counterparties_counterpartyagreements import ApiCounterpartiesCounterpartyagreements
from luisd.apis.paths.api_counterparties_counterpartyagreements_scope_code import ApiCounterpartiesCounterpartyagreementsScopeCode
from luisd.apis.paths.api_counterparties_creditsupportannexes import ApiCounterpartiesCreditsupportannexes
from luisd.apis.paths.api_counterparties_creditsupportannexes_scope_code import ApiCounterpartiesCreditsupportannexesScopeCode
from luisd.apis.paths.api_customentities_entitytypes import ApiCustomentitiesEntitytypes
from luisd.apis.paths.api_customentities_entitytypes_entity_type import ApiCustomentitiesEntitytypesEntityType
from luisd.apis.paths.api_customentities_entity_type import ApiCustomentitiesEntityType
from luisd.apis.paths.api_customentities_entity_type_identifier_type_identifier_value import ApiCustomentitiesEntityTypeIdentifierTypeIdentifierValue
from luisd.apis.paths.api_customentities_entity_type_identifier_type_identifier_value_relationships import ApiCustomentitiesEntityTypeIdentifierTypeIdentifierValueRelationships
from luisd.apis.paths.api_datatypes import ApiDatatypes
from luisd.apis.paths.api_datatypes_scope import ApiDatatypesScope
from luisd.apis.paths.api_datatypes_scope_code import ApiDatatypesScopeCode
from luisd.apis.paths.api_datatypes_scope_code_referencedatavalues import ApiDatatypesScopeCodeReferencedatavalues
from luisd.apis.paths.api_datatypes_scope_code_units import ApiDatatypesScopeCodeUnits
from luisd.apis.paths.api_derivedtransactionportfolios_scope import ApiDerivedtransactionportfoliosScope
from luisd.apis.paths.api_derivedtransactionportfolios_scope_code_details import ApiDerivedtransactionportfoliosScopeCodeDetails
from luisd.apis.paths.api_entities_changes_portfolios import ApiEntitiesChangesPortfolios
from luisd.apis.paths.api_executions import ApiExecutions
from luisd.apis.paths.api_executions_scope_code import ApiExecutionsScopeCode
from luisd.apis.paths.api_feesandcommissions import ApiFeesandcommissions
from luisd.apis.paths.api_feesandcommissions_rules import ApiFeesandcommissionsRules
from luisd.apis.paths.api_instruments import ApiInstruments
from luisd.apis.paths.api_instruments_get import ApiInstrumentsGet
from luisd.apis.paths.api_instruments_upsertproperties import ApiInstrumentsUpsertproperties
from luisd.apis.paths.api_instruments_identifier_types import ApiInstrumentsIdentifierTypes
from luisd.apis.paths.api_instruments_identifier_type_identifier import ApiInstrumentsIdentifierTypeIdentifier
from luisd.apis.paths.api_instruments_identifier_type_identifier_properties import ApiInstrumentsIdentifierTypeIdentifierProperties
from luisd.apis.paths.api_instruments_identifier_type_identifier_properties_delete import ApiInstrumentsIdentifierTypeIdentifierPropertiesDelete
from luisd.apis.paths.api_instruments_identifier_type_identifier_properties_list import ApiInstrumentsIdentifierTypeIdentifierPropertiesList
from luisd.apis.paths.api_instruments_identifier_type_identifier_properties_time_series import ApiInstrumentsIdentifierTypeIdentifierPropertiesTimeSeries
from luisd.apis.paths.api_legalentities import ApiLegalentities
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code import ApiLegalentitiesIdTypeScopeIdTypeCode
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code import ApiLegalentitiesIdTypeScopeIdTypeCodeCode
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_identifiers import ApiLegalentitiesIdTypeScopeIdTypeCodeCodeIdentifiers
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_metadata import ApiLegalentitiesIdTypeScopeIdTypeCodeCodeMetadata
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_metadata_metadata_key import ApiLegalentitiesIdTypeScopeIdTypeCodeCodeMetadataMetadataKey
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_properties import ApiLegalentitiesIdTypeScopeIdTypeCodeCodeProperties
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_properties_time_series import ApiLegalentitiesIdTypeScopeIdTypeCodeCodePropertiesTimeSeries
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_relations import ApiLegalentitiesIdTypeScopeIdTypeCodeCodeRelations
from luisd.apis.paths.api_legalentities_id_type_scope_id_type_code_code_relationships import ApiLegalentitiesIdTypeScopeIdTypeCodeCodeRelationships
from luisd.apis.paths.api_metadata_access_resources import ApiMetadataAccessResources
from luisd.apis.paths.api_metadata_downloads_exceladdin import ApiMetadataDownloadsExceladdin
from luisd.apis.paths.api_metadata_quotes_rules import ApiMetadataQuotesRules
from luisd.apis.paths.api_metadata_quotes_rules_scope import ApiMetadataQuotesRulesScope
from luisd.apis.paths.api_metadata_versions import ApiMetadataVersions
from luisd.apis.paths.api_ordergraph_blocks import ApiOrdergraphBlocks
from luisd.apis.paths.api_ordergraph_placements import ApiOrdergraphPlacements
from luisd.apis.paths.api_orderinstructions import ApiOrderinstructions
from luisd.apis.paths.api_orderinstructions_scope_code import ApiOrderinstructionsScopeCode
from luisd.apis.paths.api_orders import ApiOrders
from luisd.apis.paths.api_orders_scope_code import ApiOrdersScopeCode
from luisd.apis.paths.api_packages import ApiPackages
from luisd.apis.paths.api_packages_scope_code import ApiPackagesScopeCode
from luisd.apis.paths.api_participations import ApiParticipations
from luisd.apis.paths.api_participations_scope_code import ApiParticipationsScopeCode
from luisd.apis.paths.api_persons import ApiPersons
from luisd.apis.paths.api_persons_id_type_scope_id_type_code import ApiPersonsIdTypeScopeIdTypeCode
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code import ApiPersonsIdTypeScopeIdTypeCodeCode
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_identifiers import ApiPersonsIdTypeScopeIdTypeCodeCodeIdentifiers
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_metadata import ApiPersonsIdTypeScopeIdTypeCodeCodeMetadata
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_metadata_metadata_key import ApiPersonsIdTypeScopeIdTypeCodeCodeMetadataMetadataKey
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_properties import ApiPersonsIdTypeScopeIdTypeCodeCodeProperties
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_properties_time_series import ApiPersonsIdTypeScopeIdTypeCodeCodePropertiesTimeSeries
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_relations import ApiPersonsIdTypeScopeIdTypeCodeCodeRelations
from luisd.apis.paths.api_persons_id_type_scope_id_type_code_code_relationships import ApiPersonsIdTypeScopeIdTypeCodeCodeRelationships
from luisd.apis.paths.api_placements import ApiPlacements
from luisd.apis.paths.api_placements_scope_code import ApiPlacementsScopeCode
from luisd.apis.paths.api_portfoliogroups_scope import ApiPortfoliogroupsScope
from luisd.apis.paths.api_portfoliogroups_scope_code import ApiPortfoliogroupsScopeCode
from luisd.apis.paths.api_portfoliogroups_scope_code_a2b import ApiPortfoliogroupsScopeCodeA2b
from luisd.apis.paths.api_portfoliogroups_scope_code_commands import ApiPortfoliogroupsScopeCodeCommands
from luisd.apis.paths.api_portfoliogroups_scope_code_expansion import ApiPortfoliogroupsScopeCodeExpansion
from luisd.apis.paths.api_portfoliogroups_scope_code_holdings import ApiPortfoliogroupsScopeCodeHoldings
from luisd.apis.paths.api_portfoliogroups_scope_code_metadata import ApiPortfoliogroupsScopeCodeMetadata
from luisd.apis.paths.api_portfoliogroups_scope_code_metadata_metadata_key import ApiPortfoliogroupsScopeCodeMetadataMetadataKey
from luisd.apis.paths.api_portfoliogroups_scope_code_portfolios import ApiPortfoliogroupsScopeCodePortfolios
from luisd.apis.paths.api_portfoliogroups_scope_code_portfolios_portfolio_scope_portfolio_code import ApiPortfoliogroupsScopeCodePortfoliosPortfolioScopePortfolioCode
from luisd.apis.paths.api_portfoliogroups_scope_code_properties import ApiPortfoliogroupsScopeCodeProperties
from luisd.apis.paths.api_portfoliogroups_scope_code_properties_delete import ApiPortfoliogroupsScopeCodePropertiesDelete
from luisd.apis.paths.api_portfoliogroups_scope_code_properties_upsert import ApiPortfoliogroupsScopeCodePropertiesUpsert
from luisd.apis.paths.api_portfoliogroups_scope_code_properties_time_series import ApiPortfoliogroupsScopeCodePropertiesTimeSeries
from luisd.apis.paths.api_portfoliogroups_scope_code_relations import ApiPortfoliogroupsScopeCodeRelations
from luisd.apis.paths.api_portfoliogroups_scope_code_relationships import ApiPortfoliogroupsScopeCodeRelationships
from luisd.apis.paths.api_portfoliogroups_scope_code_subgroups import ApiPortfoliogroupsScopeCodeSubgroups
from luisd.apis.paths.api_portfoliogroups_scope_code_subgroups_subgroup_scope_subgroup_code import ApiPortfoliogroupsScopeCodeSubgroupsSubgroupScopeSubgroupCode
from luisd.apis.paths.api_portfoliogroups_scope_code_transactions import ApiPortfoliogroupsScopeCodeTransactions
from luisd.apis.paths.api_portfoliogroups_scope_code_transactions_build import ApiPortfoliogroupsScopeCodeTransactionsBuild
from luisd.apis.paths.api_portfolios import ApiPortfolios
from luisd.apis.paths.api_portfolios_reconcile_generic import ApiPortfoliosReconcileGeneric
from luisd.apis.paths.api_portfolios_reconcileholdings import ApiPortfoliosReconcileholdings
from luisd.apis.paths.api_portfolios_reconcile_inline import ApiPortfoliosReconcileInline
from luisd.apis.paths.api_portfolios_reconcile_valuation import ApiPortfoliosReconcileValuation
from luisd.apis.paths.api_portfolios_preview_reconcileholdings import ApiPortfoliosPreviewReconcileholdings
from luisd.apis.paths.api_portfolios_scope import ApiPortfoliosScope
from luisd.apis.paths.api_portfolios_scope_code import ApiPortfoliosScopeCode
from luisd.apis.paths.api_portfolios_scope_code_commands import ApiPortfoliosScopeCodeCommands
from luisd.apis.paths.api_portfolios_scope_code_metadata import ApiPortfoliosScopeCodeMetadata
from luisd.apis.paths.api_portfolios_scope_code_metadata_metadata_key import ApiPortfoliosScopeCodeMetadataMetadataKey
from luisd.apis.paths.api_portfolios_scope_code_properties import ApiPortfoliosScopeCodeProperties
from luisd.apis.paths.api_portfolios_scope_code_properties_list import ApiPortfoliosScopeCodePropertiesList
from luisd.apis.paths.api_portfolios_scope_code_properties_time_series import ApiPortfoliosScopeCodePropertiesTimeSeries
from luisd.apis.paths.api_portfolios_scope_code_relations import ApiPortfoliosScopeCodeRelations
from luisd.apis.paths.api_portfolios_scope_code_relationships import ApiPortfoliosScopeCodeRelationships
from luisd.apis.paths.api_portfolios_scope_code_returns_return_scope_return_code import ApiPortfoliosScopeCodeReturnsReturnScopeReturnCode
from luisd.apis.paths.api_portfolios_scope_code_returns_return_scope_return_code_aggregated import ApiPortfoliosScopeCodeReturnsReturnScopeReturnCodeAggregated
from luisd.apis.paths.api_portfolios_scope_code_returns_return_scope_return_code_delete import ApiPortfoliosScopeCodeReturnsReturnScopeReturnCodeDelete
from luisd.apis.paths.api_propertydefinitions import ApiPropertydefinitions
from luisd.apis.paths.api_propertydefinitions_derived import ApiPropertydefinitionsDerived
from luisd.apis.paths.api_propertydefinitions_domain_scope_code import ApiPropertydefinitionsDomainScopeCode
from luisd.apis.paths.api_quotes_scope import ApiQuotesScope
from luisd.apis.paths.api_quotes_scope_delete import ApiQuotesScopeDelete
from luisd.apis.paths.api_quotes_scope_deprecated import ApiQuotesScopeDeprecated
from luisd.apis.paths.api_quotes_scope_get import ApiQuotesScopeGet
from luisd.apis.paths.api_recipes import ApiRecipes
from luisd.apis.paths.api_recipes_scope_code import ApiRecipesScopeCode
from luisd.apis.paths.api_referenceportfolios_scope import ApiReferenceportfoliosScope
from luisd.apis.paths.api_referenceportfolios_scope_code_constituents import ApiReferenceportfoliosScopeCodeConstituents
from luisd.apis.paths.api_referenceportfolios_scope_code_constituentsadjustments import ApiReferenceportfoliosScopeCodeConstituentsadjustments
from luisd.apis.paths.api_relationdefinitions import ApiRelationdefinitions
from luisd.apis.paths.api_relationdefinitions_scope_code import ApiRelationdefinitionsScopeCode
from luisd.apis.paths.api_relations_scope_code import ApiRelationsScopeCode
from luisd.apis.paths.api_relations_scope_code_delete import ApiRelationsScopeCodeDelete
from luisd.apis.paths.api_relationshipdefinitions import ApiRelationshipdefinitions
from luisd.apis.paths.api_relationshipdefinitions_scope_code import ApiRelationshipdefinitionsScopeCode
from luisd.apis.paths.api_relationshipdefinitions_scope_code_relationships import ApiRelationshipdefinitionsScopeCodeRelationships
from luisd.apis.paths.api_relationshipdefinitions_scope_code_relationships_delete import ApiRelationshipdefinitionsScopeCodeRelationshipsDelete
from luisd.apis.paths.api_results_queryable_keys import ApiResultsQueryableKeys
from luisd.apis.paths.api_schemas_entities import ApiSchemasEntities
from luisd.apis.paths.api_schemas_entities_entity import ApiSchemasEntitiesEntity
from luisd.apis.paths.api_schemas_properties import ApiSchemasProperties
from luisd.apis.paths.api_schemas_types import ApiSchemasTypes
from luisd.apis.paths.api_scopes import ApiScopes
from luisd.apis.paths.api_search_instruments import ApiSearchInstruments
from luisd.apis.paths.api_search_portfoliogroups import ApiSearchPortfoliogroups
from luisd.apis.paths.api_search_portfolios import ApiSearchPortfolios
from luisd.apis.paths.api_search_propertydefinitions import ApiSearchPropertydefinitions
from luisd.apis.paths.api_sequences import ApiSequences
from luisd.apis.paths.api_sequences_scope import ApiSequencesScope
from luisd.apis.paths.api_sequences_scope_code import ApiSequencesScopeCode
from luisd.apis.paths.api_sequences_scope_code_next import ApiSequencesScopeCodeNext
from luisd.apis.paths.api_systemconfiguration_cutlabels import ApiSystemconfigurationCutlabels
from luisd.apis.paths.api_systemconfiguration_cutlabels_code import ApiSystemconfigurationCutlabelsCode
from luisd.apis.paths.api_systemconfiguration_transactions import ApiSystemconfigurationTransactions
from luisd.apis.paths.api_systemconfiguration_transactions_side import ApiSystemconfigurationTransactionsSide
from luisd.apis.paths.api_systemconfiguration_transactions_type import ApiSystemconfigurationTransactionsType
from luisd.apis.paths.api_systemconfiguration_transactions_type_source import ApiSystemconfigurationTransactionsTypeSource
from luisd.apis.paths.api_transactionportfolios_scope import ApiTransactionportfoliosScope
from luisd.apis.paths.api_transactionportfolios_scope_code_resolve import ApiTransactionportfoliosScopeCodeResolve
from luisd.apis.paths.api_transactionportfolios_scope_code_a2b import ApiTransactionportfoliosScopeCodeA2b
from luisd.apis.paths.api_transactionportfolios_scope_code_a2bmovements import ApiTransactionportfoliosScopeCodeA2bmovements
from luisd.apis.paths.api_transactionportfolios_scope_code_bucketed_cash_flows import ApiTransactionportfoliosScopeCodeBucketedCashFlows
from luisd.apis.paths.api_transactionportfolios_scope_code_cashflows import ApiTransactionportfoliosScopeCodeCashflows
from luisd.apis.paths.api_transactionportfolios_scope_code_cashladder import ApiTransactionportfoliosScopeCodeCashladder
from luisd.apis.paths.api_transactionportfolios_scope_code_cashstatement import ApiTransactionportfoliosScopeCodeCashstatement
from luisd.apis.paths.api_transactionportfolios_scope_code_details import ApiTransactionportfoliosScopeCodeDetails
from luisd.apis.paths.api_transactionportfolios_scope_code_holdings import ApiTransactionportfoliosScopeCodeHoldings
from luisd.apis.paths.api_transactionportfolios_scope_code_holdingsadjustments import ApiTransactionportfoliosScopeCodeHoldingsadjustments
from luisd.apis.paths.api_transactionportfolios_scope_code_holdingsadjustments_effective_at import ApiTransactionportfoliosScopeCodeHoldingsadjustmentsEffectiveAt
from luisd.apis.paths.api_transactionportfolios_scope_code_holdings_with_orders import ApiTransactionportfoliosScopeCodeHoldingsWithOrders
from luisd.apis.paths.api_transactionportfolios_scope_code_transactions import ApiTransactionportfoliosScopeCodeTransactions
from luisd.apis.paths.api_transactionportfolios_scope_code_transactions_build import ApiTransactionportfoliosScopeCodeTransactionsBuild
from luisd.apis.paths.api_transactionportfolios_scope_code_transactions_transaction_id_properties import ApiTransactionportfoliosScopeCodeTransactionsTransactionIdProperties
from luisd.apis.paths.api_transactionportfolios_scope_code_upsertablecashflows import ApiTransactionportfoliosScopeCodeUpsertablecashflows
from luisd.apis.paths.api_translation_instrumentdefinitions import ApiTranslationInstrumentdefinitions
from luisd.apis.paths.api_unitresults_datamap_scope import ApiUnitresultsDatamapScope
from luisd.apis.paths.api_unitresults_datamap_scope_get import ApiUnitresultsDatamapScopeGet
from luisd.apis.paths.api_unitresults_virtualdocument_scope_get import ApiUnitresultsVirtualdocumentScopeGet
from luisd.apis.paths.api_unitresults_scope import ApiUnitresultsScope
from luisd.apis.paths.api_unitresults_scope_delete import ApiUnitresultsScopeDelete
from luisd.apis.paths.api_unitresults_scope_get import ApiUnitresultsScopeGet

PathToApi = typing.TypedDict(
    'PathToApi',
    {
        PathValues.API_AGGREGATION_VALUATION: ApiAggregationValuation,
        PathValues.API_AGGREGATION_VALUATIONINLINED: ApiAggregationValuationinlined,
        PathValues.API_AGGREGATION_SCOPE_CODE_GENERATECONFIGURATIONRECIPE: ApiAggregationScopeCodeGenerateconfigurationrecipe,
        PathValues.API_ALLOCATIONS: ApiAllocations,
        PathValues.API_ALLOCATIONS_SCOPE_CODE: ApiAllocationsScopeCode,
        PathValues.API_BLOCKS: ApiBlocks,
        PathValues.API_BLOCKS_SCOPE_CODE: ApiBlocksScopeCode,
        PathValues.API_CALENDARS_BUSINESSDAY_SCOPE_ADD: ApiCalendarsBusinessdayScopeAdd,
        PathValues.API_CALENDARS_BUSINESSDAY_SCOPE_CODE: ApiCalendarsBusinessdayScopeCode,
        PathValues.API_CALENDARS_GENERIC: ApiCalendarsGeneric,
        PathValues.API_CALENDARS_GENERIC_SCOPE: ApiCalendarsGenericScope,
        PathValues.API_CALENDARS_GENERIC_SCOPE_CODE: ApiCalendarsGenericScopeCode,
        PathValues.API_CALENDARS_GENERIC_SCOPE_CODE_DATES: ApiCalendarsGenericScopeCodeDates,
        PathValues.API_CALENDARS_GENERIC_SCOPE_CODE_DATES_DATE_ID: ApiCalendarsGenericScopeCodeDatesDateId,
        PathValues.API_CALENDARS_SCHEDULE_SCOPE: ApiCalendarsScheduleScope,
        PathValues.API_COMPLEXMARKETDATA: ApiComplexmarketdata,
        PathValues.API_COMPLEXMARKETDATA_SCOPE: ApiComplexmarketdataScope,
        PathValues.API_COMPLEXMARKETDATA_SCOPE_DELETE: ApiComplexmarketdataScopeDelete,
        PathValues.API_COMPLEXMARKETDATA_SCOPE_GET: ApiComplexmarketdataScopeGet,
        PathValues.API_COMPLIANCE: ApiCompliance,
        PathValues.API_COMPLIANCE_RUN: ApiComplianceRun,
        PathValues.API_COMPLIANCE_RUN_ID: ApiComplianceRunId,
        PathValues.API_CONVENTIONS_CREDIT_CONVENTIONS: ApiConventionsCreditConventions,
        PathValues.API_CONVENTIONS_CREDIT_CONVENTIONS_SCOPE_CODE: ApiConventionsCreditConventionsScopeCode,
        PathValues.API_CONVENTIONS_RATES_FLOWCONVENTIONS: ApiConventionsRatesFlowconventions,
        PathValues.API_CONVENTIONS_RATES_FLOWCONVENTIONS_SCOPE_CODE: ApiConventionsRatesFlowconventionsScopeCode,
        PathValues.API_CONVENTIONS_RATES_INDEXCONVENTIONS: ApiConventionsRatesIndexconventions,
        PathValues.API_CONVENTIONS_RATES_INDEXCONVENTIONS_SCOPE_CODE: ApiConventionsRatesIndexconventionsScopeCode,
        PathValues.API_CORPORATEACTIONSOURCES: ApiCorporateactionsources,
        PathValues.API_CORPORATEACTIONSOURCES_SCOPE_CODE: ApiCorporateactionsourcesScopeCode,
        PathValues.API_CORPORATEACTIONSOURCES_SCOPE_CODE_CORPORATEACTIONS: ApiCorporateactionsourcesScopeCodeCorporateactions,
        PathValues.API_COUNTERPARTIES_COUNTERPARTYAGREEMENTS: ApiCounterpartiesCounterpartyagreements,
        PathValues.API_COUNTERPARTIES_COUNTERPARTYAGREEMENTS_SCOPE_CODE: ApiCounterpartiesCounterpartyagreementsScopeCode,
        PathValues.API_COUNTERPARTIES_CREDITSUPPORTANNEXES: ApiCounterpartiesCreditsupportannexes,
        PathValues.API_COUNTERPARTIES_CREDITSUPPORTANNEXES_SCOPE_CODE: ApiCounterpartiesCreditsupportannexesScopeCode,
        PathValues.API_CUSTOMENTITIES_ENTITYTYPES: ApiCustomentitiesEntitytypes,
        PathValues.API_CUSTOMENTITIES_ENTITYTYPES_ENTITY_TYPE: ApiCustomentitiesEntitytypesEntityType,
        PathValues.API_CUSTOMENTITIES_ENTITY_TYPE: ApiCustomentitiesEntityType,
        PathValues.API_CUSTOMENTITIES_ENTITY_TYPE_IDENTIFIER_TYPE_IDENTIFIER_VALUE: ApiCustomentitiesEntityTypeIdentifierTypeIdentifierValue,
        PathValues.API_CUSTOMENTITIES_ENTITY_TYPE_IDENTIFIER_TYPE_IDENTIFIER_VALUE_RELATIONSHIPS: ApiCustomentitiesEntityTypeIdentifierTypeIdentifierValueRelationships,
        PathValues.API_DATATYPES: ApiDatatypes,
        PathValues.API_DATATYPES_SCOPE: ApiDatatypesScope,
        PathValues.API_DATATYPES_SCOPE_CODE: ApiDatatypesScopeCode,
        PathValues.API_DATATYPES_SCOPE_CODE_REFERENCEDATAVALUES: ApiDatatypesScopeCodeReferencedatavalues,
        PathValues.API_DATATYPES_SCOPE_CODE_UNITS: ApiDatatypesScopeCodeUnits,
        PathValues.API_DERIVEDTRANSACTIONPORTFOLIOS_SCOPE: ApiDerivedtransactionportfoliosScope,
        PathValues.API_DERIVEDTRANSACTIONPORTFOLIOS_SCOPE_CODE_DETAILS: ApiDerivedtransactionportfoliosScopeCodeDetails,
        PathValues.API_ENTITIES_CHANGES_PORTFOLIOS: ApiEntitiesChangesPortfolios,
        PathValues.API_EXECUTIONS: ApiExecutions,
        PathValues.API_EXECUTIONS_SCOPE_CODE: ApiExecutionsScopeCode,
        PathValues.API_FEESANDCOMMISSIONS: ApiFeesandcommissions,
        PathValues.API_FEESANDCOMMISSIONS_RULES: ApiFeesandcommissionsRules,
        PathValues.API_INSTRUMENTS: ApiInstruments,
        PathValues.API_INSTRUMENTS_GET: ApiInstrumentsGet,
        PathValues.API_INSTRUMENTS_UPSERTPROPERTIES: ApiInstrumentsUpsertproperties,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPES: ApiInstrumentsIdentifierTypes,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER: ApiInstrumentsIdentifierTypeIdentifier,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES: ApiInstrumentsIdentifierTypeIdentifierProperties,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES_DELETE: ApiInstrumentsIdentifierTypeIdentifierPropertiesDelete,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES_LIST: ApiInstrumentsIdentifierTypeIdentifierPropertiesList,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES_TIMESERIES: ApiInstrumentsIdentifierTypeIdentifierPropertiesTimeSeries,
        PathValues.API_LEGALENTITIES: ApiLegalentities,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE: ApiLegalentitiesIdTypeScopeIdTypeCode,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE: ApiLegalentitiesIdTypeScopeIdTypeCodeCode,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_IDENTIFIERS: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeIdentifiers,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeMetadata,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA_METADATA_KEY: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeMetadataMetadataKey,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeProperties,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES_TIMESERIES: ApiLegalentitiesIdTypeScopeIdTypeCodeCodePropertiesTimeSeries,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONS: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeRelations,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONSHIPS: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeRelationships,
        PathValues.API_METADATA_ACCESS_RESOURCES: ApiMetadataAccessResources,
        PathValues.API_METADATA_DOWNLOADS_EXCELADDIN: ApiMetadataDownloadsExceladdin,
        PathValues.API_METADATA_QUOTES_RULES: ApiMetadataQuotesRules,
        PathValues.API_METADATA_QUOTES_RULES_SCOPE: ApiMetadataQuotesRulesScope,
        PathValues.API_METADATA_VERSIONS: ApiMetadataVersions,
        PathValues.API_ORDERGRAPH_BLOCKS: ApiOrdergraphBlocks,
        PathValues.API_ORDERGRAPH_PLACEMENTS: ApiOrdergraphPlacements,
        PathValues.API_ORDERINSTRUCTIONS: ApiOrderinstructions,
        PathValues.API_ORDERINSTRUCTIONS_SCOPE_CODE: ApiOrderinstructionsScopeCode,
        PathValues.API_ORDERS: ApiOrders,
        PathValues.API_ORDERS_SCOPE_CODE: ApiOrdersScopeCode,
        PathValues.API_PACKAGES: ApiPackages,
        PathValues.API_PACKAGES_SCOPE_CODE: ApiPackagesScopeCode,
        PathValues.API_PARTICIPATIONS: ApiParticipations,
        PathValues.API_PARTICIPATIONS_SCOPE_CODE: ApiParticipationsScopeCode,
        PathValues.API_PERSONS: ApiPersons,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE: ApiPersonsIdTypeScopeIdTypeCode,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE: ApiPersonsIdTypeScopeIdTypeCodeCode,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_IDENTIFIERS: ApiPersonsIdTypeScopeIdTypeCodeCodeIdentifiers,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA: ApiPersonsIdTypeScopeIdTypeCodeCodeMetadata,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA_METADATA_KEY: ApiPersonsIdTypeScopeIdTypeCodeCodeMetadataMetadataKey,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES: ApiPersonsIdTypeScopeIdTypeCodeCodeProperties,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES_TIMESERIES: ApiPersonsIdTypeScopeIdTypeCodeCodePropertiesTimeSeries,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONS: ApiPersonsIdTypeScopeIdTypeCodeCodeRelations,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONSHIPS: ApiPersonsIdTypeScopeIdTypeCodeCodeRelationships,
        PathValues.API_PLACEMENTS: ApiPlacements,
        PathValues.API_PLACEMENTS_SCOPE_CODE: ApiPlacementsScopeCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE: ApiPortfoliogroupsScope,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE: ApiPortfoliogroupsScopeCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_A2B: ApiPortfoliogroupsScopeCodeA2b,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_COMMANDS: ApiPortfoliogroupsScopeCodeCommands,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_EXPANSION: ApiPortfoliogroupsScopeCodeExpansion,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_HOLDINGS: ApiPortfoliogroupsScopeCodeHoldings,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_METADATA: ApiPortfoliogroupsScopeCodeMetadata,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_METADATA_METADATA_KEY: ApiPortfoliogroupsScopeCodeMetadataMetadataKey,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PORTFOLIOS: ApiPortfoliogroupsScopeCodePortfolios,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PORTFOLIOS_PORTFOLIO_SCOPE_PORTFOLIO_CODE: ApiPortfoliogroupsScopeCodePortfoliosPortfolioScopePortfolioCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES: ApiPortfoliogroupsScopeCodeProperties,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES_DELETE: ApiPortfoliogroupsScopeCodePropertiesDelete,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES_UPSERT: ApiPortfoliogroupsScopeCodePropertiesUpsert,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES_TIMESERIES: ApiPortfoliogroupsScopeCodePropertiesTimeSeries,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_RELATIONS: ApiPortfoliogroupsScopeCodeRelations,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_RELATIONSHIPS: ApiPortfoliogroupsScopeCodeRelationships,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_SUBGROUPS: ApiPortfoliogroupsScopeCodeSubgroups,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_SUBGROUPS_SUBGROUP_SCOPE_SUBGROUP_CODE: ApiPortfoliogroupsScopeCodeSubgroupsSubgroupScopeSubgroupCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_TRANSACTIONS: ApiPortfoliogroupsScopeCodeTransactions,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_TRANSACTIONS_BUILD: ApiPortfoliogroupsScopeCodeTransactionsBuild,
        PathValues.API_PORTFOLIOS: ApiPortfolios,
        PathValues.API_PORTFOLIOS_RECONCILE_GENERIC: ApiPortfoliosReconcileGeneric,
        PathValues.API_PORTFOLIOS_RECONCILEHOLDINGS: ApiPortfoliosReconcileholdings,
        PathValues.API_PORTFOLIOS_RECONCILE_INLINE: ApiPortfoliosReconcileInline,
        PathValues.API_PORTFOLIOS_RECONCILE_VALUATION: ApiPortfoliosReconcileValuation,
        PathValues.API_PORTFOLIOS_PREVIEW_RECONCILEHOLDINGS: ApiPortfoliosPreviewReconcileholdings,
        PathValues.API_PORTFOLIOS_SCOPE: ApiPortfoliosScope,
        PathValues.API_PORTFOLIOS_SCOPE_CODE: ApiPortfoliosScopeCode,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_COMMANDS: ApiPortfoliosScopeCodeCommands,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_METADATA: ApiPortfoliosScopeCodeMetadata,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_METADATA_METADATA_KEY: ApiPortfoliosScopeCodeMetadataMetadataKey,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_PROPERTIES: ApiPortfoliosScopeCodeProperties,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_PROPERTIES_LIST: ApiPortfoliosScopeCodePropertiesList,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_PROPERTIES_TIMESERIES: ApiPortfoliosScopeCodePropertiesTimeSeries,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RELATIONS: ApiPortfoliosScopeCodeRelations,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RELATIONSHIPS: ApiPortfoliosScopeCodeRelationships,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RETURNS_RETURN_SCOPE_RETURN_CODE: ApiPortfoliosScopeCodeReturnsReturnScopeReturnCode,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RETURNS_RETURN_SCOPE_RETURN_CODE_AGGREGATED: ApiPortfoliosScopeCodeReturnsReturnScopeReturnCodeAggregated,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RETURNS_RETURN_SCOPE_RETURN_CODE_DELETE: ApiPortfoliosScopeCodeReturnsReturnScopeReturnCodeDelete,
        PathValues.API_PROPERTYDEFINITIONS: ApiPropertydefinitions,
        PathValues.API_PROPERTYDEFINITIONS_DERIVED: ApiPropertydefinitionsDerived,
        PathValues.API_PROPERTYDEFINITIONS_DOMAIN_SCOPE_CODE: ApiPropertydefinitionsDomainScopeCode,
        PathValues.API_QUOTES_SCOPE: ApiQuotesScope,
        PathValues.API_QUOTES_SCOPE_DELETE: ApiQuotesScopeDelete,
        PathValues.API_QUOTES_SCOPE_DEPRECATED: ApiQuotesScopeDeprecated,
        PathValues.API_QUOTES_SCOPE_GET: ApiQuotesScopeGet,
        PathValues.API_RECIPES: ApiRecipes,
        PathValues.API_RECIPES_SCOPE_CODE: ApiRecipesScopeCode,
        PathValues.API_REFERENCEPORTFOLIOS_SCOPE: ApiReferenceportfoliosScope,
        PathValues.API_REFERENCEPORTFOLIOS_SCOPE_CODE_CONSTITUENTS: ApiReferenceportfoliosScopeCodeConstituents,
        PathValues.API_REFERENCEPORTFOLIOS_SCOPE_CODE_CONSTITUENTSADJUSTMENTS: ApiReferenceportfoliosScopeCodeConstituentsadjustments,
        PathValues.API_RELATIONDEFINITIONS: ApiRelationdefinitions,
        PathValues.API_RELATIONDEFINITIONS_SCOPE_CODE: ApiRelationdefinitionsScopeCode,
        PathValues.API_RELATIONS_SCOPE_CODE: ApiRelationsScopeCode,
        PathValues.API_RELATIONS_SCOPE_CODE_DELETE: ApiRelationsScopeCodeDelete,
        PathValues.API_RELATIONSHIPDEFINITIONS: ApiRelationshipdefinitions,
        PathValues.API_RELATIONSHIPDEFINITIONS_SCOPE_CODE: ApiRelationshipdefinitionsScopeCode,
        PathValues.API_RELATIONSHIPDEFINITIONS_SCOPE_CODE_RELATIONSHIPS: ApiRelationshipdefinitionsScopeCodeRelationships,
        PathValues.API_RELATIONSHIPDEFINITIONS_SCOPE_CODE_RELATIONSHIPS_DELETE: ApiRelationshipdefinitionsScopeCodeRelationshipsDelete,
        PathValues.API_RESULTS_QUERYABLE_KEYS: ApiResultsQueryableKeys,
        PathValues.API_SCHEMAS_ENTITIES: ApiSchemasEntities,
        PathValues.API_SCHEMAS_ENTITIES_ENTITY: ApiSchemasEntitiesEntity,
        PathValues.API_SCHEMAS_PROPERTIES: ApiSchemasProperties,
        PathValues.API_SCHEMAS_TYPES: ApiSchemasTypes,
        PathValues.API_SCOPES: ApiScopes,
        PathValues.API_SEARCH_INSTRUMENTS: ApiSearchInstruments,
        PathValues.API_SEARCH_PORTFOLIOGROUPS: ApiSearchPortfoliogroups,
        PathValues.API_SEARCH_PORTFOLIOS: ApiSearchPortfolios,
        PathValues.API_SEARCH_PROPERTYDEFINITIONS: ApiSearchPropertydefinitions,
        PathValues.API_SEQUENCES: ApiSequences,
        PathValues.API_SEQUENCES_SCOPE: ApiSequencesScope,
        PathValues.API_SEQUENCES_SCOPE_CODE: ApiSequencesScopeCode,
        PathValues.API_SEQUENCES_SCOPE_CODE_NEXT: ApiSequencesScopeCodeNext,
        PathValues.API_SYSTEMCONFIGURATION_CUTLABELS: ApiSystemconfigurationCutlabels,
        PathValues.API_SYSTEMCONFIGURATION_CUTLABELS_CODE: ApiSystemconfigurationCutlabelsCode,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS: ApiSystemconfigurationTransactions,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS_SIDE: ApiSystemconfigurationTransactionsSide,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS_TYPE: ApiSystemconfigurationTransactionsType,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS_TYPE_SOURCE: ApiSystemconfigurationTransactionsTypeSource,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE: ApiTransactionportfoliosScope,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_RESOLVE: ApiTransactionportfoliosScopeCodeResolve,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_A2B: ApiTransactionportfoliosScopeCodeA2b,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_A2BMOVEMENTS: ApiTransactionportfoliosScopeCodeA2bmovements,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_BUCKETED_CASH_FLOWS: ApiTransactionportfoliosScopeCodeBucketedCashFlows,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_CASHFLOWS: ApiTransactionportfoliosScopeCodeCashflows,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_CASHLADDER: ApiTransactionportfoliosScopeCodeCashladder,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_CASHSTATEMENT: ApiTransactionportfoliosScopeCodeCashstatement,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_DETAILS: ApiTransactionportfoliosScopeCodeDetails,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGS: ApiTransactionportfoliosScopeCodeHoldings,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGSADJUSTMENTS: ApiTransactionportfoliosScopeCodeHoldingsadjustments,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGSADJUSTMENTS_EFFECTIVE_AT: ApiTransactionportfoliosScopeCodeHoldingsadjustmentsEffectiveAt,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGS_WITH_ORDERS: ApiTransactionportfoliosScopeCodeHoldingsWithOrders,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_TRANSACTIONS: ApiTransactionportfoliosScopeCodeTransactions,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_TRANSACTIONS_BUILD: ApiTransactionportfoliosScopeCodeTransactionsBuild,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_TRANSACTIONS_TRANSACTION_ID_PROPERTIES: ApiTransactionportfoliosScopeCodeTransactionsTransactionIdProperties,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_UPSERTABLECASHFLOWS: ApiTransactionportfoliosScopeCodeUpsertablecashflows,
        PathValues.API_TRANSLATION_INSTRUMENTDEFINITIONS: ApiTranslationInstrumentdefinitions,
        PathValues.API_UNITRESULTS_DATAMAP_SCOPE: ApiUnitresultsDatamapScope,
        PathValues.API_UNITRESULTS_DATAMAP_SCOPE_GET: ApiUnitresultsDatamapScopeGet,
        PathValues.API_UNITRESULTS_VIRTUALDOCUMENT_SCOPE_GET: ApiUnitresultsVirtualdocumentScopeGet,
        PathValues.API_UNITRESULTS_SCOPE: ApiUnitresultsScope,
        PathValues.API_UNITRESULTS_SCOPE_DELETE: ApiUnitresultsScopeDelete,
        PathValues.API_UNITRESULTS_SCOPE_GET: ApiUnitresultsScopeGet,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_AGGREGATION_VALUATION: ApiAggregationValuation,
        PathValues.API_AGGREGATION_VALUATIONINLINED: ApiAggregationValuationinlined,
        PathValues.API_AGGREGATION_SCOPE_CODE_GENERATECONFIGURATIONRECIPE: ApiAggregationScopeCodeGenerateconfigurationrecipe,
        PathValues.API_ALLOCATIONS: ApiAllocations,
        PathValues.API_ALLOCATIONS_SCOPE_CODE: ApiAllocationsScopeCode,
        PathValues.API_BLOCKS: ApiBlocks,
        PathValues.API_BLOCKS_SCOPE_CODE: ApiBlocksScopeCode,
        PathValues.API_CALENDARS_BUSINESSDAY_SCOPE_ADD: ApiCalendarsBusinessdayScopeAdd,
        PathValues.API_CALENDARS_BUSINESSDAY_SCOPE_CODE: ApiCalendarsBusinessdayScopeCode,
        PathValues.API_CALENDARS_GENERIC: ApiCalendarsGeneric,
        PathValues.API_CALENDARS_GENERIC_SCOPE: ApiCalendarsGenericScope,
        PathValues.API_CALENDARS_GENERIC_SCOPE_CODE: ApiCalendarsGenericScopeCode,
        PathValues.API_CALENDARS_GENERIC_SCOPE_CODE_DATES: ApiCalendarsGenericScopeCodeDates,
        PathValues.API_CALENDARS_GENERIC_SCOPE_CODE_DATES_DATE_ID: ApiCalendarsGenericScopeCodeDatesDateId,
        PathValues.API_CALENDARS_SCHEDULE_SCOPE: ApiCalendarsScheduleScope,
        PathValues.API_COMPLEXMARKETDATA: ApiComplexmarketdata,
        PathValues.API_COMPLEXMARKETDATA_SCOPE: ApiComplexmarketdataScope,
        PathValues.API_COMPLEXMARKETDATA_SCOPE_DELETE: ApiComplexmarketdataScopeDelete,
        PathValues.API_COMPLEXMARKETDATA_SCOPE_GET: ApiComplexmarketdataScopeGet,
        PathValues.API_COMPLIANCE: ApiCompliance,
        PathValues.API_COMPLIANCE_RUN: ApiComplianceRun,
        PathValues.API_COMPLIANCE_RUN_ID: ApiComplianceRunId,
        PathValues.API_CONVENTIONS_CREDIT_CONVENTIONS: ApiConventionsCreditConventions,
        PathValues.API_CONVENTIONS_CREDIT_CONVENTIONS_SCOPE_CODE: ApiConventionsCreditConventionsScopeCode,
        PathValues.API_CONVENTIONS_RATES_FLOWCONVENTIONS: ApiConventionsRatesFlowconventions,
        PathValues.API_CONVENTIONS_RATES_FLOWCONVENTIONS_SCOPE_CODE: ApiConventionsRatesFlowconventionsScopeCode,
        PathValues.API_CONVENTIONS_RATES_INDEXCONVENTIONS: ApiConventionsRatesIndexconventions,
        PathValues.API_CONVENTIONS_RATES_INDEXCONVENTIONS_SCOPE_CODE: ApiConventionsRatesIndexconventionsScopeCode,
        PathValues.API_CORPORATEACTIONSOURCES: ApiCorporateactionsources,
        PathValues.API_CORPORATEACTIONSOURCES_SCOPE_CODE: ApiCorporateactionsourcesScopeCode,
        PathValues.API_CORPORATEACTIONSOURCES_SCOPE_CODE_CORPORATEACTIONS: ApiCorporateactionsourcesScopeCodeCorporateactions,
        PathValues.API_COUNTERPARTIES_COUNTERPARTYAGREEMENTS: ApiCounterpartiesCounterpartyagreements,
        PathValues.API_COUNTERPARTIES_COUNTERPARTYAGREEMENTS_SCOPE_CODE: ApiCounterpartiesCounterpartyagreementsScopeCode,
        PathValues.API_COUNTERPARTIES_CREDITSUPPORTANNEXES: ApiCounterpartiesCreditsupportannexes,
        PathValues.API_COUNTERPARTIES_CREDITSUPPORTANNEXES_SCOPE_CODE: ApiCounterpartiesCreditsupportannexesScopeCode,
        PathValues.API_CUSTOMENTITIES_ENTITYTYPES: ApiCustomentitiesEntitytypes,
        PathValues.API_CUSTOMENTITIES_ENTITYTYPES_ENTITY_TYPE: ApiCustomentitiesEntitytypesEntityType,
        PathValues.API_CUSTOMENTITIES_ENTITY_TYPE: ApiCustomentitiesEntityType,
        PathValues.API_CUSTOMENTITIES_ENTITY_TYPE_IDENTIFIER_TYPE_IDENTIFIER_VALUE: ApiCustomentitiesEntityTypeIdentifierTypeIdentifierValue,
        PathValues.API_CUSTOMENTITIES_ENTITY_TYPE_IDENTIFIER_TYPE_IDENTIFIER_VALUE_RELATIONSHIPS: ApiCustomentitiesEntityTypeIdentifierTypeIdentifierValueRelationships,
        PathValues.API_DATATYPES: ApiDatatypes,
        PathValues.API_DATATYPES_SCOPE: ApiDatatypesScope,
        PathValues.API_DATATYPES_SCOPE_CODE: ApiDatatypesScopeCode,
        PathValues.API_DATATYPES_SCOPE_CODE_REFERENCEDATAVALUES: ApiDatatypesScopeCodeReferencedatavalues,
        PathValues.API_DATATYPES_SCOPE_CODE_UNITS: ApiDatatypesScopeCodeUnits,
        PathValues.API_DERIVEDTRANSACTIONPORTFOLIOS_SCOPE: ApiDerivedtransactionportfoliosScope,
        PathValues.API_DERIVEDTRANSACTIONPORTFOLIOS_SCOPE_CODE_DETAILS: ApiDerivedtransactionportfoliosScopeCodeDetails,
        PathValues.API_ENTITIES_CHANGES_PORTFOLIOS: ApiEntitiesChangesPortfolios,
        PathValues.API_EXECUTIONS: ApiExecutions,
        PathValues.API_EXECUTIONS_SCOPE_CODE: ApiExecutionsScopeCode,
        PathValues.API_FEESANDCOMMISSIONS: ApiFeesandcommissions,
        PathValues.API_FEESANDCOMMISSIONS_RULES: ApiFeesandcommissionsRules,
        PathValues.API_INSTRUMENTS: ApiInstruments,
        PathValues.API_INSTRUMENTS_GET: ApiInstrumentsGet,
        PathValues.API_INSTRUMENTS_UPSERTPROPERTIES: ApiInstrumentsUpsertproperties,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPES: ApiInstrumentsIdentifierTypes,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER: ApiInstrumentsIdentifierTypeIdentifier,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES: ApiInstrumentsIdentifierTypeIdentifierProperties,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES_DELETE: ApiInstrumentsIdentifierTypeIdentifierPropertiesDelete,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES_LIST: ApiInstrumentsIdentifierTypeIdentifierPropertiesList,
        PathValues.API_INSTRUMENTS_IDENTIFIER_TYPE_IDENTIFIER_PROPERTIES_TIMESERIES: ApiInstrumentsIdentifierTypeIdentifierPropertiesTimeSeries,
        PathValues.API_LEGALENTITIES: ApiLegalentities,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE: ApiLegalentitiesIdTypeScopeIdTypeCode,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE: ApiLegalentitiesIdTypeScopeIdTypeCodeCode,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_IDENTIFIERS: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeIdentifiers,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeMetadata,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA_METADATA_KEY: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeMetadataMetadataKey,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeProperties,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES_TIMESERIES: ApiLegalentitiesIdTypeScopeIdTypeCodeCodePropertiesTimeSeries,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONS: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeRelations,
        PathValues.API_LEGALENTITIES_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONSHIPS: ApiLegalentitiesIdTypeScopeIdTypeCodeCodeRelationships,
        PathValues.API_METADATA_ACCESS_RESOURCES: ApiMetadataAccessResources,
        PathValues.API_METADATA_DOWNLOADS_EXCELADDIN: ApiMetadataDownloadsExceladdin,
        PathValues.API_METADATA_QUOTES_RULES: ApiMetadataQuotesRules,
        PathValues.API_METADATA_QUOTES_RULES_SCOPE: ApiMetadataQuotesRulesScope,
        PathValues.API_METADATA_VERSIONS: ApiMetadataVersions,
        PathValues.API_ORDERGRAPH_BLOCKS: ApiOrdergraphBlocks,
        PathValues.API_ORDERGRAPH_PLACEMENTS: ApiOrdergraphPlacements,
        PathValues.API_ORDERINSTRUCTIONS: ApiOrderinstructions,
        PathValues.API_ORDERINSTRUCTIONS_SCOPE_CODE: ApiOrderinstructionsScopeCode,
        PathValues.API_ORDERS: ApiOrders,
        PathValues.API_ORDERS_SCOPE_CODE: ApiOrdersScopeCode,
        PathValues.API_PACKAGES: ApiPackages,
        PathValues.API_PACKAGES_SCOPE_CODE: ApiPackagesScopeCode,
        PathValues.API_PARTICIPATIONS: ApiParticipations,
        PathValues.API_PARTICIPATIONS_SCOPE_CODE: ApiParticipationsScopeCode,
        PathValues.API_PERSONS: ApiPersons,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE: ApiPersonsIdTypeScopeIdTypeCode,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE: ApiPersonsIdTypeScopeIdTypeCodeCode,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_IDENTIFIERS: ApiPersonsIdTypeScopeIdTypeCodeCodeIdentifiers,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA: ApiPersonsIdTypeScopeIdTypeCodeCodeMetadata,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_METADATA_METADATA_KEY: ApiPersonsIdTypeScopeIdTypeCodeCodeMetadataMetadataKey,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES: ApiPersonsIdTypeScopeIdTypeCodeCodeProperties,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_PROPERTIES_TIMESERIES: ApiPersonsIdTypeScopeIdTypeCodeCodePropertiesTimeSeries,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONS: ApiPersonsIdTypeScopeIdTypeCodeCodeRelations,
        PathValues.API_PERSONS_ID_TYPE_SCOPE_ID_TYPE_CODE_CODE_RELATIONSHIPS: ApiPersonsIdTypeScopeIdTypeCodeCodeRelationships,
        PathValues.API_PLACEMENTS: ApiPlacements,
        PathValues.API_PLACEMENTS_SCOPE_CODE: ApiPlacementsScopeCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE: ApiPortfoliogroupsScope,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE: ApiPortfoliogroupsScopeCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_A2B: ApiPortfoliogroupsScopeCodeA2b,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_COMMANDS: ApiPortfoliogroupsScopeCodeCommands,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_EXPANSION: ApiPortfoliogroupsScopeCodeExpansion,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_HOLDINGS: ApiPortfoliogroupsScopeCodeHoldings,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_METADATA: ApiPortfoliogroupsScopeCodeMetadata,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_METADATA_METADATA_KEY: ApiPortfoliogroupsScopeCodeMetadataMetadataKey,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PORTFOLIOS: ApiPortfoliogroupsScopeCodePortfolios,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PORTFOLIOS_PORTFOLIO_SCOPE_PORTFOLIO_CODE: ApiPortfoliogroupsScopeCodePortfoliosPortfolioScopePortfolioCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES: ApiPortfoliogroupsScopeCodeProperties,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES_DELETE: ApiPortfoliogroupsScopeCodePropertiesDelete,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES_UPSERT: ApiPortfoliogroupsScopeCodePropertiesUpsert,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_PROPERTIES_TIMESERIES: ApiPortfoliogroupsScopeCodePropertiesTimeSeries,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_RELATIONS: ApiPortfoliogroupsScopeCodeRelations,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_RELATIONSHIPS: ApiPortfoliogroupsScopeCodeRelationships,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_SUBGROUPS: ApiPortfoliogroupsScopeCodeSubgroups,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_SUBGROUPS_SUBGROUP_SCOPE_SUBGROUP_CODE: ApiPortfoliogroupsScopeCodeSubgroupsSubgroupScopeSubgroupCode,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_TRANSACTIONS: ApiPortfoliogroupsScopeCodeTransactions,
        PathValues.API_PORTFOLIOGROUPS_SCOPE_CODE_TRANSACTIONS_BUILD: ApiPortfoliogroupsScopeCodeTransactionsBuild,
        PathValues.API_PORTFOLIOS: ApiPortfolios,
        PathValues.API_PORTFOLIOS_RECONCILE_GENERIC: ApiPortfoliosReconcileGeneric,
        PathValues.API_PORTFOLIOS_RECONCILEHOLDINGS: ApiPortfoliosReconcileholdings,
        PathValues.API_PORTFOLIOS_RECONCILE_INLINE: ApiPortfoliosReconcileInline,
        PathValues.API_PORTFOLIOS_RECONCILE_VALUATION: ApiPortfoliosReconcileValuation,
        PathValues.API_PORTFOLIOS_PREVIEW_RECONCILEHOLDINGS: ApiPortfoliosPreviewReconcileholdings,
        PathValues.API_PORTFOLIOS_SCOPE: ApiPortfoliosScope,
        PathValues.API_PORTFOLIOS_SCOPE_CODE: ApiPortfoliosScopeCode,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_COMMANDS: ApiPortfoliosScopeCodeCommands,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_METADATA: ApiPortfoliosScopeCodeMetadata,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_METADATA_METADATA_KEY: ApiPortfoliosScopeCodeMetadataMetadataKey,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_PROPERTIES: ApiPortfoliosScopeCodeProperties,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_PROPERTIES_LIST: ApiPortfoliosScopeCodePropertiesList,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_PROPERTIES_TIMESERIES: ApiPortfoliosScopeCodePropertiesTimeSeries,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RELATIONS: ApiPortfoliosScopeCodeRelations,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RELATIONSHIPS: ApiPortfoliosScopeCodeRelationships,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RETURNS_RETURN_SCOPE_RETURN_CODE: ApiPortfoliosScopeCodeReturnsReturnScopeReturnCode,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RETURNS_RETURN_SCOPE_RETURN_CODE_AGGREGATED: ApiPortfoliosScopeCodeReturnsReturnScopeReturnCodeAggregated,
        PathValues.API_PORTFOLIOS_SCOPE_CODE_RETURNS_RETURN_SCOPE_RETURN_CODE_DELETE: ApiPortfoliosScopeCodeReturnsReturnScopeReturnCodeDelete,
        PathValues.API_PROPERTYDEFINITIONS: ApiPropertydefinitions,
        PathValues.API_PROPERTYDEFINITIONS_DERIVED: ApiPropertydefinitionsDerived,
        PathValues.API_PROPERTYDEFINITIONS_DOMAIN_SCOPE_CODE: ApiPropertydefinitionsDomainScopeCode,
        PathValues.API_QUOTES_SCOPE: ApiQuotesScope,
        PathValues.API_QUOTES_SCOPE_DELETE: ApiQuotesScopeDelete,
        PathValues.API_QUOTES_SCOPE_DEPRECATED: ApiQuotesScopeDeprecated,
        PathValues.API_QUOTES_SCOPE_GET: ApiQuotesScopeGet,
        PathValues.API_RECIPES: ApiRecipes,
        PathValues.API_RECIPES_SCOPE_CODE: ApiRecipesScopeCode,
        PathValues.API_REFERENCEPORTFOLIOS_SCOPE: ApiReferenceportfoliosScope,
        PathValues.API_REFERENCEPORTFOLIOS_SCOPE_CODE_CONSTITUENTS: ApiReferenceportfoliosScopeCodeConstituents,
        PathValues.API_REFERENCEPORTFOLIOS_SCOPE_CODE_CONSTITUENTSADJUSTMENTS: ApiReferenceportfoliosScopeCodeConstituentsadjustments,
        PathValues.API_RELATIONDEFINITIONS: ApiRelationdefinitions,
        PathValues.API_RELATIONDEFINITIONS_SCOPE_CODE: ApiRelationdefinitionsScopeCode,
        PathValues.API_RELATIONS_SCOPE_CODE: ApiRelationsScopeCode,
        PathValues.API_RELATIONS_SCOPE_CODE_DELETE: ApiRelationsScopeCodeDelete,
        PathValues.API_RELATIONSHIPDEFINITIONS: ApiRelationshipdefinitions,
        PathValues.API_RELATIONSHIPDEFINITIONS_SCOPE_CODE: ApiRelationshipdefinitionsScopeCode,
        PathValues.API_RELATIONSHIPDEFINITIONS_SCOPE_CODE_RELATIONSHIPS: ApiRelationshipdefinitionsScopeCodeRelationships,
        PathValues.API_RELATIONSHIPDEFINITIONS_SCOPE_CODE_RELATIONSHIPS_DELETE: ApiRelationshipdefinitionsScopeCodeRelationshipsDelete,
        PathValues.API_RESULTS_QUERYABLE_KEYS: ApiResultsQueryableKeys,
        PathValues.API_SCHEMAS_ENTITIES: ApiSchemasEntities,
        PathValues.API_SCHEMAS_ENTITIES_ENTITY: ApiSchemasEntitiesEntity,
        PathValues.API_SCHEMAS_PROPERTIES: ApiSchemasProperties,
        PathValues.API_SCHEMAS_TYPES: ApiSchemasTypes,
        PathValues.API_SCOPES: ApiScopes,
        PathValues.API_SEARCH_INSTRUMENTS: ApiSearchInstruments,
        PathValues.API_SEARCH_PORTFOLIOGROUPS: ApiSearchPortfoliogroups,
        PathValues.API_SEARCH_PORTFOLIOS: ApiSearchPortfolios,
        PathValues.API_SEARCH_PROPERTYDEFINITIONS: ApiSearchPropertydefinitions,
        PathValues.API_SEQUENCES: ApiSequences,
        PathValues.API_SEQUENCES_SCOPE: ApiSequencesScope,
        PathValues.API_SEQUENCES_SCOPE_CODE: ApiSequencesScopeCode,
        PathValues.API_SEQUENCES_SCOPE_CODE_NEXT: ApiSequencesScopeCodeNext,
        PathValues.API_SYSTEMCONFIGURATION_CUTLABELS: ApiSystemconfigurationCutlabels,
        PathValues.API_SYSTEMCONFIGURATION_CUTLABELS_CODE: ApiSystemconfigurationCutlabelsCode,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS: ApiSystemconfigurationTransactions,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS_SIDE: ApiSystemconfigurationTransactionsSide,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS_TYPE: ApiSystemconfigurationTransactionsType,
        PathValues.API_SYSTEMCONFIGURATION_TRANSACTIONS_TYPE_SOURCE: ApiSystemconfigurationTransactionsTypeSource,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE: ApiTransactionportfoliosScope,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_RESOLVE: ApiTransactionportfoliosScopeCodeResolve,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_A2B: ApiTransactionportfoliosScopeCodeA2b,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_A2BMOVEMENTS: ApiTransactionportfoliosScopeCodeA2bmovements,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_BUCKETED_CASH_FLOWS: ApiTransactionportfoliosScopeCodeBucketedCashFlows,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_CASHFLOWS: ApiTransactionportfoliosScopeCodeCashflows,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_CASHLADDER: ApiTransactionportfoliosScopeCodeCashladder,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_CASHSTATEMENT: ApiTransactionportfoliosScopeCodeCashstatement,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_DETAILS: ApiTransactionportfoliosScopeCodeDetails,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGS: ApiTransactionportfoliosScopeCodeHoldings,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGSADJUSTMENTS: ApiTransactionportfoliosScopeCodeHoldingsadjustments,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGSADJUSTMENTS_EFFECTIVE_AT: ApiTransactionportfoliosScopeCodeHoldingsadjustmentsEffectiveAt,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_HOLDINGS_WITH_ORDERS: ApiTransactionportfoliosScopeCodeHoldingsWithOrders,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_TRANSACTIONS: ApiTransactionportfoliosScopeCodeTransactions,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_TRANSACTIONS_BUILD: ApiTransactionportfoliosScopeCodeTransactionsBuild,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_TRANSACTIONS_TRANSACTION_ID_PROPERTIES: ApiTransactionportfoliosScopeCodeTransactionsTransactionIdProperties,
        PathValues.API_TRANSACTIONPORTFOLIOS_SCOPE_CODE_UPSERTABLECASHFLOWS: ApiTransactionportfoliosScopeCodeUpsertablecashflows,
        PathValues.API_TRANSLATION_INSTRUMENTDEFINITIONS: ApiTranslationInstrumentdefinitions,
        PathValues.API_UNITRESULTS_DATAMAP_SCOPE: ApiUnitresultsDatamapScope,
        PathValues.API_UNITRESULTS_DATAMAP_SCOPE_GET: ApiUnitresultsDatamapScopeGet,
        PathValues.API_UNITRESULTS_VIRTUALDOCUMENT_SCOPE_GET: ApiUnitresultsVirtualdocumentScopeGet,
        PathValues.API_UNITRESULTS_SCOPE: ApiUnitresultsScope,
        PathValues.API_UNITRESULTS_SCOPE_DELETE: ApiUnitresultsScopeDelete,
        PathValues.API_UNITRESULTS_SCOPE_GET: ApiUnitresultsScopeGet,
    }
)
