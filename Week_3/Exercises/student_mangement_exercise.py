from random import randrange


def get_student_id():
    student_first_name = input("Enter student\'s first name: ")
    student_last_name = input("Enter student\'s last name: ")
    return f"{student_first_name[0]}{student_last_name[0]}{randrange(1, 999)}"


def get_choice(question):
    entered_choice = input(f"{question}: ")
    if entered_choice.lower() == "yes":
        return True
    elif entered_choice.lower() == "no":
        return False


def enter_grade():
    grade1 = int(input("Enter the grade for CS:"))
    grade2 = int(input("Enter the grade for workshop:"))
    return grade1, grade2


def add_student():
    grade1 = 0
    grade2 = 0
    student_id = get_student_id()
    print(student_id)
    if get_choice("You have any grades to enter (yes/no) ?"):
        grade1, grade2 = enter_grade()
    return [student_id, grade1, grade2]


def get_id_from_user():
    return input("Enter the student id: ")


def change_or_update_grade(student_list):
    student_id = get_id_from_user()
    grade1, grade2 = enter_grade()
    for student in student_list:
        if student[0] == student_id:
            student[1] = grade1
            student[2] = grade2


def remove_student(student_list):
    student_id = get_id_from_user()
    if get_choice("Are you sure, you want to remove student (yes/no) ?"):
        for student in student_list:
            if student[0] == student_id:
                student_list.remove(student)


def generate_student_report(student_list):
    for student in student_list:
        print(f"Student id: {student[0]}")
        print(f"Student mark1: {student[1]}")
        print(f"Student mark2: {student[2]} \n")


def display_rank_of_students(student_list):
    sorted_list = [( student[0], (student[1] + student[2]) / 2)for student in
                   student_list]
    sorted(sorted_list, key=lambda student: student[1])
    print(sorted_list)


def main():
    student_list = []
    while True:
        choice = int(input("Student management System\n"
                           "1. Add a student\n"
                           "2. Change an assessment grade for a student\n"
                           "3. Remove a student\n"
                           "4. Generate a report of all students and their grades\n"
                           "5. Generate a report showing student grades highest to lowest\n"
                           "6. Exit\n"
                           "Please make your choice: "))

        match choice:
            case 1:
                student_list.append(add_student())
                print(student_list)
            case 2:
                change_or_update_grade(student_list)
                print(student_list)
            case 3:
                remove_student(student_list)
                print(student_list)
            case 4:
                generate_student_report(student_list)
            case 5:
                display_rank_of_students(student_list)
            case _:
                print(" *** Please select from above option! *** \n")


if __name__ == '__main__':
    main()
