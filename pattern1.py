# Fibbonacci sequence

def printfib(n):
    a,b=0,1
    count=1
    while count<=n:
        print(a,end=' ')
        #  a and b are updated at the same time, preserving the correct sequence. This simultaneous assignment in Python allows both values to be updated based on their previous states without interfering with each other.
        a,b=b,a+b
        count+=1
        

num=int(input("Enter the number of terms"))
printfib(num)


