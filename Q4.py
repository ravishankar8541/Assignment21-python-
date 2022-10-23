# Write a recursive python function to print first N odd natural numbers in reverse order
def printOdd(n):
    if n==0:
        return 1
    print(2*n-1)     
    printOdd(n-1)   
    
printOdd(9) 