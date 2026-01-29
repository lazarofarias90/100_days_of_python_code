def life_in_weeks(age):
   
    calculated_age = (90 - int(age)) * 52
    print(f"You have {calculated_age} weeks left")

real_age = input("How old are you? ")
life_in_weeks(real_age)