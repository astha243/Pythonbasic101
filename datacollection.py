msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
operations = ['+', '-', '*', '/']
memory = M = 0
def calculation():
    while True:
        print(msg_0)
        calc = input()
        (x, o, y) = calc.split()
        try:
            float(x) and float(y)
            if o in operations:
                break
            else:
                print(msg_2)
            continue
        except ValueError:
            print(msg_1)
            continue
        
        
calculation()
        
'''my old soln
# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
while True:
  print(msg_0)
  calc = input()
  x,oper,y = calc.split()
  operation_list = ["+", "-", "*", "/"]
  # x = int(x)
  # y = int(y)
  try:
    float(x) and float (y)
  except Exception:
    print(msg_1)
    continue
  
  if oper in operation_list:
    pass
    
  else:
    oper not in operation_list
    print(msg_2)
    continue
  break'''