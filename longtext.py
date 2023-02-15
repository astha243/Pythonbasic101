''' Write a Python program to print a long text, 
convert the string to a list and print all the words and their frequencies.'''

def word_frequency(word):

    str_to_lst = word.split()
    word_count = [str_to_lst.count(i) for i in str_to_lst ]
    print(list(zip(str_to_lst, word_count)))
(word_frequency('''The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''))

