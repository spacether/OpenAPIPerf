from luisd.paths.api_transactionportfolios_scope_code_holdings.get import ApiForget
from luisd.paths.api_transactionportfolios_scope_code_holdings.put import ApiForput
from luisd.paths.api_transactionportfolios_scope_code_holdings.post import ApiForpost
from luisd.paths.api_transactionportfolios_scope_code_holdings.delete import ApiFordelete


class ApiTransactionportfoliosScopeCodeHoldings(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
