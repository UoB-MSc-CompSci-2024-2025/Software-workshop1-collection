import csv
from datetime import datetime


def user_message(message):
    print(message)


def zoo_info(first=False):
    zoo_info = {}

    if first:
        user_message("Zoo information loaded.....")

    with open("zoo_schedule.csv", 'r') as zoo_schedule:
        for each_schedule in zoo_schedule.readlines():
            each_schedule_row_to_list = each_schedule.split(';')
            zoo_info[f"{each_schedule_row_to_list[0]}"] = {
                "name": each_schedule_row_to_list[1].strip(),
                "enclosure": each_schedule_row_to_list[2].strip(),
                "feedAm": each_schedule_row_to_list[3].strip(),
                "feedPm": each_schedule_row_to_list[4].strip(),
                "start_time": each_schedule_row_to_list[5].strip(),
            }
            if not first:
                print(
                    f"Zoo keeper {each_schedule_row_to_list[0]} with name as {each_schedule_row_to_list[1]} works in enclosure for {each_schedule_row_to_list[2]}.")
                print(
                    f"Feed time are: {each_schedule_row_to_list[3]} and {each_schedule_row_to_list[4]} {each_schedule_row_to_list[1]} starts work at {each_schedule_row_to_list[5].strip()}")

    return zoo_info


def display_times(zoo_info):
    found_animal = False
    if not zoo_info:
        user_message("The schedule are currently not available!")
        return

    user_search = input("Please enter the animal name to check the schedule :) ").lower().strip()
    for schedule_items in zoo_info.values():
        if user_search == schedule_items['enclosure'].lower():
            print(
                f"The {schedule_items['enclosure']} have feeding time at {schedule_items['feedAm']} and at {schedule_items['feedPm']}\n")
            found_animal = True

    if not found_animal:
        print("The animal you are searching is currently not available in the zoo!, search for another animal.\n")


def validate_time(check_in_time):
    try:
        return bool(datetime.strptime(check_in_time, "%H:%M:%S"))
    except ValueError:
        return False


def check_in(keeper_id, zoo_info):
    check_in_time = input("What time are you checking in?")
    outcome = validate_time(check_in_time)
    if not outcome:
        print(f"The time that you have entered is not in the correct format. Enter it as HH:MM:SS")
        return
    elif datetime.strptime(check_in_time, '%H:%M:%S') <= datetime.strptime(zoo_info[keeper_id]['start_time'],
                                                                           '%H:%M:%S'):
        print("checked in on time")
    else:
        logging_late_check_in(zoo_info[keeper_id]['name'], 'checked in time is late')


def logging_late_check_in(name, msg):
    print(name, msg)
    with open('late_checkin.csv', 'a') as late_checkin_date:
        late_checkin_date.write(f"{name} {msg}\n")


def report_feeds_complete(record):
    all_fed = []
    which_enc = input("Which enclosure are you reporting feeds completed for?")
    which_feed = int(input("Would this be for the 1. am or 2.pm feed"))
    time_feed = "AM" if which_feed == 1 else "PM"

    for key in record.keys():
        print(key)
        if key == which_enc:
            all_fed = record[which_enc]

    print(all_fed)

    if which_feed == 1:
        if not all_fed:
            all_fed = [1,0]
        else:
            all_fed[0] = 1
        print(f"{which_enc} are fed for the {time_feed} feed")
    else:
        if not all_fed:
            all_fed = [0, 1]
        else:
            all_fed[1] = 1
        print(f"{which_enc} are fed for the {time_feed} feed")

    record[which_enc] = all_fed
    print(record)
    return record


def check_key(id, data):
    msg = ""
    for zoo_keeper_id in data:
        if id == zoo_keeper_id:
            msg = "Valid"
    return msg


def main():
    information = zoo_info(True)
    record = {}
    validate_time('')
    while True:
        choice = int(input("Zookeeper and enclosure information about feeds\n"
                           "1. Show zookeeper information for all enclosures \n"
                           "2. Check a feed time for an animal\n"
                           "3. Zookeeper check in\n"
                           "4. Daily report of feeds\n"
                           "5. Exit\n"))
        match choice:
            case 1:
                zoo_info()
            case 2:
                display_times(information)
            case 3:
                keeper_id = input("Please enter the zookeeper's id to check in for work")
                outcome = check_key(keeper_id, information)
                if outcome == "":
                    print("No such Id exists, try again")
                else:
                    check_in(keeper_id, information)
            case 4:
                record = report_feeds_complete(record)
            case 5:
                break
            case _:
                print("Incorrect choice entered")


if __name__ == '__main__':
    main()
