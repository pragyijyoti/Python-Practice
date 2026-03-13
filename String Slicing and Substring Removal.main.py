'''
String Slicing and Substring Removal

Practice Problem: Write a function to remove characters from a string starting 
from index 0 up to n and return a new string.
'''

def remove_char(word,n):
    new=word[:n]
    return new
    
print(remove_char("python",3))