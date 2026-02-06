import csv

FILE_NAME = "expenses.csv"

def add_expense():
    item = input("What did you buy? ").strip()
    amount = float(input("How much? ").strip())

    # Append en række til csv fil
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([item, amount])

    print("Item added")


def read_expenses(): 
    expenses = []
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                item = row[0]
                amount= float(row[1])
                expenses.append({"item": item, "amount": amount})
    except FileNotFoundError:
        pass

    return expenses


def show_total():
    expenses = read_expenses()
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: {total:.2f}")


def show_all():
    expenses = read_expenses()
    if not expenses:
        print("No expenses yet")
        return
    
    for e in expenses:
        print(f"{e["item"]}: {e["amount"]:.2f}")


def main():
    while True:
        print("\n1) Add expense")
        print("2) Show total")
        print("3) Show all")
        print("4) Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_total()
        elif choice == "3":
            show_all()
        elif choice == "4":
            break
        else: 
            print("Try 1 - 4")


if __name__ == "__main__":
    main()