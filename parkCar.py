garage = []

def park_car():
    your_car = input("Whats is you licensplate? ").upper()

    if your_car not in garage:
        garage.append(your_car)
        print(f"car with licensplate {your_car} has been parked")


def remove_car():
    your_car = input("Whats is you licensplate? ").upper()

    if your_car in garage:
        garage.remove(your_car)
    
    print(f"car with licensplate {your_car} has been retrieved")



def show_all_cars():
    print(garage)


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