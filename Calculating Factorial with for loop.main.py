'''
Calculating Factorial with a Loop


Practice Problem: Write a program that calculates the factorial of a given number 
(e.g., 5!) using a for loop.
'''

num=5
for i in range(1,num+1):
    factorial=num*i
    
print("Factorial of",num,"is:",factorial)