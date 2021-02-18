import json
from typing import List
from Debt import Debt

# This classes purpose is to be a container of a list of debts, as passed into the constructor


class DebtAccounts:
    def __init__(self, accounts: List[Debt] = None):
        if accounts is None:
            accounts = []
        self.accounts = accounts

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    def getTotalAmountOutstanding(self):
        total_outstanding = 0.0
        for account in self.accounts:
            total_outstanding += account.outstanding

        return total_outstanding


