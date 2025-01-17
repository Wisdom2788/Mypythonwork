import re
from datetime import date

def main():
    items = []
    quantities = []
    prices = []

    customers_name = input("What is the customer's name: ")
    while not re.match(r'^[a-zA-Z\s]+$', customers_name):
        print("Oga input a valid name")
        customers_name = input("What is the customer's name: ")

    while True:
        purchase = input("What did the user buy: ")
        while not re.match(r'^[a-zA-Z\s]+$', purchase):
            print("Oga input a valid item")
            purchase = input("What did the user buy: ")
        items.append(purchase)

        try:
            quantity = int(input("How many pieces: "))
            while quantity < 0:
                print("Please input a valid quantity:")
                quantity = int(input("How many pieces: "))
            quantities.append(quantity)

            price = int(input("How much per unit: "))
            while price < 0:
                print("Please input a valid price:")
                price = int(input("How much per unit: "))
            prices.append(price)
        except ValueError:
            print("Please input valid numbers for quantity and price.")
            continue

        choice = input("Add more items? (yes/no): ").strip().lower()
        while choice not in ("yes", "no"):
            print("Please behave yourself and type 'yes' or 'no':")
            choice = input("Add more items? (yes/no): ").strip().lower()

        if choice == "no":
            break

    cashier = input("Cashier Name: ")

    try:
        discount = float(input("How much discount will the customer get? (%): "))
        while discount < 0 or discount > 100:
            print("Please enter a valid discount percentage:")
            discount = float(input("How much discount will the customer get? (%): "))
    except ValueError:
        print("Invalid discount input. Setting discount to 0.")
        discount = 0

    current_date = date.today()

    print("===============================================================")
    print("Welcome to SEMICOLON store")
    print("Main Branch")
    print("Location: 312 HERBERT MACULAY WAY, SABO YABA, LAGOS.")
    print("Tel: 07084554333")
    print(f"Date: {current_date}")
    print(f"Customer's Name: {customers_name}")
    print("===============================================================")
    print("            ITEM         QTY      PRICE      TOTAL (NGN) ")
    print("---------------------------------------------------------------")

    grand_total = 0
    for item, quantity, price in zip(items, quantities, prices):
        total = quantity * price
        grand_total += total
        print(f"{item:<15} {quantity:<10} {price:<10} {total:<10.2f}")

    discount_amount = (discount / 100) * grand_total
    vat = 0.175 * grand_total
    bill_total = grand_total - discount_amount + vat

    print("---------------------------------------------------------------")
    print(f"\t\tSubtotal: {grand_total:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"VAT @ 17.50%: {vat:.2f}")
    print("===============================================================")
    print(f"Bill Total: {bill_total:.2f}")
    print("===============================================================")
    print(f"This is not a receipt. Kindly pay: {bill_total:.2f}")
    print("===============================================================")

    try:
        cash_paid = float(input("How much did the customer give to you: "))
        while cash_paid < bill_total:
            print("Insufficient amount! oga input correct amount make i no swear for you:")
            cash_paid = float(input("How much did the customer give to you: "))
    except ValueError:
        print("Invalid input. Setting cash paid to 0.")
        cash_paid = 0

    balance = cash_paid - bill_total

    print("===============================================================")
    print("Welcome to SEMICOLON store")
    print("Main Branch")
    print("Location: 312 HERBERT MACULAY WAY, SABO YABA, LAGOS.")
    print("Tel: 07084554333")
    print(f"Date: {current_date}")
    print(f"Customer's Name: {customers_name}")
    print("===============================================================")
    print("             ITEM         QTY      PRICE      TOTAL (NGN) ")
    print("---------------------------------------------------------------")

    for item, quantity, price in zip(items, quantities, prices):
        total = quantity * price
        print(f"{item:<15} {quantity:<10} {price:<10} {total:<10.2f}")

    print(f"\t\tSubtotal: {grand_total:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"VAT @ 17.50%: {vat:.2f}")
    print("===============================================================")
    print(f"Bill Total: {bill_total:.2f}")
    print(f"Amount Paid: {cash_paid:.2f}")
    print(f"Balance: {balance:.2f}")
    print("===============================================================")
    print("Thanks for Shopping with us, oya come dey go")

if __name__ == "__main__":
    main()
