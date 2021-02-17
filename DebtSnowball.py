"""This is a python file in which the running of various functions is executed in order for a DebtSnowball to be
possible. The functions are called from the DebtSnowball_utils.py. This project follows the plaaning and is part of the
FinancialPeace Project."""
import json
from DebtSnowball_Utils import DebtSnowballUtils
from Debt import Debt
from DebtAccounts import DebtAccounts

# opening json file
debt_accounts = DebtAccounts()
debt_data = json.load(open('Debts.json'))
for individual_debt in debt_data["debt_accounts"]:
    debt_class = Debt(name=individual_debt["name"], current=individual_debt["current"],
                      outstanding=individual_debt["outstanding"])
    debt_accounts.debt_accounts.append(debt_class)
print(debt_accounts.toJSON())

add_remove_sort = input(
    "Do you want to add a new debt entry (add), remove old debt (remove) or continue onto the debt snowball (sort)\n")
amount = 0
if add_remove_sort == 'add':  # adding new debt
    new_amount = int(input("How many new debts do you want to add? (integer only) \n"))
    if new_amount > 0:
        while amount < new_amount:
            new_debt_account = DebtSnowballUtils.create_debt_account()
            debt_accounts.debt_accounts.append(new_debt_account)
            amount += 1
    else:
        raise ValueError(" You have entered 0 amounts of new Debt to be added!")
#
if add_remove_sort == 'remove':  # remove old debt
    remove_amount = int(input("How many debts do you want to remove ? (integer only) \n"))
    if remove_amount > 0:
        while amount < remove_amount:
            remove_debt = input("Enter the name of the debt you wish to remove: \n")
            for debt in debt_accounts.debt_accounts:
                if debt.name == remove_debt:
                    debt_accounts.debt_accounts.remove(debt)
                    print(f"Removed {debt.name}")
                    amount += 1
            if amount > remove_amount:
                print(f"No debt entry for the given name {remove_debt} exists")
                break

if add_remove_sort == 'sort':
    sorted_list = DebtSnowballUtils.sortDebtSnowball(debt_data["debt_accounts"])
    sorted_dict = {"sorted_debt_accounts": sorted_list}

# write new debt to json file
with open('Debts.json', 'w') as outfile:
    json.dump(debt_accounts.__dict__, outfile, default=lambda o: o.__dict__, indent=4)

with open('SortedDebts.json', 'w') as sorted_file:
    json.dump(sorted_dict, sorted_file)
