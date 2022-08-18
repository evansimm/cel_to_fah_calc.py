#!/usr/bin/env python3
#Celsius to Fahrenheit Calculator
#This app will take the temperature as an input in Celsius and converts it to Fahrenheit. I made a program like this years ago in Java and wanted to do it again in python.

Cel = input("Please enter temperature in Celsius: ")
Fah = int(Cel) * 9/5 + 32
Temp = str(Fah)
print("The temperature is " + Temp + " degrees Fahrenheit.")