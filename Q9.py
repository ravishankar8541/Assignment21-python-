###Write a recursive python function to print first N multiples of a given number.

def f1(num,n):
    
    if num==0:
        return 1;
    f1(num-1,n) 
    print(n*num)   
f1(10,int(input("Enter a number :")))
 
