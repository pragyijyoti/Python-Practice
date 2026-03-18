
# Integer Digit Extraction and Reversal

#Practice Problem: Write a program to extract each digit from an integer in the reverse order.

number=3569
while number>0:
    digit=number%10
    print(digit, end="")
    number=number//10