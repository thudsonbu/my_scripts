def retrieve_pay():
    weekly_pay = []

    while True:
        try:
            print('Input weekly pay (float), e to exit, d to delete last, l to list')
            command = input()

            if command == 'e':
                break

            elif command == 'd':
                weekly_pay.pop()

            elif command == 'l':
                total = 0.0

                for pay in weekly_pay:
                    print(pay)
                    total += pay

                print("Total: " + str(total))

            else:
                weekly_pay.append(float(command))

        except Error:
            print(Error)

    return None


def main():
    retrieve_pay()


main()
