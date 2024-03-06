from datetime import datetime
import time

def set_reminder():
    print("What am I reminding you about?")
    text = str(input())

    print("At what time(HH:MM:SS)")
    time_of_day = str(input())

    print("What day? YYYY-MM-DD")
    day = str(input())

    # Combine date and time and format it to ISO format
    reminder_datetime = datetime.strptime(day + " " + time_of_day, '%Y-%m-%d %H:%M:%S')
    return reminder_datetime, text

def check_reminders(reminders):
    now = datetime.now()
    for reminder in reminders:
        if now >= reminder[0]:
            print("Reminder:", reminder[1])
            reminders.remove(reminder)

def main():
    reminders = []
    reminder_datetime, text = set_reminder()
    reminders.append((reminder_datetime, text))
    print("Reminder set for:", reminder_datetime,": ", text)

    while True:
        check_reminders(reminders)
        time.sleep(15)  # Check reminders every 15 seconds

if __name__ == "__main__":
    main()
