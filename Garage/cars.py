import csv
import re


PARKED_FILE = "parked.csv"
REMOVED_FILE = "removed.csv"


garage = []


def car_already_parked(plate: str) -> bool:
    try:
        with open(PARKED_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader: 
                if row and row[0].upper() == plate:
                    return True
    except FileNotFoundError:
        return False
    
    return False


def park_car():
    your_car = input("Whats is you licensplate? ").strip().upper()

    if not re.match(r"^[A-Z]{2}\d{5}$", your_car):
        print("Invalid licensplate format. (must be 2 letters followed by 5 numbers)")
        return

    if car_already_parked(your_car):
        print("Your car is already parked")
        return

    # Append bil til parked.csv
    with open(PARKED_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([your_car])

    print(f"car with licensplate {your_car} has been parked")


def remove_car():
    your_car = input("Whats is you licensplate? ").strip().upper()

    # 1. Læs alle parkerede biler fra PARKED_FILE
    parked = []
    try:
        with open(PARKED_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    parked.append(row[0].strip().upper())
    except FileNotFoundError:
        print("No cars have been parked")
        return

    # 2. Tjek om bilen findes i listen
    if your_car not in parked:
        print("Your car is not found")
        return
    
    # 3. Fjern bilen fra listen
    parked.remove(your_car)

    # 4. Overskriv PARKED_FILE med de resterende biler
    with open(PARKED_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for plate in parked:
            writer.writerow([plate])
    
    # 5. Append din bil til REMOVED_FILE
    with open(REMOVED_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([your_car])

    print(f"Your car with licensplate {your_car} has been retrieved")


def show_all_cars():
    try:
        with open(PARKED_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    print(row[0])

    except FileNotFoundError:
        print("No cars have been parked")


def main():
    while True:
        print("\n1) Park car")
        print("2) Retrieve car")
        print("3) Show all cars")
        print("4) Quit")

        choice = input("Choose: ").upper()

        if choice == "1":
            park_car()
        elif choice == "2":
            remove_car()
        elif choice == "3":
            show_all_cars()
        elif choice == "4":
            break
        else:
            print("Please choose 1 or 2")


if __name__ == "__main__":
    main()