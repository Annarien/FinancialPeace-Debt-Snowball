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
    def moneyInsertionForCurrent(money, sorted_list):
        """
        This inserts the extra money after paying all bills into the debts. This is adds the money to all debts the contain payments needed to keep current payments.
        Args:
            money(float):       This is the money to pay all current bills.
            sorted_list(list):  This is the sorted list of all debts
        """

        for i in sorted_list:
            print(sorted_list[i])





