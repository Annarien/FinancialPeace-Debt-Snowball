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
        """
        Creating the Debt Snowball, each debt is paid off by paying off the current amount of all debts.
        If there us enough money, each debt is paid off and the current payment for that debt is added to the overall
        income. This creates a snowball effect of income to pay off debt, paying off debt faster.
        Args:
            debts (DebtAccounts): Class containing all debts and some helper functions.
        """
        remaining_income = float(input('Enter how much extra money you have in your budget after staying current. \n'))
        monthly_available_extra = remaining_income
        old_total_amount_outstanding = debts.getTotalAmountOutstanding()
        print(f"The total amount of debt still to be paid off is: {old_total_amount_outstanding}")

        month = 0
        while debts.getTotalAmountOutstanding() > 0:
            print("\n")
            print(f"Month: {month}\n")
            print("=========================================\n")

            # Keeping current on all debts
            for account in debts.accounts:
                if not account.isPaidOff():
                    if account.current >= account.amountLeftToPay():
                        account.makeAdditionalMonthlyPayment(account.amountLeftToPay())
                    else:
                        account.makeMonthlyPaymentToStayCurrent()

            # Pay extra
            money_left_for_the_month = monthly_available_extra
            for account in debts.accounts:
                print(f"We have R{money_left_for_the_month} extra left for the month")
                if not account.isPaidOff() and money_left_for_the_month > 0:
                    if money_left_for_the_month >= account.amountLeftToPay():  # Pay it off in one month
                        print(f"We still owe R{account.amountLeftToPay()}, paying it off now.")
                        print(f"Adding R{account.current} to our available extra spend for each month.")
                        print(f"We had R{monthly_available_extra} available each month, we will now have R{monthly_available_extra + account.current}")
                        # print(f"We have R{money_left_for_the_month - account.amountLeftToPay()} left for the month, moving to next account")

                        money_left_for_the_month -= account.amountLeftToPay()  # Take out the money we're about to spend
                        monthly_available_extra += account.current  # Add the accounts current payment to the amount we have extra each month
                        account.has_been_added_to_snowball = True  # Add the account to the list of accounts paid off and part of the snowball
                        account.makeAdditionalMonthlyPayment(account.amountLeftToPay())  # Spend the money
                    else:  # We don't have enough to pay it off in one month, so pay what we can
                        print(f"We still owe R{account.amountLeftToPay()} but only have R{money_left_for_the_month}, paying what we can.")
                        print(f"We now have R0 extra left for this month")

                        account.makeAdditionalMonthlyPayment(money_left_for_the_month)  # Use everything we have to pay as much as we can
                        money_left_for_the_month = 0  # We've got nothing left for this month, try again next month
                elif account.isPaidOff() and not account.has_been_added_to_snowball:  # Account is paid off simply by staying current, but we must add it to our snowball
                    print("Account is paid off by staying current with our payments")
                    print(f"Adding R{account.current} to our available extra spend for each month.")
                    print(f"We had R{monthly_available_extra} available each month, we will now have R{monthly_available_extra + account.current}")
                    monthly_available_extra += account.current  # Add the accounts current payment to the amount we have extra each month
                    account.has_been_added_to_snowball = True  # Add the account to the list of accounts paid off and part of the snowball

            month += 1

        print("DONE!")
        new_total_amount_outstanding = debts.getTotalAmountOutstanding()
        print(f"The new total amount of debt still to be paid off is: R{new_total_amount_outstanding}")
        print(f"The total of debt paid of is: R{abs(new_total_amount_outstanding - old_total_amount_outstanding)}")
