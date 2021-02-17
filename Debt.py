""" Managing debt accounts for all debt entries. """
import json


# This class represents a single instance of a debt, such as a credit card, or a car, etc.
class Debt:

    def __init__(
            self,
            name: str,
            current: float,
            outstanding: float,
            interest_rate: float = 7.25,
            additional_payment: float = 0.0):
        self.name = name
        self.current = current
        self.outstanding = outstanding
        self.interest_rate = interest_rate
        self.additional_payment = additional_payment
        self.total_monthly_payment = self.current + self.additional_payment

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    def getMonthlyDebtPayment(self):
        self.total_monthly_payment = self.current + self.additional_payment
        return self.total_monthly_payment
