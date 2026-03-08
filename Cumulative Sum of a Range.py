
# Iterate through the first 10 numbers (0–9).In each iteration, print the current number, the previous number, and their sum.
previous_num=0
for i in range (10):
    print(f"Current number {i} previous num: {previous_num} Sum:{i+previous_num}")

    previous_num=i
print("End")
    
