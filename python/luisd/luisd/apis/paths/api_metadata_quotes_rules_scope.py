from luisd.paths.api_metadata_quotes_rules_scope.get import ApiForget
from luisd.paths.api_metadata_quotes_rules_scope.post import ApiForpost
from luisd.paths.api_metadata_quotes_rules_scope.delete import ApiFordelete


class ApiMetadataQuotesRulesScope(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
