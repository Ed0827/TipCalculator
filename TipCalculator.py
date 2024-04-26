print("Welcome to the tip calculator")
bill = input("What was the total bill?")
tip = input("How much tip would you like to give?")
num_people = input("How many people to split the bill")

tip_calculator = (float(bill) / 100) * float(tip)
total_cost = (float(bill) + float(tip_calculator)) / float(num_people)

print(f"Each person should pay: {round(total_cost, 2)}")
