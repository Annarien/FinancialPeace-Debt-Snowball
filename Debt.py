""" Managing debt accounts for all debt entries. """
import json


# This class represents a single instance of a debt, such as a credit card, or a car, etc.
class Debt:

    def __init__(self, name: str, current: float, outstanding: float, interest_rate: float = 7.25):
        self.name = name
        self.current = current
        self.outstanding = outstanding
        self.interest_rate = interest_rate

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
