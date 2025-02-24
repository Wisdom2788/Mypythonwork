def welcome_Heading():
    return """
     Welcome To Semicolon Expense Tracker Application
     ________________________________________________
    """
    

def menu():
    return """
      1. Add An Expense
      2. View All Expense
      3. Calculate Total
      4. Exit
    """
    

def add_expenses(Expenses):
    date = str(input("Date: "))
    description = str(input("Description: "))
    amount = int(input("Amount: "))
    Expense_Tracker = {"date": date, "description": description, "amount": amount}
    Expenses.append(Expense_Tracker)
    return "\n<<< Expense Added Successfully >>>"

def view_all_expenses(Expenses):
    if Expenses:
        result = "       <<< Expenses >>>   \n"
        for Expense_Tracker in Expenses:
            result += f"Date: {Expense_Tracker['date']}, Description: {Expense_Tracker['description']}, Amount: #{Expense_Tracker['amount']}\n"
        return result
    else:
        return "Oga can't you see that expenses have not been recorded? Please add an expense."

def calculate_total_expenses(Expenses):
    if Expenses:
        total = sum(Expense_Tracker['amount'] for Expense_Tracker in Expenses)
        return f"Total Expenses: #{total}"
    else:
        return "Oga, Oga, Oga there is no expense to calculate.\nPlease add an expense."

def main():
    Expenses = []
    
    print(welcome_Heading())
    
    while True:
        print(menu())
        menu_selection = input("Select an option: ")
        
        if menu_selection == "1":
            print(add_expenses(Expenses))
             
        elif menu_selection == "2":
            print(view_all_expenses(Expenses))
            
        elif menu_selection == "3":
            print(calculate_total_expenses(Expenses))
            
        elif menu_selection == "4":
            print("Thank you for using Semicolon's ExpenseTracker App <<<<<SIIIUUUUU>>>>>")
            break
            
        else:
            print("Oga input a valid option from the Menu") 
            
main()
