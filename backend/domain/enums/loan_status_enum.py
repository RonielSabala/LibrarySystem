from enum import StrEnum


class LoanStatusEnum(StrEnum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"
