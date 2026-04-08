from datetime import datetime

from backend.repository.loan_repository import LoanRepository


def renew_loan(
    book_id: int,
    student_id: int,
    new_end_date: datetime,
) -> bool:

    repository = LoanRepository()

    loan = repository.get_by_ids(book_id, student_id)

    if not loan:
        return False

    loan.end_date = new_end_date

    return repository.update(loan)
