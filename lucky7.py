'''Read the first input – a number n. Then read input n times. Each time you'll get an integer value.
If it's a multiple of 7 (can be divided by 7 without a remainder), print its square on a new line. 
Note that you don't need to perform any calculations on the first input (the n).'''
# my solution
first_input = int(input("Enter a number: "))
counter = 0
final_squared_value = []
while counter < first_input:
    user_int_value = int(input("Enter your number: "))
    if user_int_value % 7 == 0:
        final_squared_value.append(user_int_value ** 2)
    counter += 1
for x in final_squared_value:
    print(x)