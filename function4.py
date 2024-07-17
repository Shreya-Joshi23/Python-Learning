# Program to reverse an integer

def reverse_integer(n):
    reversed_num=0
    while n>0:
        digit=n%10
        reversed_num=reversed_num*10+digit
        # using single / will give infinity i.e shows incorrect results bcoz n becomes float after first iteration and n=n/10 gives too large number so use // which will perform integer division and ensures n remains an integer
        n=n//10

    return reversed_num

num=int(input("Enter the integer"))
reversed_number=reverse_integer(num)
print("Reversed number:",reversed_number)