'''Write a program that reads 2 numbers, a and b, from the input. As an output, it shows the mean of all numbers that lie on the interval between a and b, and are divisible by 3.'''

def reminder (a,b):
    nums = [ x for x in range(a, (b + 1)) if x % 3 == 0]
    '''
    divisibl_by_3 = []
    for x in range(a,b):
        if x % 3 == 0:
            divisibl_by_3.append(x)
    print(sum(divisibl_by_3) / len(divisibl_by_3)) '''
    # mean_of_all_num = sum(divisibl_by_3) / len(divisibl_by_3)
    # print(mean_of_all_num) 
    print(nums)
    print(sum(nums)/ len(nums))
reminder(-5,12)
            