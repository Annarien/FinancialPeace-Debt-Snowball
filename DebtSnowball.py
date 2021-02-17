"""This is a python file in which the running of various functions is executed in order for a DebtSnowball to be
possible. The functions are called from the DebtSnowball_utils.py. This project follows the plaaning and is part of the
FinancialPeace Project."""
import json
from DebtSnowballUtils import DebtSnowballUtils
from Debt import Debt
from DebtAccounts import DebtAccounts

# opening json file
debts = DebtAccounts()
debt_data = json.load(open('Debts.json'))
for individual_debt in debt_data["accounts"]:
    name = individual_debt["name"]
    current = individual_debt["current"]
    outstanding = individual_debt["outstanding"]

    try:
        interest_rate = individual_debt["interest_rate"]
    except KeyError:
        interest_rate = 0.0

    try:
        additional_payment = individual_debt["additional_payment"]
    except KeyError:
        additional_payment = 0.0

    debt_class = Debt(name,
                      current,
                      outstanding,
                      interest_rate,
                      additional_payment)
    debts.accounts.append(debt_class)

add_or_remove = input("Do you want to add or remove a debt account? yes/no \n")
if add_or_remove == "yes":
    option = input("Do you want to add a new debt entry (add), remove old debt (remove)\n")
    amount = 0
    if option == 'add':  # adding new debt
        new_amount = int(input("How many new debts do you want to add? (integer only) \n"))
        if new_amount > 0:
            while amount < new_amount:
                new_debt_account = DebtSnowballUtils.create_debt_account()
                debts.accounts.append(new_debt_account)
                amount += 1
        else:
            raise ValueError(" You have entered 0 amounts of new Debt to be added!")

    if option == 'remove':  # remove old debt
        remove_amount = int(input("How many debts do you want to remove ? (integer only) \n"))
        if remove_amount > 0:
            while amount < remove_amount:
                remove_debt = input("Enter the name of the debt you wish to remove: \n")
                for debt in debts.accounts:
                    if debt.name == remove_debt:
                        debts.accounts.remove(debt)
                        print(f"Removed {debt.name}")
                        amount += 1
                if amount > remove_amount:
                    print(f"No debt entry for the given name {remove_debt} exists")
                    break

debts.accounts = DebtSnowballUtils.sortDebtSnowball(debts.accounts)
# print(debts.toJSON())

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

        if not debts.accounts[i].isPaidOff():
            print("Subtracting")
            debts.accounts[i].outstanding -= debts.accounts[i].getMonthlyDebtPayment()

print(debts.toJSON())

# write new debt to json file
# with open('Debts.json', 'w') as outfile:
    # json.dump(debts.__dict__, outfile, default=lambda o: o.__dict__, indent=4)
