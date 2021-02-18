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


DebtSnowballUtils.debtSnowball(debts)

print(debts.toJSON())

# DebtSnowballUtils.debtSnowball(debts)

# write new debt to json file
# with open('Debts.json', 'w') as outfile:
# json.dump(debts.__dict__, outfile, default=lambda o: o.__dict__, indent=4)
