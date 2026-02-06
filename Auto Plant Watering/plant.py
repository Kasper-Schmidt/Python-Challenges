import csv
import random
from datetime import datetime
import time

MEASUREMENTS_FILE = "measurements.csv"

THRESHOLD = 70

def log_measurement(dryness: int):
    timestamp = datetime.now().strftime("%d-%m %H:%M:%S")

    with open(MEASUREMENTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, dryness])

    if dryness >= THRESHOLD:
        print(f"Dryness is at {dryness}, which is over the threshold")



def increasing_dryness(current_dryness: int) -> int:
    time.sleep(1)
    current_dryness += random.randint(1, 3)
    return min(100, current_dryness) 


def watering_start(current_dryness: int) -> int:
    time.sleep(1)
    current_dryness -= random.randint(10,15)
    return max(25, current_dryness)
    


def main():
    dryness = int(input("Initial dryness: "))

    while True:
        dryness = increasing_dryness(dryness)
        print("Dryness:", dryness)
        log_measurement(dryness)

        if dryness >= THRESHOLD:
            print("Watering Started!")

            while dryness > 25:
                dryness = watering_start(dryness)
                log_measurement(dryness)

if __name__ == "__main__":
    main()
