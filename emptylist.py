'''Python: Remove and print every third number from a list of numbers until the list becomes empty'''
def eleminate_3rd_num(my_list):
    i = 0
    new_list = len(my_list)
    while i <= new_list:
        
        if len(my_list) == 2:
            print(my_list.pop(1))
            print(my_list.pop(0))
            break
        else:
            # my_list.pop(2)
            print(my_list.pop(2))
        i += 1
    print(my_list)
eleminate_3rd_num(my_list= [1,5,2,3,4,10,89,90,5,6,8,7])

        