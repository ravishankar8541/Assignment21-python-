# Write a recursive python function to print first N odd natural numbers
def printOdd(n):
    if n==0:
        return 1
    printOdd(n-1)   
    print(2*n-1) 
printOdd(9)    