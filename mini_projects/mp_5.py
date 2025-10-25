# Timer and stopwatch

import os
import time

def stopwatch_timer():
    time_mode = input("Enter H: Hours, M: Minutes, or S: Seconds: ").strip().upper()
    total_time = int(input("Enter the time duration: "))

    if "S" in time_mode:
        total_time = total_time
    elif "M" in time_mode:
        total_time *= 60
    elif "H" in time_mode:
        total_time *= 3600
    else:
        print("Sorry, the mode is not properly set.")
        return
    while total_time > -1:
        minutes, seconds = divmod(total_time, 60)
        if minutes >= 60:
            hours, minutes = divmod(minutes, 60)
            print(f" Hours: {hours:02d} Minutes: {minutes:02d} Seconds: {seconds:02d}", end="\r")
        else:
            print(f" Minutes: {minutes:02d} Seconds: {seconds:02d}                               ", end="\r")
        time.sleep(1)
        total_time -= 1

def incremental_timer():
    time_mode = input("Enter H: Hours, M: Minutes, or S: Seconds: ").strip().upper()
    total_time = int(input("Enter the time duration: "))

    if "S" in time_mode:
        total_time = total_time
    elif "M" in time_mode:
        total_time *= 60
    elif "H" in time_mode:
        total_time *= 3600
    else:
        print("Sorry, the mode is not properly set.")
        return
    counter = 0
    while counter <= total_time:
        minutes, seconds = divmod(counter, 60)
        if minutes >= 60:
            hours, minutes = divmod(minutes, 60)
            print(f" Hours: {hours:02d} Minutes: {minutes:02d} Seconds: {seconds:02d}", end="\r")
        else:
            print(f" Minutes: {minutes:02d} Seconds: {seconds:02d}                               ", end="\r")
        time.sleep(1)
        counter += 1

if __name__ == "__main__":
    while True:
        mode = int(input("Enter the mode: 1: Stopwatch, 2: Incremental Timer, 3: Exit: "))
        print()
        if mode == 1:
            stopwatch_timer()
            os.system("cls||clear")
        elif mode == 2:
            incremental_timer()
            os.system("cls||clear")
        else:
            break
        print()