from luisd.paths.api_systemconfiguration_transactions_type_source.get import ApiForget
from luisd.paths.api_systemconfiguration_transactions_type_source.put import ApiForput
from luisd.paths.api_systemconfiguration_transactions_type_source.delete import ApiFordelete


class ApiSystemconfigurationTransactionsTypeSource(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
