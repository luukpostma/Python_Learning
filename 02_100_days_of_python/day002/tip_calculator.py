print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip_value = input("How much tip would you like to give? 10, 12 or 15? ")
people = input("How man people to split the bill? ")

total_tip = float(tip_value) / 100 + 1
total_bill = float(bill) * float(total_tip) / int(people)

print("Each person should pay: $", round(total_bill, 2))
