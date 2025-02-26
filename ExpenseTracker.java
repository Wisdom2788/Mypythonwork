import java.util.Scanner;

public class ExpenseTracker {
    static String[][] expenses = new String[100][3]; // 2D array to store Date, Description, and Amount
    static int expenseCount = 0; // Counter for number of expenses
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println(welcomeHeading());

        while (true) {
            System.out.println(menu());
            System.out.print("Select an option: ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Date: ");
                String date = scanner.nextLine();
                System.out.print("Description: ");
                String description = scanner.nextLine();
                System.out.print("Amount: ");

                try {
                    String amount = scanner.nextLine();
                    System.out.println(addExpense(date, description, amount));
                } catch (NumberFormatException e) {
                    System.out.println("\nInvalid input for amount. Please enter a number.\n");
                }
            } else if (choice.equals("2")) {
                System.out.println(viewAllExpenses());
            } else if (choice.equals("3")) {
                System.out.println(calculateTotalExpenses());
            } else if (choice.equals("4")) {
                System.out.println("Thank you for using Semicolon's ExpenseTracker App <<<<<SIIIUUUUU>>>>> ");
                break;
            } else {
                System.out.println("Oga input a valid option from the Menu.");
            }
        }
    }

    public static String welcomeHeading() {
        return """
                Welcome To Semicolon Expense Tracker Application
                ________________________________________________
                """;
    }

    public static String menu() {
        return """
                1. Add An Expense
                2. View All Expenses
                3. Calculate Total
                4. Exit
                """;
    }

    public static String addExpense(String date, String description, String amount) {
        if (expenseCount < expenses.length) {
            expenses[expenseCount][0] = date;
            expenses[expenseCount][1] = description;
            expenses[expenseCount][2] = amount;
            expenseCount++;
            return "\n<<< Expense Added Successfully >>>\n";
        } else {
            return "\nExpense list is full! Cannot add more expenses.\n";
        }
    }

    public static String viewAllExpenses() {
        if (expenseCount == 0) {
            return "Oga can't you see that expenses have not been recorded? Please add an expense.";
        }
        String result = "\n       <<< Expenses >>>   \n";
        for (int i = 0; i < expenseCount; i++) {
            result += (i + 1) + ". Date: " + expenses[i][0] +
                    ", Description: " + expenses[i][1] +
                    ", Amount: #" + expenses[i][2] + "\n";
        }
        return result;
    }

    public static String calculateTotalExpenses() {
        if (expenseCount == 0) {
            return "Oga, Oga, Oga there is no expense to calculate.\nPlease add an expense.";
        }
        int total = 0;
        for (int i = 0; i < expenseCount; i++) {
            total += Integer.parseInt(expenses[i][2]);
        }
        return "Total Expenses: #" + total;
    }
}
