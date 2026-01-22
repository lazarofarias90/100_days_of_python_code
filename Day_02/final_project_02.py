print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percent_of_tip = float(input("How much tip would you like to give? 10, 12 or 15 "))
number_of_people = float(input("How many people to split the bill? "))

amount_of_tip = percent_of_tip * total_bill / 100
add_total_bill = total_bill + amount_of_tip
bill_to_person = add_total_bill / number_of_people

print(f"Each person should pay: ${round(bill_to_person, 2)}")