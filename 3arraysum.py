import random
def three_sums (x,y,z):
            
            while True:
                random_num= [random.choice(x), random.choice(y), random.choice(z) ]
                if sum(random_num) == 70:
                    print (f'The unique num is {random_num}')
                    break
                # else:
                #     print(f"the sum of unique isn't 0, {random_num}")
                #     break
            
three_sums (x = [10, 20, 20, 20],
y = [10, 20, 30, 40],
z = [10, 30, 40, 20])