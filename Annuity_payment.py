import math
def loan_timeline ():
    desired_calculation = input('''What do you want to calculate?\ntype "n" for number of monthly payments,\ntype "a" for annuity monthly payment amount,\ntype "p" for loan principal:\n''')
    if desired_calculation == 'n':
        P = float(input("Enter the loan principal: "))
        A = float(input("Enter the monthly payment: "))
        loan_intrest = float(input("Enter the loan interest: "))
        i = (loan_intrest / (12 * 100))
        x =(A / (A - (i * P)))
        base = (1 + i)
        N = math.ceil(math.log(x , base))
        print (N)
        year, months = divmod(N, 12)  
        print(year, months)
        if year == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0 and year == 1:
            print(f"It will take {year} year to repay this loan!")
        else:
            print(f"It will take {year} years and {months} months to repay this loan!")   
    elif desired_calculation == 'a':
        P = float(input("Enter the loan principal: "))
        N = float(input("Enter the number of periods: "))
        loan_intrest = float(input("Enter the loan interest: "))
        i = (loan_intrest / (12 * 100))
        A = math.ceil(P * ( (i * pow( 1 + i, N)) / ((pow(1 + i, N )) - 1)))
        print(f"Your monthly payment = {A}!")
    elif desired_calculation == 'p':
        A = float(input("Enter the annuity payment: "))
        N = float(input("Enter the number of periods: "))
        loan_intrest = float(input("Enter the loan interest: "))
        i = (loan_intrest / (12 * 100))
        P = round(A / ((i * (pow(1 + i, N ))) / ((pow(1 + i, N )) - 1)))
        print(f'Your loan principal = {P}!')
        
loan_timeline()
