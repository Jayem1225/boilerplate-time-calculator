def add_time(start, duration, day_name=None):
    DAY_NAMES = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    day_index = None
    start_time = start.split()[0]
    start_hour = int(start_time.split(":")[0])
    start_minute = int(start_time.split(":")[1])
    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])
    is_am = upper(start.split()[1]) == "AM"
    if day_name:
        day_index = DAY_NAMES.index(capitalizeday_name))
    
    # Minutes
    added_minutes = start_minute + duration_minute
    new_minute = added_minutes % 60
    # Hours
    carry_hours = int(added_minutes/60)
    added_hours = start_hour + duration_hour + carry_hours
    new_hour = added_hours % 12
    # 12 Hrs
    added_12hrs = int(added_hours/12)
    if added_12hrs % 2 == 1:
        is_am = !is_am
    # 24 Hrs
    if day_index:
        added_24hrs = int(added_hours/24)
        day_index = (day_index + added_24hrs) % 7
    
    new_time = f"{new_hour}:{new_minute} {"AM" if is_am else "PM"}"
    if day_index:
        new_time += " " + DAY_NAMES[day_index]
     
    return new_time
