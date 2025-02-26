import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ExpenseTrackerTest {

    @Test
    public void testWelcomeHeading() {
        String expected = "\n<<< Welcome to Expense Tracker >>>\n" +
                          "__________________________________\n";
        assertEquals(expected, ExpenseTracker.welcomeHeading());
    }

    @Test
    public void testDisplayMenu() {
        String expected = "1. Add an Expense\n" +
                          "2. View All Expenses\n" +
                          "3. Get Total Expenses\n" +
                          "4. Delete an Expense\n" +
                          "5. Exit\n";
        assertEquals(expected, ExpenseTracker.displayMenu());
    }

    @Test
    public void testAddExpense() {
        // Reset state manually
        ExpenseTracker.expenseCount = 0;
        ExpenseTracker.expenses = new String[100][2];

        String result = ExpenseTracker.addExpense("Groceries", 50.0);
        assertEquals("\n<<< Expense added successfully >>>\n", result);
        assertEquals(1, ExpenseTracker.expenseCount);
        assertEquals("Groceries", ExpenseTracker.expenses[0][0]);
        assertEquals("50.0", ExpenseTracker.expenses[0][1]);
    }

    @Test
    public void testViewExpensesWhenEmpty() {
        // Reset state manually
        ExpenseTracker.expenseCount = 0;
        ExpenseTracker.expenses = new String[100][2];

        assertEquals("No expenses recorded.\n", ExpenseTracker.viewExpenses());
    }

    @Test
    public void testViewExpensesWithEntries() {
        // Reset state manually
        ExpenseTracker.expenseCount = 0;
        ExpenseTracker.expenses = new String[100][2];

        ExpenseTracker.addExpense("Groceries", 50.0);
        ExpenseTracker.addExpense("Electricity Bill", 100.0);

        String expected = "\n<<< Expenses >>>\n" +
                          "1. Groceries - $50.0\n" +
                          "2. Electricity Bill - $100.0\n";

        assertEquals(expected, ExpenseTracker.viewExpenses());
    }

    @Test
    public void testGetTotalExpenses() {
        // Reset state manually
        ExpenseTracker.expenseCount = 0;
        ExpenseTracker.expenses = new String[100][2];

        ExpenseTracker.addExpense("Groceries", 50.0);
        ExpenseTracker.addExpense("Electricity Bill", 100.0);

        assertEquals("Total Expenses: $150.0\n", ExpenseTracker.getTotalExpenses());
    }

    @Test
    public void testDeleteExpenseValid() {
        // Reset state manually
        ExpenseTracker.expenseCount = 0;
        ExpenseTracker.expenses = new String[100][2];

        ExpenseTracker.addExpense("Groceries", 50.0);
        ExpenseTracker.addExpense("Electricity Bill", 100.0);

        String result = ExpenseTracker.deleteExpense(1);
        assertEquals("Expense deleted!\n", result);
        assertEquals(1, ExpenseTracker.expenseCount);
        assertEquals("Electricity Bill", ExpenseTracker.expenses[0][0]); // Shifted up
    }

    @Test
    public void testDeleteExpenseInvalid() {
        // Reset state manually
        ExpenseTracker.expenseCount = 0;
        ExpenseTracker.expenses = new String[100][2];

        ExpenseTracker.addExpense("Groceries", 50.0);
        String result = ExpenseTracker.deleteExpense(5);
        assertEquals("Invalid expense number.\n", result);
    }
}
