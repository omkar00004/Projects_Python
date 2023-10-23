print("Welcome to tip calculator!")
bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
# tip_1=round((((float(bill)*int(tip))/100)+float(bill)) / float(people),2)
bill_plus_tip=(bill*tip)/100+bill
bill_for_each=round(bill_plus_tip/people,2)
print(f"Each person should pay : ${bill_for_each}")