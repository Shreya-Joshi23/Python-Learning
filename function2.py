# Program to print multiplication table

def multiplication_table(n):
    for i in range(1,11,1):
        print(f"{n} * {i} = {n*i}")


n=int(input("Enter the number to print table"))
multiplication_table(n)