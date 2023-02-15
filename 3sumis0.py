import random
def three_sums (my_list):
            i = 0
            while i < len(my_list):
                random_num= [random.choice(my_list), random.choice(my_list), random.choice(my_list) ]
            
                i += 1  
                
                if sum(random_num) == 0:
                    print (f'The unique num is {random_num}')
                    break
            # else:
            #     print(f"the sum of unique isn't 0, {random_num}")
            #     break
            
three_sums (my_list=[1, -6, 4, 2, -1, 2, 0, -2, 0])