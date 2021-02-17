"""This is a utils python file, containing a class called DebtSnowballUtils in which various functions are created."""

# imports
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
    def sortDebtSnowball(debt_data_accounts):
        """
        This sorts the debt in terms of the debt.
        Args:
            debt_accounts(list):    This is a list of all debt accounts
        Returns:
            sorted_debts(list):     This is a sorted list of all debt accounts
            :param debt_data_accounts:
        """

        print(debt_data_accounts)
        sortedlist = sorted(debt_data_accounts, key=lambda k: k['outstanding'])
        print('Sorted List: ' + str(sortedlist))
        return sortedlist
