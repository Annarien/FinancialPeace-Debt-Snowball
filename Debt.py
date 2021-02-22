""" Managing debt accounts for all debt entries. """
import json


# This class represents a single instance of a debt, such as a credit card, or a car, etc.
class Debt:

    def __init__(
            self,
            name: str,
            current: float,
            outstanding: float,
            amount_left_to_pay: float,
            interest_rate: float = 7.25,
            additional_payment: float = 0.0,
            months_to_pay_off: int = 0):
        self.name = name
        self.current = current
        self.outstanding = outstanding
        self.interest_rate = interest_rate
        self.additional_payment = additional_payment
        self.total_monthly_payment = self.current + self.additional_payment
        self.amount_left_to_pay = self.outstanding - self.total_monthly_payment
        self.months_to_pay_off = months_to_pay_off

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    def getMonthlyDebtPayment(self):
        self.total_monthly_payment = self.current + self.additional_payment
        return self.total_monthly_payment

    @staticmethod
    def isPaidOff(outstanding):
        return outstanding <= 0.0

    def leftToPay(self):
        self.amount_left_to_pay = self.outstanding - self.getMonthlyDebtPayment()
        return self.amount_left_to_pay
