# Program to check if division is possible or not

def check_division(num,den):
    return num/den

def main():
    num=float(input("Enter numerator")) 
    den=float(input("Enter denominator"))
    if(den!=0):
        division=check_division(num,den)
        print("The result of division is {:.4f}".format(division))
    else:
        print("Division is not possible")

main()