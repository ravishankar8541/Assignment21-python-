# Write a recursive python function to print first N even natural numbers.
def printEven(n):
    if n==0:
        return 1
    printEven(n-1) 
    print(2*n)      
    
printEven(9) 
