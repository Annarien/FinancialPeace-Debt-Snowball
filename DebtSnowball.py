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
    debt_class = Debt(name=individual_debt["name"], current=individual_debt["current"], outstanding=individual_debt["outstanding"])
    debt_accounts.debt_accounts.append(debt_class)
print(debt_accounts.toJSON())

add_remove_skip = input(
    "Do you want to add a new debt entry (add), remove old debt (remove) or continue onto the debt snowball (skip)\n")

amount = 0
if add_remove_skip == 'add':  # adding new debt
    new_amount = int(input("How many new debts do you want to add? (integer only) \n"))
    if new_amount > 0:
        while amount < new_amount:
            new_debt_account = DebtSnowballUtils.create_debt_account()
            debt_accounts.debt_accounts.append(new_debt_account)
            amount += 1
    else:
        raise ValueError(" You have entered 0 amounts of new Debt to be added!")
#
# if add_remove_skip == 'remove':  # remove old debt
#     remove_amount = int(input("How many debts do you want to remove ? (integer only) \n"))
#     if remove_amount > 0:
#         while amount < remove_amount:
#             remove_debt = input("Enter the name of the debt you wish to remove: \n")
#             try:
#                 for i in range(len(data)):
#                     if data[i]['name'] == remove_debt:
#                         del data[i]
#                         break
#             except KeyError:
#                 raise KeyError("No Entry like that exists!")
#                 break

# write new debt to json file
with open('Debts.json', 'w') as outfile:
    json.dump(debt_accounts.__dict__, outfile, default=lambda o: o.__dict__, indent=4)
