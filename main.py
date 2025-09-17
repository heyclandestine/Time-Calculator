days_of_week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday"
]

def add_time(start, duration, day=None):
    og_start = start
    int_start = ""
    for char in start:
        if char == " ":
            break
        int_start += char
    print("Initial AM or PM: ", f"{start[-2]}M")


    start = int_start.split(':')
    duration = duration.split(':')

    if int(start[0]) == 12:
        times_passed_twelve = -1
    else:
        times_passed_twelve = 0

    start = int(start[0])*60 + int(start[1])
    print("Start: ", start)
    duration = int(duration[0])*60 + int(duration[1])
    print("Duration: ", duration)
    count = start + duration
    print("SUM OF START AND DURATION: ", count)


    while count > 720:
        count -= 720
        times_passed_twelve += 1
    print("Revised Count: ", count)
    print("Times passed 12:00: ", times_passed_twelve)
    if count // 60 == 0:
        hours = 12
    else:
        hours = count // 60
    minutes = count % 60

    if minutes < 10:
        raw_time = str(hours) + ':' + "0" + str(minutes)
    else:
        raw_time = str(hours) + ':' + str(minutes)

    print("RAW TIME: ", raw_time)

    if times_passed_twelve % 2 == 0 and og_start[-2] == "P":
        raw_time += " PM"
    if times_passed_twelve % 2 == 1 and og_start[-2] == "P":
        raw_time += " AM"
    
    if times_passed_twelve % 2 == 0 and og_start[-2] == "A":
        raw_time += " AM"
    if times_passed_twelve % 2 == 1 and og_start[-2] == "A":
        raw_time += " PM"

    print("RAW TIME: ", raw_time)

    new_time = ""
    days_elapsed = 0

    if day != None:
        current_day_index = days_of_week.index(day.lower())
        print("Current Day Index: ", current_day_index, f"({days_of_week[current_day_index].capitalize()})")
    


    if og_start[-2] == "P" and (times_passed_twelve == 1 or times_passed_twelve == 2):
        days_elapsed = 1
        movement_in_index = days_elapsed % 7
        if day != None:
            if movement_in_index + current_day_index > 6:
                current_day_index = movement_in_index + current_day_index - 7
            else:
                current_day_index += movement_in_index
    elif og_start[-2] == "P" and times_passed_twelve > 2:
        days_elapsed = 1
        while times_passed_twelve > 2:
            times_passed_twelve -= 2
            days_elapsed += 1
        movement_in_index = days_elapsed % 7
        print("Movement in index: ", movement_in_index)
        if day != None:
            if movement_in_index + current_day_index > 6:
                current_day_index = movement_in_index + current_day_index - 7
            else:
                current_day_index += movement_in_index
            print(days_of_week[current_day_index])






    if og_start[-2] == "A" and (times_passed_twelve == 2 or times_passed_twelve == 3):
        days_elapsed = 1
        movement_in_index = days_elapsed % 7
        if day != None:
            if movement_in_index + current_day_index > 6:
                current_day_index = movement_in_index + current_day_index - 7
            else:
                current_day_index += movement_in_index
    elif og_start[-2] == "A" and times_passed_twelve > 3:
        days_elapsed = 1
        while times_passed_twelve > 3:
            times_passed_twelve -= 2
            days_elapsed += 1
        movement_in_index = days_elapsed % 7
        print("Movement in index: ", movement_in_index)
        if movement_in_index + current_day_index > 6:
            current_day_index = movement_in_index + current_day_index - 7
        else:
            current_day_index += movement_in_index
        print(days_of_week[current_day_index])





    print("Days Elapsed: ", days_elapsed)

    if days_elapsed > 1 and day != None:
        new_time = raw_time + f", {days_of_week[current_day_index].capitalize()} ({days_elapsed} days later)"
        return new_time
    if og_start[-2] == "A" and (times_passed_twelve == 2 or times_passed_twelve == 3) and day != None:
        new_time = raw_time + f", {days_of_week[current_day_index].capitalize()} (next day)"
        return new_time      
    if og_start[-2] == "P" and (times_passed_twelve == 1 or times_passed_twelve == 2) and day != None:
        new_time = raw_time + f", {days_of_week[current_day_index].capitalize()} (next day)"
        return new_time
    if day != None:
        new_time = raw_time + f", {days_of_week[current_day_index].capitalize()}"
        return new_time
    elif days_elapsed > 1:
        new_time = raw_time + f" ({days_elapsed} days later)"
        return new_time
    elif days_elapsed == 1:
        new_time = raw_time + f" (next day)"
        return new_time
    else:
        new_time = raw_time
        return new_time
   

print(add_time('2:59 AM', '24:00', 'saturDay'))