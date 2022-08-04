from luisd.paths.api_transactionportfolios_scope_code_transactions.get import ApiForget
from luisd.paths.api_transactionportfolios_scope_code_transactions.post import ApiForpost
from luisd.paths.api_transactionportfolios_scope_code_transactions.delete import ApiFordelete


class ApiTransactionportfoliosScopeCodeTransactions(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
