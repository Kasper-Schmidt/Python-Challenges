def main():
    amount_persons = int(input("How many people? "))
    amount_to_pay = float(input("How much is the bill? "))

    if amount_persons <= 0:
        print("Number of people must be at least 1.")
        return

    per_person = average_pay(amount_to_pay, amount_persons)
    print(f"Each person pays: {per_person:.2f}")


def average_pay(amount_to_pay: float, amount_persons: int) -> float:
    return amount_to_pay / amount_persons


if __name__ == "__main__":
    main()
