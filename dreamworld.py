import math
def loan_timeline (principal):
    desired_calculation = input("What do you want to calculate?\n")
    if desired_calculation == 'm':
        monthly_payment = int(input('Enter the monthly payment:\n'))
        months = math.ceil(principal / monthly_payment)
        if months != 1:
            print(f'It will take {months} months to repay the loan')
        else:
            print(f'It will take {months} month to repay the loan')
    elif desired_calculation == 'p':
        months = int(input('Enter the number of months:\n'))
        monthly_payment = math.ceil(principal/months)
        last_payment = principal - (months - 1) * monthly_payment
        if last_payment == monthly_payment:
            print(f'Your monthly payment = {monthly_payment}')
        else:
            print(f'Your monthly payment {monthly_payment} and the last payment = {last_payment}.')
loan_timeline(principal=int(input('Enter the loan principal:\n')))