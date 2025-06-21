

#task 1
def factorial(n):
    if  n < 2 :
        return 1
    else:
        return n * (factorial(n-1))
number=float(input("Enter the number:"))
print(f"The factorial of {number} is {factorial(number)}")


#task 2
import math
number = float(input("Enter the number:"))
print("Square root :",math.sqrt(number))
print("logarithm :",math.log(number))
print("sine:",math.sin(number))












