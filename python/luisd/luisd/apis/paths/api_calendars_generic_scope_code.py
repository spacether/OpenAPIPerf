from luisd.paths.api_calendars_generic_scope_code.get import ApiForget
from luisd.paths.api_calendars_generic_scope_code.post import ApiForpost
from luisd.paths.api_calendars_generic_scope_code.delete import ApiFordelete


class ApiCalendarsGenericScopeCode(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
