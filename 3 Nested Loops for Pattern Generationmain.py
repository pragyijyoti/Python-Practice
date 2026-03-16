
'''3 Nested Loops for Pattern Generation

Practice Problem: Print the following pattern where each row contains a number repeated a specific number
of times based on its value.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()
        