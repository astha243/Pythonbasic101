msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
operations = ['+', '-', '*', '/']
MEMORY = 0

def loop():
    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            break
        if answer == 'n':
            break
            

while True:
    (x, o, y) = input('Enter an equation ').split()
    if x == 'M':
        x = MEMORY
    elif y == 'M':
        y = MEMORY
    try:
        (x, y) = float(x), float(y)
    except ValueError:
        print(msg_1) 
        continue
    # elif x.isalpha() or y.isalpha():
    #     print (msg_1)
    if o in operations:
            (x, y) = float(x) ,float(y)
            if  o == "+" :
                result = x + y
                print(result) 
                store_result = input('"Do you want to store the result? (y / n):" ')
                if store_result == 'y':
                    MEMORY = result
                    continue_cal = input("Do you want to continue calculations? (y / n): ")
                    if continue_cal == 'y':
                            continue
                    else:
                            break
                else:
                    loop()
            elif  o == "-":
                result = x - y
                print(result) 
                store_result = input('"Do you want to store the result? (y / n):" ')
                if store_result == 'y':
                    MEMORY = result
                    continue_cal = input("Do you want to continue calculations? (y / n): ")
                    if continue_cal == 'y':
                            continue
                    else:
                            break
                else:
                     loop()
            elif o == "*":
                result = x * y
                print(result) 
                store_result = input('"Do you want to store the result? (y / n):" ')
                if store_result == 'y':
                    MEMORY = result
                    continue_cal = input("Do you want to continue calculations? (y / n): ")
                    if continue_cal == 'y':
                            continue
                    else:
                            break
                else:
                    loop()
            if  o == "/" and y != 0:
                result = x / y
                print(result) 
                store_result = input('"Do you want to store the result? (y / n):" ')
                if store_result == 'y':
                    MEMORY = result
                    continue_cal = input("Do you want to continue calculations? (y / n): ")
                    if continue_cal == 'y':
                            continue
                    else:
                            break
                else:
                     loop()
            else:
                print (msg_3)
                continue 
                
            # all calculation ends here so the 4th message should print here
            #  if answer is yes the result is memory and  prints message 5 and continues
            #  if the ans is no loop back to msg 4 and contines from loop4
            
    else:
        print(msg_2)
        continue
    # except ZeroDivisionError:
    #     print(msg_3)
    #     continue
    # cant use value error cause we have allowed x or y to be M
    # except ValueError:  
    #     print(msg_1)
    #     continue
    
