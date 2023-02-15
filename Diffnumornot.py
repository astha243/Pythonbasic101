
def numbers (my_list):
   
    if len(my_list) == len(set(my_list)):
       return True
    else:
        return False
print(numbers(my_list=[1,2,3,4,4,6]))