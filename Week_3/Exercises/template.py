def one():
    print(1)


def two():
    print(2)


def three():
    print(3)


def four():
    print(4)


def five():
    print(5)


def main():
    while True:
        choice = int(input(" *** Template *** System\n"
                           "1. \n"
                           "2. \n"
                           "3. \n"
                           "4. \n"
                           "5. Exit\n"
                           "Please make your choice: "))

        match choice:
            case 1:
                one()
            case 2:
                two()
            case 3:
                three()
            case 4:
                four()
            case 5:
                five()
            case _:
                print(" *** Please select from above option! *** \n")


if __name__ == '__main__':
    main()
