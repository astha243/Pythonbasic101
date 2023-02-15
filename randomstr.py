'''Write a Python program to create all possible strings by using 
'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.'''

import random
def random_str (my_list):
    i = 0
    while i < len(my_list):
       
        unique_list = random.sample(my_list, 5)
        print (unique_list)
        i += 1
        
(random_str(my_list=['a', 'e', 'i', 'o', 'u'])) 