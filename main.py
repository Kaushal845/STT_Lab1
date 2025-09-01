# This file is written for Lab 1
# It also has many pylint issues on purpose


def subtract(a,b): #missing space s around comma
 return a-b #bad indentation + missing spaces


def welcome(user): #no type hints
  print("Welcome " + user) #wrong indentation, no docstring


def fibonacci(n):
 if n<=1: return n #inline if
 else: 
   return fibonacci(n-1)+fibonacci(n-2) #inconsistent indent


def squares(limit): #no docstring
 for i in range(limit):print(i*i) #inline for-loop


def main():  #no docstring
  print("Fibonacci numbers:") 
  for j in range(6):print(fibonacci(j)) #inline for-loop
  welcome("Alex")
  print("Subtract 10-4 =", subtract(10,4))
  print("Squares up to 5:")
  squares(5)


main() #should use __main__ guard
