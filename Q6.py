"""Write a recursive python function to print first N even natural numbers in reverse
order."""
def printEven(n):
    if n==0:
        return 1
    print(2*n)         
    printEven(n-1)  
printEven(9) 

