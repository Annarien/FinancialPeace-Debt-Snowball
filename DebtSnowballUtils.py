"""This is a utils python file, containing a class called DebtSnowballUtils in which various functions are created."""

# imports
from typing import List

from Debt import Debt
from DebtAccounts import DebtAccounts

# from DebtSnowball import debt


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
    def debtSnowball(debts: DebtAccounts):
        remaining_income = float(input('Enter how much extra money you have in your budget after staying current. \n'))
        times_paid = 0
        print(f"The total amount of debt still to be paid off is: {debts.getTotalAmountOutstanding()}")

        for i in range(0, len(debts.accounts)):
            debts.accounts[i].amount_left_to_pay = debts.accounts[i].outstanding - remaining_income
            times_paid += 1
            debts.accounts[i].months_to_pay_off = times_paid

            if debts.accounts[i] is not Debt.isPaidOff(outstanding=debts.accounts[i].outstanding):
                # debts_accounts[i].amount_left_to_pay = debts_accounts[i].outstanding - remaining_income
                if debts.accounts[i].amount_left_to_pay < 0.00:
                    remaining_income = abs(debts.accounts[i].amount_left_to_pay)
                    print(f"Paid off {debts.accounts[i].name}")
                    print(f"The amount of debts paid off is: {times_paid}.")
                    print(f"The total amount of debt still to be paid off is: {debts.getTotalAmountOutstanding()}")

                    i += 1

                elif debts.accounts[i].amount_left_to_pay > 0.00:
                    debts.accounts[i].outstanding = abs(debts.accounts[i].amount_left_to_pay)
                    print(
                        f"Not paid off {debts.accounts[i].name}, the amount outstanding is {debts.accounts[i].outstanding}")
                    print(f"The amount of debts paid off is: {times_paid}.")
                    print(f"The total amount of debt still to be paid off is: {debts.getTotalAmountOutstanding()}")
                    break

            elif debts.accounts[i] is Debt.isPaidOff(outstanding=debts.accounts[i].outstanding):
                print(f"{debts.accounts[i].name} has been paid off.")
                i += 1
            #     times_paid += 1
            # debts_accounts[i].times_paid = times_paid
            # print(f"The amount of debts paid off is: {times_paid}.")
            # print(f"The total amount of debt still to be paid off is: {debts.getTotalAmountOutstanding()}")
