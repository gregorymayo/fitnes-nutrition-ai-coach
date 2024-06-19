from chatgpt import get_chatgpt_response

def build_weekday_routine():
    wake_time = input("What time did you wake up? ")
    sleep_time = input("What time do you sleep? ")
    work_location = input("Are you working from home or office? ")
    has_meetings = input("Do you have meetings today (yes/no)? ")
    meeting_schedule = []

    if has_meetings.lower() == 'yes':
        meeting_schedule = input(
            "What time is your meeting? (separated by comma)\nExample: 10.00 - 11.00, 13.30 - 14.00\n")

    meetings_formatted = ""
    if meeting_schedule:
        meetings_formatted = f"meetings at {meeting_schedule}"

    prompt = (f"Create a healthy weekday routine for someone who wakes up at {wake_time}, "
              f"and sleeps at {sleep_time}, works from {work_location}, "
              f"and {'has ' + meetings_formatted if has_meetings.lower() == 'yes' else 'does not have meetings'}.")

    return get_chatgpt_response(prompt)

def build_weekend_routine():
    wake_time = input("What time did you wake up? ")
    sleep_time = input("What time do you sleep? ")
    prompt = f"Create a healthy weekend routine for someone who wakes up at {wake_time} and sleeps at {sleep_time}."
    return get_chatgpt_response(prompt)

def build_holiday_routine():
    days = input("How many days do you want the healthy routine to last? ")
    prompt = f"Create a healthy routine for a holiday lasting {days} days."
    return get_chatgpt_response(prompt)
