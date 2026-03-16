
# Filtering Lists with Conditional Logic
#Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.
    
mylist=[3,5,7,9,15,30,60,90,99]
newlist=[]
for num in mylist:
    if num%5==0:
        newlist.append(num)
    
print(newlist)