from enum                  import Enum
class FailureCodes(Enum):
    VALID                   = 0
    INCORRECT_PASSWORD      = 1
    INCORRECT_USERNAME      = 2
    EXISTING_USER           = 3
    INVALID_CREDENTIALS     = 4
    MISSING_PERMISSIONS     = 5
    TOO_MANY_USERS          = 6
    INVALID_USER_INPUT      = 7
    INVALID_RATE_INPUT      = 8
    INVALID_ATRIUM_INPUT    = 9
    INVALID_VENTRICLE_INPUT = 10
    CANNOT_OPEN_COM_PORT    = 11