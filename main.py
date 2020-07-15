# 1. Storing elements of a list into new variables

list = [1,2,3]
x,y,z = list
print(x,y,z)   # Output: 1 2 3


# 2. Display the path of the imported modules

import threading
import Tkinter

print(threading)
print(Tkinter)


# 3. The interactive operator " _ " shows the output of the last executed expression
     # lets run it on shell
     
>>> 2+7
9
>>> _
9


# 4. Concatenate Strings

characters = ['a','r','m','a','n']
word = "".join(characters)
print(word)       #Output: arman


#5. Convert 2 lists into a dictionary

students = ["Arman","Nora Fatehi"]
marks = [99,100]
dictionary = dict(zip(students,marks))
print(dictionary)         #Output: {'Arman': 99, 'Nora Fatehi': 100}


