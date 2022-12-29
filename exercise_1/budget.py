print("my budget")
#all figure monthly
income = 1000
coffee = 2.5 * 5 * 4
#coffee 5 days per week, 4weeks per monthly
milk = 1.5 * 3 * 4
#milk 3 days per week, 4weeks per monthly
print(f"my available income per month is ${income}")
total_expense = int(coffee + milk)
print(f"my expenditure per month is ${total_expense}")
cash_left = income - total_expense
print(f"this leaves me with $", cash_left)
