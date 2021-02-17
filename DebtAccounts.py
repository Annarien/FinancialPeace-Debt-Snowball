import json
import Debt
from typing import List


# This classes purpose is to be a container of a list of debts, as passed into the constructor
class DebtAccounts:
    def __init__(self, debts=None):
        if debts is None:
            debts = []
        self.debt_accounts = debts

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
