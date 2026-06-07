import random
import time

def print_title(title):
    width = 50
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width + "\n")


def show_menu(menu):
    for category, items in menu.items():
        border = "*" * 50
        print(f"\n{border}")
        print(f"* {category.center(46)} *")
        print(border)
        for index, item in enumerate(items, start=1):
            name = item['name']
            price = f"${item['price']}"
            print(f"  {index}. {name.ljust(34)} {price.rjust(8)}")
    print("\n" + "~" * 50 + "\n")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ["y", "yes"]:
            return True
        if answer in ["n", "no"]:
            return False
        print("Please answer with y or n.")


def pick_dish(menu):
    chosen = {}
    for category in menu:
        if not ask_yes_no(f"Would you like to order from {category}?"):
            continue

        print(f"\nChoose one or more from {category}:")
        for index, item in enumerate(menu[category], start=1):
            print(f"  {index}. {item['name']} - ${item['price']}")
        print("Enter numbers separated by commas, e.g. 1,2")

        while True:
            choice = input(f"Enter choice(s) for {category}: ")
            selected = [part.strip() for part in choice.split(",") if part.strip().isdigit()]
            selected = [int(part) for part in selected if 1 <= int(part) <= len(menu[category])]
            if selected:
                seen = set()
                unique = []
                for number in selected:
                    if number not in seen:
                        seen.add(number)
                        unique.append(number)
                chosen[category] = [menu[category][number - 1] for number in unique]
                break
            print("Invalid choice, please select at least one valid number.")
    return chosen


