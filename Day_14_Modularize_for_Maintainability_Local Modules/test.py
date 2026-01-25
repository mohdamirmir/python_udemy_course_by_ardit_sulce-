year_of_birth = int(input("Enter your year of birth: "))

def get_age(year_of_birth, current_year=2025):
    age = current_year - year_of_birth
    return age
    
age = get_age(year_of_birth)
print(age)