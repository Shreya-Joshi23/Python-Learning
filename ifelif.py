# Checking age criteria

def check_agecriteria(age):
    if age<18:
        return "Minor"
    elif 18<=age<=65:
        return "Adult"
    else:
        return "Senior"
    
age=int(input("Enter your age"))
print(check_agecriteria(age))
