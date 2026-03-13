'''
Variable Swapping (The In-Place Method)

Practice Problem: Write a program to swap the values of two variables,
a and b, without using a third temporary variable.
'''

a=5
b=6
(a,b)=(b,a)
print(f"Swapped values: a={a},b={b}")