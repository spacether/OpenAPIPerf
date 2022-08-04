from luisd.paths.api_portfolios_scope_code_properties.get import ApiForget
from luisd.paths.api_portfolios_scope_code_properties.post import ApiForpost
from luisd.paths.api_portfolios_scope_code_properties.delete import ApiFordelete


class ApiPortfoliosScopeCodeProperties(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
