# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 06:06:05 2023

@author: UmerShahzad

"""

#================Python Numbers=============
#There are 3 types in python int,complex,float

x=1;
w=2.0;
h=2.3342200567;
p=-2.33415;
t=2j;
print(type(x))
print(type(w))
print(type(h))
print(type(p))
print(type(t))

#====================Python Type Conversion========================
z=21;
l=9.887;
i=float(z)
n=int(l)
print(i)
print(n)


#=====================See Another Example=========================
g=4;
v=4.654;
m=float(g)
b=int(v)
print(m)
print(b) #=====you can do more exercises on you behalf======


#===================Python Random Number==============================
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers

import random;
print(random.randrange(0,13))

#=================Python Strings=====================
'''Strings in python are surrounded by either single quotation marks, or double quotation marks.

 'umer' is the same as "umer" use the print function to see results.'''

#========Assigning String to a Variable============
l='UmerShahzad';
print(l)
#==========Multiline Strings================
r="""I am UmerShahzad. I am from beautiful country Pakistan
     I am teaching you python programming""" #==you can also use single quotes it doesn't affect==
print(r)

#====================Strings are Arrays====================
'''Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.'''

o="UmerShahzad";
print(o[1]) #=======it will return 'm' because array starts from 0=======

#=========Lopping through the srting ==========

for y in "UmerShahzad":
    print(y)
    
    
#===============Python String Length==================

t="umershahzad";
print(len(t))

#==================Python Check String (Whether present in a Line)===================
e="I am UmerShahzad from Pakistan";
print("Pakistan" in e)

#==============To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.==============
e="I am UmerShahzad from Pakistan";
print("pakistan" not in e) #returns true because of Capitalized 'p'.