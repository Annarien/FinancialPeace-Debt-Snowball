"""This is a utils python file, containing a class called DebtSnowballUtils in which various functions are created."""

# imports
from typing import List

from Debt import Debt


# creating a class called DebtSnowballClass

class DebtSnowballUtils:
    def __init__(self, debt):
        """
        This is the init file
        Args:
            debt_name (str):         This is the intialising of the debt name.
            debt_current (float):    This is the initialising of the amount needed to be paid each month in order for the
                                     debt payments to stay current.
            debt_outstanding(float): The amount still outstanding on the debt.
        """
        self.debt_name = debt.name
        self.debt_current = debt.current
        self.debt_outstanding = debt.outstanding

    @staticmethod
    def create_debt_account():
        """
        Adding each debt's name, amount to stay current, and outstanding amount to dictionary.
        Args:
            debt_name (str):             This is the name of the debt.
            debt_current(float):         This is the minimum amount needed each month to keep the debt current.
            debt_outstanding(float):     This is the amount outstanding on paying off the debt.

        Returns:
            debt_dict (dict):       A dictionary of a debt including the debts name, amount to stay current and the
                                    total outstanding debt.
        """

        debt_name = input("Enter name of debt: \n")
        debt_current = float(input("Enter amount to keep debt current: \n"))
        debt_outstanding = float(input("Enter the amount of debt that is currently outstanding: \n"))

        return Debt(debt_name, debt_current, debt_outstanding)

    @staticmethod
    def sortDebtSnowball(debt_data_accounts: List[Debt]):
        """
        This sorts the debt in terms of the outstanding debt.
        Args:
            debt_data_accounts(list):    This is a list of all debt accounts
        Returns:
            sorted_ist(list):     This is a sorted list of all debt accounts
        """

        sorted_list = sorted(debt_data_accounts, key=lambda k: k.outstanding)
        return sorted_list

    @staticmethod
    def debtSnowball(debts):
        # inserting money into debts that is needed into current payments necessary
        print(f"Total amount owed: R{debts.getTotalAmountOutstanding()}")
        remaining_income = float(input('Enter how much extra money you have in your budget after staying current. \n'))

        while debts.getTotalAmountOutstanding() > 0:
            # simulate months.
            # each iteration of this loop will represent one month.
            # debts.accounts[0].outstanding -= debts.accounts[0].getMonthlyDebtPayment()
            # eventually this will become <= 0, move to the next debt

            for i in range(0, len(debts.accounts)):
                if i == 0 and not debts.accounts[0].isPaidOff():
                    debts.accounts[0].additional_payment = remaining_income
                if i == 1 and not debts.accounts[1].isPaidOff() and debts.accounts[0].isPaidOff():
                    debts.accounts[1].additional_payment = debts.accounts[0].getMonthlyDebtPayment()
                if i == 2 and not debts.accounts[2].isPaidOff() and debts.accounts[1].isPaidOff():
                    debts.accounts[2].additional_payment = debts.accounts[1].getMonthlyDebtPayment()
                if i == 3 and not debts.accounts[3].isPaidOff() and debts.accounts[2].isPaidOff():
                    debts.accounts[3].additional_payment = debts.accounts[2].getMonthlyDebtPayment()

                if not debts.accounts[i].isPaidOff():
                    print(
                        f"Subtracting {debts.accounts[i].getMonthlyDebtPayment()} from {debts.accounts[i].outstanding}")
                    debts.accounts[i].outstanding -= debts.accounts[i].getMonthlyDebtPayment()
