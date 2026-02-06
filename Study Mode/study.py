import csv
from datetime import datetime
import time

TIME_FILE = "time.csv"

timer = 0

def log_study(study: str):
    timestamp = datetime.now().strftime("%d-%m %H:%M:%S")

    with open(TIME_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, study])



def studyMode(focus_time: int, pause_time: int):
    print("FOCUS")
    log_study("FOCUS_START")
    for remaining in range(focus_time, 0, -1):
        print(remaining)
        time.sleep(1)
    log_study("FOCUS_END")

    print("PAUSE")
    log_study("PAUSE_START")
    for remaining in range(pause_time, 0, -1):
        print(remaining)
        time.sleep(1)
    log_study("PAUSE_END")



def main():

    focus_time = int(input("How many seconds to focus for? "))
    pause_time = int(input("How many seconds to pause for? "))

    while True:
        studyMode(focus_time, pause_time)



if __name__ == "__main__":
    main()