def pick_payment_method():
    methods = ["Cash", "Card", "QR Scanner", "Bank"]
    print("\nPayment methods:")
    for index, method in enumerate(methods, start=1):
        print(f"  {index}. {method}")

    while True:
        choice = input("Choose payment method: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(methods):
                return methods[choice - 1]
        print("Invalid choice, please enter a valid number.")


def show_processing(min_seconds=10, max_seconds=30):
    duration = random.randint(min_seconds, max_seconds)
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    print("Payment processing [   ]", end="", flush=True)
    for i in range(duration):
        symbol = spinner[i % len(spinner)]
        print(f"\rPayment processing [ {symbol} ]", end="", flush=True)
        time.sleep(1)
    print("\rPayment processing [ ✓ ]")
    print()


def process_payment(payment_method, amount_due):
    print("\n" + "~" * 50)
    print(f"Payment method: {payment_method}")

    if payment_method == "Cash":
        while True:
            amount = input(f"Enter cash received (${amount_due:.2f}): ")
            try:
                cash_received = float(amount)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if cash_received < amount_due:
                print("Amount received is less than the total due. Please enter a sufficient amount.")
                continue
            change = round(cash_received - amount_due, 2)
            print(f"Cash received: ${cash_received:.2f}")
            print(f"Change given: ${change:.2f}")
            show_processing()
            print("Payment completed in cash. Thank you for your payment!")
            break

    elif payment_method == "Card":
        bank = input("Enter your card bank name: ").strip()
        if not bank:
            bank = "your bank"
        show_processing()
        print(f"Payment successful through {bank}.")
        print("Thank you for choosing card payment!")

    elif payment_method == "QR Scanner":
        qr_code = (
            "███████       ███████\n"
            "█     █       █     █\n"
            "█ ███ █       █ ███ █\n"
            "█ █ █ █       █ █ █ █\n"
            "█ ███ █       █ ███ █\n"
            "█     █       █     █\n"
            "███████       ███████\n"
            "       █ ███ █       \n"
            "  ███  █ █   █  ███  \n"
            " █   █ █ ███ █ █ █   \n"
            " █   █   █   █ █ ███ \n"
            " ███ █ █ █ █ █ █   █ \n"
            "       █  █ █        \n"
            "███████              \n"
            "█     █              \n"
            "█ ███ █              \n"
            "█ ███ █              \n"
            "█ ███ █              \n"
            "█     █              \n"
            "███████              \n"
        )
        print("Scan this QR code to complete payment:")
        print(qr_code)
        show_processing()
        print("Payment completed via QR Scanner. Thank you!")

    elif payment_method == "Bank":
        banks = ["Bank of America", "Aathyanth funds", "books bank", "Citi", "HSBC"]
        print("\nAvailable banks:")
        for index, bank in enumerate(banks, start=1):
            print(f"  {index}. {bank}")
        while True:
            choice = input("Select your bank: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(banks):
                    selected_bank = banks[choice - 1]
                    show_processing()
                    print(f"Payment successful through {selected_bank}.")
                    print("Thank you for using our bank payment option!")
                    break
            print("Invalid choice, please enter a valid number.")

    else:
        print("Payment method not recognized.")


def main():
    menu = {
        "Starters": [
            {"name": "Bruschetta", "price": 6},
            {"name": "Soup of the Day", "price": 5},
            {"name": "Garlic Bread", "price": 4},
            {"name": "Stuffed Mushrooms", "price": 7},
            {"name": "Chicken Wings", "price": 8},
            {"name": "Fried Calamari", "price": 9},
        ],
        "Main Course": [
            {"name": "Grilled Chicken", "price": 14},
            {"name": "Pasta Alfredo", "price": 12},
            {"name": "Steak", "price": 18},
            {"name": "Salmon Fillet", "price": 16},
            {"name": "Veggie Lasagna", "price": 13},
            {"name": "Lamb Chops", "price": 20},
        ],
        "Dessert": [
            {"name": "Cheesecake", "price": 7},
            {"name": "Chocolate Brownie", "price": 6},
            {"name": "Ice Cream", "price": 5},
            {"name": "Fruit Tart", "price": 7},
            {"name": "Creme Brulee", "price": 8},
            {"name": "Tiramisu", "price": 9},
        ],
        "Today's Special": [
            {"name": "Sea Food Platter", "price": 18},
            {"name": "Pasta Bolognese", "price": 67},
            {"name": "Dream Cake", "price": 99},
            {"name": "Chef's Platter", "price": 45},
            {"name": "Spicy Curry Bowl", "price": 22},
            {"name": "Special Ramen", "price": 24},
        ],
    }

    print_title("AATHYANTH HOTEL")
    print("Welcome to AATHYANTH Hotel! Today\'s menu is ready for you.")
    show_menu(menu)

    order = pick_dish(menu)

    order_border = "#" * 50
    print(f"\n{order_border}")
    print("#" + " BILL ".center(48) + "#")
    print(order_border)

    total = 0
    categories = ["Starters", "Main Course", "Dessert", "Today's Special"]
    for category in categories:
        print(f"# {category.upper():<46} #")
        items = order.get(category, [])
        if items:
            for item in items:
                total += item["price"]
                line = f"#   {item['name']:<30} ${item['price']:>6}"
                print(line.ljust(48) + " #")
        else:
            print(f"#   {'No items selected':<38}  #")
        print("#" + "-" * 48 + "#")

    if total > 200:
        tax_rate = 0.235
    elif total > 100:
        tax_rate = 0.10
    else:
        tax_rate = 0.05

    tax_amount = round(total * tax_rate, 2)
    total_with_tax = round(total + tax_amount, 2)

    print(f"# {'Subtotal:':<16} ${total:>28.2f} #")
    print(f"# {'Tax (' + (str(int(tax_rate * 100)) if tax_rate != 0.235 else '23.5') + '%):':<16} ${tax_amount:>25.2f} #")
    print(f"# {'Total with Tax:':<16} ${total_with_tax:>24.2f} #")
    print(order_border)

    payment_method = pick_payment_method()
    process_payment(payment_method, total_with_tax)

    print("\n" + "~" * 50)
    print(" PAYMENT METHOD SELECTED ".center(50))
    print("~" * 50)
    print(f"{payment_method.center(50)}")
    print("~" * 50)

    closing_border = "#" * 62
    print("\n" + closing_border)
    print("#" + " " * 60 + "#")
    print("#" + " THANK YOU FOR DINING WITH US! ".center(60) + "#")
    print("#" + " WE APPRECIATE YOUR VISIT ".center(60) + "#")
    print("#" + " VISIT US AGAIN SOON FOR MORE DELICIOUS MEALS ".center(60) + "#")
    print("#" + " " * 60 + "#")
    print(closing_border)


if __name__ == "__main__":
    main()
