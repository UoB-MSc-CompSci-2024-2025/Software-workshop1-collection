import csv
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime


def user_message(message):
    print(message)


def spacer():
    print()


def flight_schedule(first=False) -> dict:
    schedule = {}

    if first:
        user_message("Flight schedule loaded.....")

    with open("pilot_data.csv", 'r') as pilot_data:
        for pilot_details in pilot_data.readlines():
            pilot_details_row_to_list = pilot_details.split(';')
            schedule[f"pilot{pilot_details_row_to_list[0]}"] = {
                "name": pilot_details_row_to_list[1].strip(),
                "flight_id": pilot_details_row_to_list[2].strip(),
                "coord": pilot_details_row_to_list[3].strip(),
                "start_time": pilot_details_row_to_list[4].strip(),
                "end_time": pilot_details_row_to_list[5].strip(),
            }
            if not first:
                print(
                    f"Pilot pilot{pilot_details_row_to_list[0]} name is {pilot_details_row_to_list[1]}"
                    f" they are scheduled to fly on {pilot_details_row_to_list[4]}.")

    spacer()
    return schedule


def display_flight_time(schedule: dict):
    pilot_id = input("Type the pilot id for the start date/time are you wanting to see?").strip().lower()
    found_pilot = False
    if not schedule:
        user_message("The schedule are currently not available!")
        return

    for pilot_details_key, pilot_details in schedule.items():
        if pilot_id == pilot_details_key.lower():
            print(f"{pilot_details['name']} has a scheduled flight for {pilot_details['start_time']}")
            found_pilot = True

    if not found_pilot:
        user_message('Sorry, pilot does not exist / scheduled')

    spacer()


def validate_time(check_in_time: str) -> bool:
    try:
        return bool(datetime.strptime(check_in_time, "%H:%M:%S"))
    except ValueError:
        print("Invalid time format")
        return False


def check_in(pilot_id: str, schedule: dict, time_checked_in: str):
    schedule_time = ""
    if not pilot_id or not check_for_pilots(pilot_id, schedule):
        user_message("Enter valid pilot id")
        return
    else:
        pilot_id = pilot_id.strip()
        schedule_time = schedule[pilot_id]['start_time'].split()[1]

    if datetime.strptime(time_checked_in, '%H:%M:%S') < datetime.strptime(schedule_time, '%H:%M:%S'):
        user_message("You have checked in successfully")
        spacer()
    else:
        logging_late_check_in(pilot_id)


def logging_late_check_in(pilot_id: str):
    msg = "checked in late"
    write_data = [pilot_id, msg]
    with open('late_checkin.csv', 'a') as late_checkin_date:
        writer_csv = csv.writer(late_checkin_date, delimiter=';')
        writer_csv.writerow(write_data)
        user_message('You logged in late')


# Haversine formula to calculate distance between two sets of coordinates (in kilometers) - almost completed for you
def haversine(coord1: str, coord2: str) -> float:
    lat1, lon1 = map(float, coord1.split(","))
    lat2, lon2 = map(float, coord2.split(","))

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    R = 6371  # Radius of Earth in kilometers
    distance = R * c

    return distance


def check_for_pilots(pilot_id, schedule: dict):
    found_pilot = False
    for pilot_details_key, pilot_details in schedule.items():
        if pilot_id == pilot_details_key.lower():
            found_pilot = True

    return found_pilot


def get_flight_id(pilot_ids, schedule: dict):
    flight_ids = []
    for pilot_details_key, pilot_details in schedule.items():
        for pId in pilot_ids:
            if pId == pilot_details_key.lower():
                flight_ids.append(pilot_details['flight_id'])
    return tuple(flight_ids)


def get_coordinate(pilot_ids, schedule: dict):
    coordinate = []
    for pilot_details_key, pilot_details in schedule.items():
        for pId in pilot_ids:
            if pId == pilot_details_key.lower():
                coordinate.append(pilot_details['coord'])
    return tuple(coordinate)


def get_flight_times(pilot_ids, schedule: dict):
    flight_times = []
    for pilot_details_key, pilot_details in schedule.items():
        for pId in pilot_ids:
            if pId == pilot_details_key.lower():
                flight_times.append(pilot_details['start_time'].split()[1])
    return tuple(flight_times)


def detect_conflict(pilot1: str, pilot2: str, schedule: dict):
    if not check_for_pilots(pilot1, schedule) or not check_for_pilots(pilot2, schedule):
        user_message("Sorry, pilot does not exist")
        return

    coord1, coord2 = get_coordinate([pilot1, pilot2], schedule)
    flightId1, flightId2 = get_flight_id([pilot1, pilot2], schedule)
    start_time1, start_time2 = get_flight_times([pilot1, pilot2], schedule)

    distance = haversine(coord1, coord2)

    if distance <= 500 and (start_time1 == start_time2):
        user_message(f"Conflict detected between pilot pilot1 (Flight {flightId1}) "
                     f"and pilot pilot2 (Flight {flightId2}) "
                     f"at {coord1}. Distance {distance:.2f} Km")
    else:
        user_message("No conflict detected")


def main():
    schedule = flight_schedule(first=True)
    try:
        while True:
            choice = int(input("Flight Control & Scheduling of Pilots\n"
                               "1. Show flight schedule\n"
                               "2. Check flight start time for a pilot\n"
                               "3. Pilot check in\n"
                               "4. Detect conflict for flights\n"
                               "5. Exit\n"))
            match choice:
                case 1:
                    schedule = flight_schedule(first=False)
                case 2:
                    display_flight_time(schedule)
                case 3:
                    pilot_id = input("Please enter the pilot's id for check in")
                    check_in_time = input("What time are they checking in?")
                    validated = validate_time(check_in_time)

                    if validated:
                        check_in(pilot_id, schedule, check_in_time)
                    else:
                        user_message(
                            "The time that you have entered is not in the correct format. Enter it as HH:MM:SS")

                case 4:
                    pilot_id1 = input("Please enter the pilot's id")
                    pilot_id2 = input("Please enter the second pilot's id")
                    detect_conflict(pilot_id1, pilot_id2, schedule)
                case 5:
                    break
                case _:
                    print("Incorrect choice entered")

    finally:
        return


if __name__ == '__main__':
    main()
