Expense_Tracker_App = []

print("""
Welcome to Semicolon Expense Tracker App
________________________________________
""")

print("""
1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Exit
""")

while True:
    options = int(input("Enter your choice: "))

    if options == 1:
        date = str(input("Enter the date (YYYY-MM-DD): "))
        description = str(input("Description: "))
        amount = int(input("Amount: "))
        Expense_Tracker_App.append({"date": date, "description": description, "amount": amount})
        print("<<< Expense Added>>>")

    elif options == 2:
        if not Expense_Tracker_App:
            print("No expenses recorded.")
        else:
            print("\nDate| Description | Amount")
            print()
            for exp in Expense_Tracker_App:
                print(f"{exp['date']} | {exp['description']} | ${exp['amount']:.2f}")
        print()

    elif options == 3:
        total = sum(exp["amount"] for exp in Expense_Tracker_App)
        print(f"Total Expenses: ${total:.2f}")

    elif options == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, please try again.")
