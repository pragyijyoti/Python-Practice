
# Write a Python function that accepts two integer numbers. 
#If the product of the two numbers is less than or equal to 1000, return their product; otherwise, 
#return their sum.

def calculation():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    
    
    product=a*b
    sum=a+b
    
    if product<=1000:
        result=product
        return product
        
    else:
        result=sum
        return sum
       
       
result=calculation()
print(result)


