import java.util.ArrayList;
import java.util.Scanner;

public class MyCheckout {
    public static void main(String... args) {
        Scanner wisdom = new Scanner(System.in);
        
        ArrayList<String> items = new ArrayList<>();
        ArrayList<Integer> quantities = new ArrayList<>();
        ArrayList<Integer> prices = new ArrayList<>();

        System.out.println("What is the customer's name: ");
        String customersName = wisdom.nextLine();

        String choice;
        do {
            System.out.println("What did the user buy: ");
            String purchase = wisdom.next();
            items.add(purchase);

            System.out.println("How many pieces: ");
            int quantity = wisdom.nextInt();
            quantities.add(quantity);

            System.out.println("How much per unit: ");
            int price = wisdom.nextInt();
            prices.add(price);

            System.out.println("Add more items? (yes/no)");
            wisdom.nextLine(); // Consume leftover newline
            choice = wisdom.nextLine();
        } while (choice.equalsIgnoreCase("Yes"));

        System.out.println("Cashier Name: ");
        String cashier = wisdom.nextLine();

        System.out.println("How much discount will the customer get?");
        double discount = wisdom.nextDouble();

        // Generate Receipt
        System.out.println("Welcome to SEMICOLON store");
        System.out.println("Main Branch");
        System.out.println("Location: 312 HERBERT MACULAY WAY, SABO YABA, LAGOS.");
        System.out.println("Tel: 07084554333");
        System.out.println("==========================================================");
        System.out.println("             ITEM         QTY      PRICE      TOTAL (NGN) ");
        System.out.println("----------------------------------------------------------");

        double grandTotal = 0;
        for (int i = 0; i < items.size(); i++) {
            double total = quantities.get(i) * prices.get(i);
            grandTotal += total;
            System.out.printf("%-15s %-10d %-10d %-10.2f%n", items.get(i), quantities.get(i), prices.get(i), total);
        }

        double discountedTotal = grandTotal - discount;

        System.out.println("----------------------------------------------------------");
        System.out.printf("Subtotal: %.2f%n", grandTotal);
        System.out.printf("Discount: -%.2f%n", discount);
        System.out.printf("Total: %.2f%n", discountedTotal);
        System.out.println("==========================================================");
        System.out.println("Thank you for shopping with us!");

        wisdom.close();
    }
}
