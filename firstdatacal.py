msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
operations = ['+', '-', '*', '/']
def math (x, o , y):
    if  o == "+":
        return x + y 
    elif  o == "-":
        return x - y 
    elif o == "*":
       return x * y 
    elif  o == "/":
        return x / y 
                    
                
def calculation():
    while True:
        (x, o, y) = input('Enter an equation ').split()
        try:
            if o in operations:
                (x, y) = float(x) ,float(y)
                print(math(x, o, y))
                break
            else:
                print(msg_2)
                continue
        except ZeroDivisionError:
            print(msg_3)
            continue
        except ValueError:
            print(msg_1)
            continue
        
calculation()