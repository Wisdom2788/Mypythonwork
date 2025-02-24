import unittest
import expensetrackerapp

class TestExpenseTrackerMain(unittest.TestCase):
    """
    #def test_welcome_Heading(self):
      #  expected = """
     #Welcome To Semicolon Expense Tracker Application
     #______________________________________________
    #"""
     #   self.assertEqual(welcome_Heading(), expected)
    
    #def test_menu(self):
       # expected = """
      #1. Add An Expense
      #2. View All Expense
      #3. Calculate Total
     # 4. Exit
    #"""
        #self.assertEqual(menu(), expected)
    
    def test_add_expenses(self):
        Expenses = []
        test_input = {"date": "2025-02-24", "description": "Lunch", "amount": 500}
        Expenses.append(test_input)
        expected = 1
        self.assertEqual(len(Expenses), expected)
        self.assertEqual(Expenses[0]["date"], "2025-02-24")
        self.assertEqual(Expenses[0]["description"], "Lunch")
        self.assertEqual(Expenses[0]["amount"], 500)
    
    def test_view_all_expenses(self):
        Expenses = [{"date": "2025-02-24", "description": "Lunch", "amount": 500}]
        expected = "       <<< Expenses >>>   \nDate: 2025-02-24, Description: Lunch, Amount: #500\n"
        result = expensetrackerapp.view_all_expenses(Expenses)
        self.assertEqual(expected, result)
    
    def test_view_all_expenses_empty(self):
        Expenses = []
        result = expensetrackerapp.view_all_expenses(Expenses)
        expected = "Oga can't you see that expenses have not been recorded? Please add an expense."
        self.assertEqual( expected, result)
    
    def test_calculate_total_expenses(self):
        Expenses = [{"date": "2025-02-24", "description": "Lunch", "amount": 500},
                    {"date": "2025-02-25", "description": "Transport", "amount": 300}]
        result = expensetrackerapp.calculate_total_expenses(Expenses)
        expected = "Total Expenses: #800"
        self.assertEqual(expected, result)
    
    def test_calculate_total_expenses_empty(self):
        Expenses = []
        result = expensetrackerapp.calculate_total_expenses(Expenses)
        expected = "Oga, Oga, Oga there is no expense to calculate.\nPlease add an expense."
        self.assertEqual(expected, result)
    
    
    def test_invalid_date_format_floats(self):
        Expenses = [{"date": "2025.02.24", "description": "Shopping", "amount": 200}]
        expected = "2025-02-24"
        self.assertNotEqual(Expenses[0]["date"], expected)
    
    def test_amount_negative_number(self):
        Expenses = [{"date": "2025-02-24", "description": "Groceries", "amount": -100}]
        expected = -100
        self.assertEqual(Expenses[0]["amount"], expected)
    
    def test_amount_with_whitespace(self):
        Expenses = [{"date": "2025-02-24", "description": "Utilities", "amount": " 300 "}]
        expected = " 300 "
        self.assertEqual(Expenses[0]["amount"], expected)
    
    def test_amount_as_string(self):
        Expenses = [{"date": "2025-02-24", "description": "Bills", "amount": "three hundred"}]
        expected = "three hundred"
        self.assertEqual(Expenses[0]["amount"], expected)
    
    def test_description_negative_number(self):
        Expenses = [{"date": "2025-02-24", "description": -50, "amount": 300}]
        expected = -50
        self.assertEqual(Expenses[0]["description"], expected)
    
    def test_description_zero(self):
        Expenses = [{"date": "2025-02-24", "description": 0, "amount": 300}]
        expected = 0
        self.assertEqual(Expenses[0]["description"], expected)
    
    def test_description_float(self):
        Expenses = [{"date": "2025-02-24", "description": 12.5, "amount": 300}]
        expected = 12.5
        self.assertEqual(Expenses[0]["description"], expected)

if __name__ == "__main__":
    unittest.main()
