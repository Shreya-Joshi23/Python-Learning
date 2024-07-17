# print x power n

def findpower(x,n):
    i=1
    result=1
    while i <= n :
        result*=x
        i+=1

    return result


x=int(input("Enter the value of which to find power"))
n=int(input("Enter the value of how much power"))

power=findpower(x,n)
# x=x/2
print(f"{x} power {n} is {power}")




