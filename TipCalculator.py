print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would like to give? 10, 12 or 15? "))
split_person = int(input("How many people to split the bill? "))
total_with_tip = (total_bill + ((total_bill * tip)/100))/split_person
print(f"Each person should pay: ${round(total_with_tip,2)}")
