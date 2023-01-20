# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 07:47:54 2023

@author: UmerShahzad
"""

#============Python Global Variables================
#====Variables that are created outside of a function (as in all of the examples above) are known as global variables.

#=====Global variables can be used by everyone, both inside of functions and outside.

#===See an Example=====
 #===Global Variable you defined outside but you used inside the function=====
global t;
t='Awesome';
def my_func():
   
    print('Python is'+t)
my_func()
    
#====Solving an Example of Local Variable=====
def num_1():
    u='Python Programming'; #=====Local Variable Only Works inside the function======
    print('Welcome to'+ u)
num_1()

#==========Python Data Types===========
#====int,float,complex,set,tuple,frozenset,dict,list,bool,byte,bytearray,memoryview,range,str=====
d='SZABIST'; #===returns the data type=====
print(type(d))

x=['C++','JAVA','C#','PHP','Perl','Dart']
print(type(x))

o={'Flask','Django','ios','Andriod','Web'}
print(type(o))

p=('Umer','Haroon','Zain','Ahmer','Maqbool')
print(type(p))

i=range(0,7)
print(type(i))

r={'name':'Umer','Age':'22'}
print(type(r))

#====Same you can do with others data types======

