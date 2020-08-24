import math
import argparse

# write your code here
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"], dest="t", type = str)
parser.add_argument("--payment",type = float)
parser.add_argument("--principal", type = int)
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)
args = parser.parse_args()

if args.principal is not None and args.payment is not None and args.interest is not None and args.periods is None and args.t == "annuity":
    credit_principal = args.principal
    monthly_payment = args.payment
    interest = args.interest / 1200
    months = math.ceil(math.log((monthly_payment / (monthly_payment - interest * credit_principal)),(1 + interest)))
    overpayment = math.ceil((months * monthly_payment) - credit_principal)
    years = 0
    while months >= 12:
        years += 1
        months -= 12
    if months == 0:
        print("You need {} years to repay this credit!".format(years))
    else:
        print("You need {} years and {} months to repay this credit!".format(years, months))
    print("Overpayment = {}".format(overpayment))
elif args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
    credit_principal = args.principal
    months = args.periods
    interest = args.interest / 1200
    if args.t == "annuity":
        monthly_payment = math.ceil(credit_principal * ((interest * math.pow(1 + interest, months)) / (math.pow(1 + interest, months) - 1)))
        print("Your annuity payment = {}!".format(monthly_payment))
    elif args.t == "diff":
        sum = 0
        for m in range (1, months+1):
            monthly_payment = math.ceil((credit_principal / months) + interest * (credit_principal - ((credit_principal * m - credit_principal) / months)))
            print("Month {}: paid out {}".format(m, monthly_payment))
            sum += monthly_payment
        print("\nOverpayment = {}".format(sum - credit_principal))
    else:
        print("Incorrect parameters.")
elif args.payment is not None and args.periods is not None and args.interest is not None and args.principal is None and args.t == "annuity":
    monthly_payment = args.payment
    months = args.periods
    interest = args.interest / 1200
    credit_principal = math.ceil(monthly_payment / ((interest * math.pow(1 + interest, months)) / (math.pow(1 + interest, months) - 1)))
    print("Your credit principal = {}!".format(credit_principal))
    print("Overpayment = {}".format((monthly_payment * months) - credit_principal))
else:
    print("Incorrect parameters.")


