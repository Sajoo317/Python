# -*- coding: utf-8 -*-
"""Thursday13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VtkefrhQ7MstiwiI6cOqhJXIDbe-pNnR
"""

a=133
b=75
if a>b:
  print("a is greater than b")

# if statement
marks=int(input("Enter your marks:"))
if marks>40:
  print(marks, "Congratulations! You Passed.")

# if else statement
name=str(input("Name:"))
x=int(input("Enter Your Age:"))
if x>=18:
  print("Yes, You are eligible")
else:
 print("No, You are not eligible")

# elif statement
grade=int(input("Enter Your average marks:"))
if grade>=80 and grade<=100:
  print("You got an A")
elif grade<80 and grade>=70:
  print("You got B")
elif grade<70 and grade>=60:
  print("You got c")
elif grade<60 and grade>=50:
  print("You got D")
elif grade<50 and grade>=40:
  print("You got E")
else:
  print("You Failed")

# While Loop
n=1
while n<=5:
  print("Hello World!")
  n +=1

#for loop
List =['a','b','c']
for num in List:
  print(num)

alpha=['sajeel','nabeel','faizan']
for nam in alpha:
  print(nam)

# Table of 2 using while loop
n=2
while n<=20:
  print( n)
  n +=2

# Table using while Loop taking user input
a=int(input("Enter the number you want the table of:"))
i=1
while i<=10:
  print(f"{a}x{i}={a*i}") # f string
  i+=1