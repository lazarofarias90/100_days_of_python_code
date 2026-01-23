print("Welcome to the body mass calculator.")

weight = int(input("Put your weight here: "))
height = float(input("Enter your height here: "))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")