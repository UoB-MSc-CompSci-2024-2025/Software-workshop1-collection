import csv
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime


def flight_schedule(first=False) -> dict:
    schedule = {}

    """
    insert code here as per instructions 
    """

    return schedule


def display_flight_time(schedule: dict):
    pilot_id = input("Type the pilot id for the start date/time are you wanting to see?")

    """
    insert code here as per instructions 
    """


def validate_time(check_in_time: str) -> bool:
    try:
        # complete the call to strptime() on the next line
        datetime.strptime()
        print("Time is valid")
        return True
    except ValueError:
        print("Invalid time format")
        return False


def check_in(pilot_id: str, schedule: dict, time_checked_in: str):
    print()  # remove this line once you start coding

    """
    insert code here to determine the hour for time_checked_in and the start time of the flight - as per instructions
    """


def logging_late_check_in(pilot_id: str):
    msg = "checked in late"

    """
    insert code here as per instructions 
    """


# Haversine formula to calculate distance between two sets of coordinates (in kilometers) - almost completed for you
def haversine(coord1: str, coord2: str) -> float:
    lat1, lon1 = 0.0, 0.0
    lat2, lon2 = 0.0, 0.0

    """
    Replace the 0.0, 0.0 above with the map() to convert the lat/lon from a string to a float
    map function -> map(float, split())
    """

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    R = 6371  # Radius of Earth in kilometers
    distance = R * c

    return distance


def detect_conflict(pilot1: str, pilot2: str, schedule: dict):
    coord1, coord2 = schedule[pilot1]['coord'], schedule[pilot2]['coord']
    flightId1, flightId2 = '', ''
    start_time1, start_time2 = '', ''

    """
    insert code here as per instructions to find pilot flight coordinates, flight id and start times
    """

    distance = haversine(coord1, coord2)

    """
    insert code here as per instructions to show whether there is conflict between the pilots
    """


def main():
    schedule = flight_schedule(first=True)
    while True:
        choice = int(input("Flight Control & Scheduling of Pilots\n"
                           "1. Show flight schedule\n"
                           "2. Check flight start time for a pilot\n"
                           "3. Pilot check in\n"
                           "4. Detect conflict for flights\n"
                           "5. Exit\n"))
        match choice:
            case 1:
                flight_schedule(first=False)
            case 2:
                display_flight_time(schedule)
            case 3:
                pilot_id = input("Please enter the pilot's id for check in")
                check_in_time = input("What time are they checking in?")
                validated = validate_time(check_in_time)
                """
                complete the if/else code here to give an error if time is invalid or call check_in() 
                the check_in() can be seen here below these comments
                """
                check_in(pilot_id, schedule, check_in_time)
            case 4:
                pilot_id1 = input("Please enter the pilot's id")
                pilot_id2 = input("Please enter the second pilot's id")
                detect_conflict(pilot_id1, pilot_id2, schedule)
            case 5:
                break
            case _:
                print("Incorrect choice entered")


if __name__ == '__main__':
    main()
