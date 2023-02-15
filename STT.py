'''Here is your chance to write instructions for a text-to-speech system. 
Let's focus on reading phone numbers aloud. The input phone number will consist solely of digits.
Print the name of each digit on a new line for the system to read them one by one.'''

# My soln
def user_contact(a):
        nums = ['Zero',  'One', 'two', 'Three', 
            'Four','Five','Six', 'Seven','Eight','nine']
        result = []
        for i in a:
                result.append(int(i))
        print (result)
        for j in result:
          print(nums[j])
                
(user_contact(9841))
        
# more simpler soln
'''
nums = ['Zero',  'One', 'two', 'Three', 
            'Four','Five','Six', 'Seven','Eight','nine']
for index in input('Enter your phone number:    '):
        print(nums[int(index)])
'''
