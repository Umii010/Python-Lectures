# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 07:11:54 2023

@author: UmerShahzad
"""

# ==============Simple Program to Print in Python====================
print('Welcome to Python Programming')

#==========You Can Use Double Quotes as Well It does't Affect===========
print("Welcome to the World of Programming") 

#============Python Indentation=============
#Indentation refers to the spaces at the beginning of a code line.

#Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

#Python uses indentation to indicate a block of code.

if(5>2):
    print('Five is Greater!')
    
#==========Below one Without Indentation & returns an error============
if(5>3):
print("Five is Greater")

#==============For Comment Python uses hash sign(#)==============

#=========Python Variables (Don't need to define data type)===============
x=12;
y=32;
print(x*y)

#=========Second Example============
x=98;
v='UmerShahzad';
print(x,v) #=== this line displays your result in one line while otherone on different line============
print(x)
print(v)


#=========Python Casting( it will change the data type in to others)===============
x=str(9); # this will make the 9 as take as string rather then digit.
b=float(7);#converts into float(point number)
c=int(2);#take as integar


#=====You can get the datatype of variable using type() function=======
x=12;
y='Ali';
print(type(x))
print(type(y))

