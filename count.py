from collections import Counter
def counting_letters(a):
    letters_in_str =[]
    for i in a:
       if i == ' ':
           continue
       else:
        letters_in_str.append(i)
    
    print( Counter(letters_in_str))
    
    
   
   
        
        
(counting_letters(a='my name is astha'))