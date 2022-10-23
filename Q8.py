#Write a recursive python function to print cubes of first N natural numbers
def f1(n):
    if n==0:
        return 1
    f1(n-1)  
    print("cube of",n,"is",n**3)  
f1(9) 