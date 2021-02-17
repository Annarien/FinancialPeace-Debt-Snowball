import json
from typing import List
from Debt import Debt

# This classes purpose is to be a container of a list of debts, as passed into the constructor


class DebtAccounts:
    def __init__(self, debts: List[Debt] = None):
        if debts is None:
            debts = []
        self.accounts = debts

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
