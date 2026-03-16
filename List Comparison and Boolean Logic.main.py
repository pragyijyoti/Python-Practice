
# List Comparison and Boolean Logic


#Practice Problem: Write a function to return True if the first and last number of a given list is the same. 
#If the numbers are different, return False.

def comparision (nums):
    if nums[0]==nums[-1]:
        return True
    else:
        return False
        
print(comparision("2,3,4,5,2"))
print(comparision("3,6,9,12"))
    