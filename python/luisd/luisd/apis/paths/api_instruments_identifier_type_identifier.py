from luisd.paths.api_instruments_identifier_type_identifier.get import ApiForget
from luisd.paths.api_instruments_identifier_type_identifier.post import ApiForpost
from luisd.paths.api_instruments_identifier_type_identifier.delete import ApiFordelete


class ApiInstrumentsIdentifierTypeIdentifier(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
