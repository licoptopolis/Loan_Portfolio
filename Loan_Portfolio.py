import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Defining the Loan Class
class Loan:
    def __init__(self, id, amount, interest_rate, start_date, end_date, status):
        self.id = id # Unique Loan Identification
        self.amount = amount
        self.interest_rate = interest_rate
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def get_interest(self): # interest = (amount * interest_rate * days) / 365
        days = (self.end_date - self.start_date).days
        interest = self.amount * self.interest_rate * days / 365
        return round(interest, 2)

# Defining Loan Portfolio Class
class LoanPortfolio:
    def __init__(self, loans=None):
        self.loans = loans or []

    def add_loan(self, loan):
        self.loans.append(loan)

    def remove_loan(self, loan):
        self.loans.remove(loan)

    def calculate_total_interest(self):
        active_loans = filter(lambda loan: loan.status == "active", self.loans)
        total_interest = sum(map(lambda loan: loan.get_interest(), active_loans))
        return round(total_interest, 2)

    def get_loan_status(self, id):
        loan_statuses = {loan.id: loan.status for loan in self.loans}
        return loan_statuses.get(id, None)

    def update_loan_status(self, id, new_status):
        loan = next((loan for loan in self.loans if loan.id == id), None)
        if loan:
            loan.statuses = new_status
            return True
        return False

    def get_overdue_loans(self, num_loans):
        loan_id = len(self.loans) + 1
        for i in range(num_loans):
            amount = round(random.uniform(10000, 1000000), 2)
            interest_rate = round(random.uniform(0.07, 0.09), 4) # United Kingdom Interest Rate
            start_date = datetime.today() - timedelta(days=random.randint(1, 365))
            end_date = start_date + timedelta(days=random.randint(30, 365))
            status = random.choice(['active', 'closed'])
            loan = Loan(loan_id, amount, interest_rate, start_date, end_date, status)
            self.add_loan(loan)
            loan_id += 1

# Testing the Loan Portfolio Class
if __name__ == '__main__':
    loan1 = Loan(1, 100000, 0.10, datetime(2022, 1, 1), datetime(2022, 12, 31), 'active')
    loan2 = Loan(2, 50000, 0.05, datetime(2021, 1, 1), datetime(2022, 6, 30), 'closed')
    portfolio = LoanPortfolio([loan1, loan2])
    portfolio.get_overdue_loans(3)
    print('Loan portfolio:')
    for loan in portfolio.loans:
        print(
            f'Loan {loan.id}: amount={loan.amount}, interest_rate={loan.interest_rate}, start_date={loan.start_date}, end_date={loan.end_date}, status={loan.status}')
    print(f'Total interest: {portfolio.calculate_total_interest()}')
    print(f'Loan status for id 2: {portfolio.get_loan_status(2)}')

