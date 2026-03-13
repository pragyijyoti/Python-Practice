'''
Vowel Frequency Counter

Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u)
present in a given sentence.
'''

words="i love google"
vowel="aeiou"
count=0

for word in words:
    if word in vowel:
        count+=1
        
print(f"Number of vowels:{count}")
