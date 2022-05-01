import re

def add_time(start_time, duration, start_day = None):

    if start_day != None:
        start_day = start_day.lower()
        start_day = start_day.capitalize()

    days_passed = 0
    output_string = ""
    is_PM = False
    weekday_dict = {
        "Sunday" : 1,
        "Monday" : 2,
        "Tuesday" : 3,
        "Wednesday" : 4,
        "Thursday" : 5,
        "Friday" : 6,
        "Saturday" : 7
    }

    if start_day != None:
        today_int = weekday_dict[start_day]
    time_list = re.split('[\:\s]+', start_time)

    duration_split = duration.split(":")

    new_hour = int(time_list[0]) + int(duration_split[0])
    new_minute = int(time_list[1]) + int(duration_split[1])
    if time_list[2] == "PM":
        new_hour += 12

    new_hour += new_minute // 60
    days_passed += new_hour // 24
    new_minute %= 60
    new_hour %= 24

    if new_hour > 11:
        new_hour -= 12
        is_PM = True
    if new_hour == 0:
        new_hour = 12

    output_string += str(new_hour) + ":"
    if new_minute < 10:
        output_string += "0"
    output_string += str(new_minute) + " "
    if is_PM is True:
        output_string += "PM"
    else:
        output_string += "AM"

    if start_day != None:
        today_int = (today_int + days_passed) % 7
        for key, value in weekday_dict.items():
            if today_int == value:
                today = key
                output_string += ", " + today
    if days_passed > 1:
        output_string += " (" + str(days_passed) + " days later)"
    elif days_passed == 1:
        output_string += " (next day)"

    return output_string

#tests
print(add_time("3:00 PM", "3:10")) #expect 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday")) #expect 2:02 PM, Monday
print(add_time("11:43 AM", "00:20")) #expect 12:03 PM
print(add_time("10:10 PM", "3:30")) #expect 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday")) #expect 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12")) #expect 7:42 AM (9 days later)
print(add_time("8:16 PM", "466:02", "tuesday")) #expect 6:18 AM, Monday (20 days later)
