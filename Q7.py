#Write a recursive python function to print squares of first N natural numbers
def f1(n):
    if n==0:
        return 1
    f1(n-1)  
    print("square of",n,"is",n*n)  
f1(9)   
