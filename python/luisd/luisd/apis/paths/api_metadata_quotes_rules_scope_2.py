from luisd.paths.api_metadata_quotes_rules_scope_2.get import ApiForget
from luisd.paths.api_metadata_quotes_rules_scope_2.post import ApiForpost
from luisd.paths.api_metadata_quotes_rules_scope_2.delete import ApiFordelete


class ApiMetadataQuotesRulesScope(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
