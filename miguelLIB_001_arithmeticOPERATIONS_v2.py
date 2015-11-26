#!/usr/bin/python

#**************************
#IMPORTS
import sys

#**************************
#USER(string)
x = input("INSERT A VALUE X: \n")
y = input("INSERT A VALUE Y: \n")
sumUser = input("INSERT A VALUE SUM: \n")

#CONVERT(int)
convertX = int(x)
convertY = int(y)
convertSumUser = int(sumUser)

#OPERATION (+, -, *, /, %, **, //)
sumPython = convertX + convertY

#CONDITIONS AND PRINT
print("")
if ( convertSumUser  == sumPython ) : 
    print ("VALUES : " + "x = " + '{}'.format(convertX) + "; " + "y = " + '{}'.format(convertY) + "; ")
    print ("OPERATION : " + '{} '.format(convertX) + "+ " + '{} '.format(convertY) + "= " + '{} '.format(sumPython) )
    print ("CONGRATS!!! THAT IS THE SPIRIT!!!")
else :
    print ("sumUser = " + '{} '.format(convertSumUser) + "; sumPython = " + '{} '.format(sumPython) )
    print ("NOT CORRECT... TRY AGAIN...")

#**************************
#SUCCESS
print ("\nENDING APPLICATION!!")