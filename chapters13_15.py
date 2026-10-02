from datetime import date, datetime

#13.1
today = date.today()
today_text = today.isoformat()

with open("today.txt", "w") as file:
    file.write(today_text)

print("13.1 - Date written to today.txt:")
print(today_text)

# 13.2
with open("today.txt", "r") as file:
    today_string = file.read()

print("\n13.2 - today_string:")
print(today_string)


# 13.3
parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()

print("\n13.3 - Parsed date:")
print(parsed_date)

# 15.1
import multiprocessing
import random
import time
from datetime import datetime


def show_time():
    wait_time = random.random()
    time.sleep(wait_time)

    print(
        "Process waited",
        round(wait_time, 2),
        "seconds. Current time:",
        datetime.now().strftime("%H:%M:%S")
    )


if __name__ == "__main__":
    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=show_time)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
