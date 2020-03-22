letters = "abcdefghijklmnopqrstuvwxyz"
numbers = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
welcome = input("Welcome, amay i please have your name? :" )
phrase = input("please type the word here :")

for letter in letters:
    count = phrase.count(letter)
    if count > 1 :
        print( str(welcome) + ", in the phrase/word you have provided, \nThe letter :" + str(letter) + " , appears once i.e :", count)

for number in numbers:
    count = phrase.count(number)
    if count > 1 :
       print( str(welcome) + ", in the phrase/word you have provided, \nThe number :" + str(number) + " , appears once i.e :", count)          
