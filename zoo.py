while True:
    animal_in_zoo = ['camel', 'lion', 'deer', 'goose', 'bat', 'rabbit']
    animal_selection_byuser = (input('Please enter the number of the habitat you would like to view:'))
    if animal_selection_byuser != 'exit':
            print(animal_in_zoo[int(animal_selection_byuser)])
            
    elif animal_selection_byuser == 'exit':
        break
print('See you later!')
        

