# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 07:31:42 2023

@author: UmerShahzad
"""

#=====================Python Slicing Strings================================
'''Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.'''

k='umershahzad';
print(k[1:8])

#====================See Another Example============================
g='SZABIST';
print(g[1:3])

'''Slice From the Start
By leaving out the start index, the range will start at the first character:'''

y='umer';
print(y[:3])

#=====================See Another Example=====================
t='Zeeshan-ul-Hassan Usmani';
print(t[:10])

#==================Slice To the End=======================
w='Muhammad Umer';
print(w[-2:-1])

#=====================Python Modify Strings===================
o="I want to learn python";
print(o.upper()) #using upper function you can print the string capitalized

#=================Lower Case=====================
q='UMER SHAHZAD';
print(q.lower())

#================== Python Remove Whitespace=======================
s=  'umer shahzad'
print(s.strip()) #this function is used to remove whitespace if you add in the start of text.

#=======================Python Replace String======================
f="Programming in python";
print(f.replace("g", "r")) 
'''Be Remember it doesn't change the Word it only change the string or letter'''

#=========================Python Split String======================
'''The split() method returns a list where the text between the specified separator becomes the list items.'''
d='Umershahzad';
b=d.split(",")
print(b)

#=====================Python String Concatenation=======================
r="Umer";
e='Shahzad';
print(r+e) #You can Solve more examples like this!

#====================Python - Format - Strings======================
'''we Learned before we cannot combine strings and numbers
But we can combine strings and numbers by using the format() method!
'''
age=22;
l='Usama is {}';
print(l.format(age))

#==============Python Escape Character=========================
'''To insert characters that are illegal in a string, use an escape character'''

y='I am UmerShahzad from \"SZABIST\"';
print(y)
    