# LAI KAI YONG TP059040
# LIM WYE YEE TP059371

# decoration
def decoration():
    return '*' * 10


# get total lines in carDatabase file
def cardb_line_count():
    file = open("carDatabase.txt", "r")
    line_in_file = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            line_in_file += 1
    # total unique car details
    total = int(line_in_file / 7)
    return total


# get total lines in customerDetails file
def custdb_line_count():
    file = open("customerDetails.txt", "r")
    line_in_file = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            line_in_file += 1
    # total unique car details
    total = int(line_in_file / 5)
    return total


# get total lines in customerBooking file
def bookdb_line_count():
    file = open("customerBookingPayment.txt", "r")
    line_in_file = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            line_in_file += 1
    # total unique car details
    total = int(line_in_file / 7)
    return total


# convert the line users want to modified to index.
def index_converter(a):
    return a - 1


# Welcome page
def welcome():
    print(decoration(), "Welcome to the Online Car Rental System(OCRS) by Super Car Rental Services(SCRS)", decoration())
    print("""\nEnter the number that best describe you.
    Admin : 1
    Customer : 2
    """)
    login_system()


# Exit
def exit_system():
    confirmation = input("Are you sure you want to exit the Online Car Rental System?\n\n\t[YES] or [NO]\n\nOption =>\t").upper()
    if confirmation == "YES":
        print(decoration(), "Exit", decoration())
        exit()
    elif confirmation == "NO":
        print("You will be redirect to the welcome page shortly...\n")
        welcome()
    else:
        print("Invalid input, please enter YES or NO.")
        return exit_system()


# data header.
def header():
    car_header = ['Car ID', 'Car Brand', 'Car Model', 'Car Plate', 'Year', 'Status', 'Price']
    format_row = "{}  " * (len(car_header) + 1)
    print("\n", format_row.format("", *car_header))


# View all car data
def view_cars():
    car_details = {}
    car_holder = []
    with open('carDatabase.txt', 'r') as original:
        for line in original:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    line.strip()
                    continue
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
    header()
    index = 0
    line_num = 1
    for car in car_holder:
        print("{:<4}{:<9}{:<10}{:<11}{:<10}{:<6}{:<8}{:<5}"
              .format(line_num, car_holder[index]['car_id'], car_holder[index]['car_brand'], car_holder[index]['car_name'],
                      car_holder[index]['car_plate'], car_holder[index]['year'], car_holder[index]['status'],
                      car_holder[index]['price']))
        index += 1
        line_num += 1


# Administrator login page
def administrator_login():
    administrator_credential = {}
    with open("administratorLoginInfo.txt", "r") as administrator_file:
        for data in administrator_file:
            (key, value) = data.strip().split(": ")
            administrator_credential[key] = value
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")
    if username == administrator_credential["username"] and password == administrator_credential["password"]:
        administrator_file.close()
        print("\n", decoration(), "Welcome, administrator!", decoration())
        administrator_system()
    else:
        print("Invalid credential, please check your username and password.")
        return administrator_login()


# Administrator access system
def administrator_system():
    option = int(input("""
Choose the action you want to perform:

1: Add cars to be rented out.
2: Modify car details.
3: Display records.
4: Search specific record.
5: Return a rented car.
6: Mark a car as Ready after the car is available upon customer's payment on confirmation for booking.
7: OCRS Analytics Dashboard
8: Exit the system.

Select your action:\t"""))
    if option == 1:
        admin_add_car()
    elif option == 2:
        admin_modify()
    elif option == 3:
        admin_display()
    elif option == 4:
        admin_search()
    elif option == 5:
        admin_return_rent()
    elif option == 6:
        admin_mark_ready()
    elif option == 7:
        analytics_dashboard()
    elif option == 8:
        exit_system()
    else:
        print("Invalid input, please choose options in range of 1 to 8.")
        return administrator_system()


# Administrator functionalities
# 1. Add car
def admin_add_car():
    add_or_not = input("""Insert car data:
[YES] to continue
[NO] to stop and display all data. Will be redirected to admin main screen.

Option =>\t""").upper()
    car_details = {}
    car_holder = []
    with open("carDatabase.txt", 'r') as car_id_automate:
        for line in car_id_automate:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
    car_index = 0
    for car in car_holder:
        last_car_id = car_holder[car_index]['car_id'].split("R")
        new_car_id_num = int(last_car_id[1]) + 1
        car_index += 1

    if add_or_not == "YES":
        new_car_id = 'R' + f'{new_car_id_num:03d}'
        print("Car ID: ", new_car_id)
        new_car_brand = input("Enter car brand: ")
        new_car_model = input("Enter car model: ")
        new_car_plate = input("Enter car plate: ")
        new_year = input("Enter car manufacture year: ")
        new_status = input("Enter status [Open / Rented]: ")
        new_price = int(input("Enter price per hour (Only numeric data): "))
        with open('carDatabase.txt', "a") as admin_add_file:
            admin_add_file.write("\ncar_id: {}\ncar_brand: {}\ncar_name: {}\n"
                                 "car_plate: {}\nyear: {}\nstatus: {}\nprice: {}"
                                 .format(new_car_id, new_car_brand, new_car_model, new_car_plate, new_year,
                                         new_status, new_price))
        print("\nInsert completed... Processing...\n")
        return admin_add_car()
    elif add_or_not == "NO":
        print(decoration(), " Displaying all data ", decoration())
        view_cars()
        print("\n", decoration(), " Back to administrator main screen. ", decoration())
        return administrator_system()


# 2. Modify car
def admin_modify():
    view_cars()
    car_details = {}
    car_holder = []
    with open('carDatabase.txt', 'r') as original:
        for line in original:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
        data_line = int(input("\nWhich line of data you want to perform the modification: "))
        item = input("""\nIMPORTANT!!! Note that uniqueID can't be modified.
If the car had been removed from the system place X in rent status.\n\nModify data type (e.g. Car Name, Price): """)\
            .replace(" ", '_').lower()
        origin_word = car_holder[index_converter(data_line)][item]
        print("Origin word: ", origin_word)
        replace_word = input("Replaced by: ")
        car_holder[index_converter(data_line)][item] = replace_word
    count = 1
    with open('carDatabase.txt', 'w') as modified:
        for information in car_holder:
            for key in information:
                if count < len(car_holder) * 7:
                    count += 1
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}\n')
                else:
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}')

    def cont_or_no():
        continue_or_not = input("Continue modifying?\n[YES] or [NO]\n=>\t").upper()
        if continue_or_not == 'YES':
            print("\nDisplaying modified data...\nContinue modification based on new data.")
            return admin_modify()
        elif continue_or_not == 'NO':
            print("\nYou will be redirected to the administrator main screen...")
            return administrator_system()
        else:
            print("\nInvalid input, only [YES] or [NO] allowed.\n")
            return cont_or_no()
    cont_or_no()


# 3. Display all data
def admin_display():
    dis_option = int(input("""\nDisplay data choice:
1: Cars Availability
2: Customer Bookings
3: Customer Payment for a specific time duration
4: Registered customers' username in the system
5: Exit to administrator main screen.\nOption =>\t"""))
    if dis_option == 1:
        dis_rent_car()
    elif dis_option == 2:
        dis_cus_booking()
    elif dis_option == 3:
        dis_cus_pay()
    elif dis_option == 4:
        registered_customer()
    elif dis_option == 5:
        administrator_system()
    else:
        print("Invalid input. Please select choices in range 1 to 5.")
        return admin_display()


# All display dataset
# continue to display menu or administrator page.
def display_redirect():
    option = int(input("""\nDo you wish to return to the display menu or administrator's main screen?

1: Display Menu
2: Administrator Main Screen

Option=>\t"""))
    if option == 1:
        print("\nYou will be redirected to the display menu...")
        return admin_display()
    elif option == 2:
        print("\nYou are returning to the administrator main screen....")
        return administrator_system()
    else:
        print("\nInvalid input, please key in YES or NO.\n")
        return display_redirect()


# 1. Display car with different status
def dis_rent_car():
    status = input("\nCategories available [Open] [Rented] [X] [Booked]\n=>\t").capitalize()
    header()
    car_details = {}
    car_holder = []
    index = 0
    emp_spotter = []
    with open("carDatabase.txt", "r") as display_rent:
        for line in display_rent:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
    line_number = 1
    for car in car_holder:
        if status == car_holder[index]['status']:
            emp_spotter.append(index)
            print("{:<4}{:<9}{:<10}{:<12}{:<9}{:<6}{:<9}{:<5}"
                  .format(line_number, car_holder[index]['car_id'], car_holder[index]['car_brand'],
                          car_holder[index]['car_name'], car_holder[index]['car_plate'], car_holder[index]['year'],
                          car_holder[index]['status'], car_holder[index]['price']))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of cars on that particular status.\n")
        display_redirect()

    display_redirect()


# 2. Display customer booking data
# Customer booking statement header
def cus_book_header():
    cus_book = ['Username', 'Car ID', 'Price', 'Days', 'Total Amount', 'Status', 'Reservation']
    format_row = "{}  " * (len(cus_book) + 1)
    print("\n", format_row.format("", *cus_book))


# booking data
def dis_cus_booking():
    cus_book_header()
    customer_statement = {}
    customers = []
    emp_spotter = []
    index = 0
    reservation = ('In Queue', 'Ready')
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

    line_number = 1
    for customer in customers:
        if reservation[0] == customers[index]['reservation'] or reservation[1] == customers[index]['reservation']:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<5}".format(line_number, customers[index]['username'],
                                                                       customers[index]['car id'],
                                                                       customers[index]['price'],
                                                                       customers[index]['days'],
                                                                       int(customers[index]['price'])*int(customers[index]['days']),
                                                                       customers[index]['status'],
                                                                       customers[index]['reservation']))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of customer booking statement.\n")
        display_redirect()

    display_redirect()


# 3. Display customer payment
# Customer payment statement header
def cus_pay_header():
    cus_pay = ['Username', 'Car ID', 'Price', 'Days', 'Total Amount', 'Status', 'Payment Method']
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


# Customer payment data
def dis_cus_pay():
    cus_pay_header()
    customer_statement = {}
    customers = []
    emp_spotter = []
    index = 0
    status = 'Paid'
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

    line_number = 1
    for customer in customers:
        if status == customers[index]['status']:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<5}".format(line_number, customers[index]['username'],
                                                                        customers[index]['car id'],
                                                                        customers[index]['price'],
                                                                        customers[index]['days'],
                                                                        int(customers[index]['price']) * int(customers[index]['days']),
                                                                        customers[index]['status'],
                                                                        customers[index]['payment method']))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of customer payment statement.\n")
        display_redirect()

    display_redirect()


# 4. Display all registered customer username
def registered_customer():
    customer_details = {}
    customers = []
    with open("customerDetails.txt", 'r') as get_cust_info:
        for line in get_cust_info:
            row = line.strip().split(": ")
            customer_details[row[0]] = row[1]
            for customer in range(1, custdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_details) == 5:
                    copy_data = customer_details.copy()
                    customers.append(copy_data)
                    customer_details = {}
                    continue

    index = 0
    customers_names = []
    for customer in customers:
        customers_names.append(customers[index]['username'])
        index += 1

    customers_names.sort()

    line_num = 1
    print('\n\tUsername')
    for name in customers_names:
        print(f"{line_num}\t{name}", end='\n')
        line_num += 1

    print("\nThis is all of the registered customers' username."
          "\nReturning to the administrator main screen....")
    administrator_system()


# 4. Search Record
def admin_search():
    file_choose = int(input("""Choose database that you want to inspect / search
1: Customer Booking
2: Customer Payment

Option =>\t"""))
    if file_choose == 1:
        cus_book_search()
    elif file_choose == 2:
        cus_pay_search()
    else:
        print("Invalid input, choose only 1 or 2.\n")
        return admin_search()


# Continue at search menu or back to administrator main screen.
def search_redirect():
    option = int(input("""\nDo you want to return to the search menu or administrator main screen?
    
1: Search menu
2: Administrator Main screen
=>\t"""))
    if option == 1:
        print("\nYou will be redirected to the search menu shortly....\n")
        return admin_search()
    elif option == 2:
        print('\nYou will be redirected to the administrator main screen shortly...\n')
        return administrator_system()
    else:
        print("\nInvalid input, please select 1 or 2.\n")
        return search_redirect()


# Search on customer booking data
def cus_book_search():
    data_type = input("""\nOptions: [Username] [Car ID] [Price] [Days] [Total Amount] [Status] [Reservation]
 
What is the data type you would like to seek for: """).lower()
    search_phrase = input("Enter keyword to search: ")
    cus_book_header()
    customer_statement = {}
    customers = []
    emp_spotter = []
    index = 0
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

    line_num = 1
    for customer in customers:
        if search_phrase == customers[index][data_type]:
            emp_spotter.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<5}".format(line_num, customers[index]['username'],
                                                                        customers[index]['car id'],
                                                                        customers[index]['price'],
                                                                        customers[index]['days'],
                                                                        int(customers[index]['price']) * int(customers[index]['days']),
                                                                        customers[index]['status'],
                                                                        customers[index]['reservation']))
            index += 1
            line_num += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of customer booking statement based on your search keyword.\n")

        def cont_search_book():
            option = input("Continue searching?\n\t[YES] or [NO] "
                           "\n\n[NO] to navigate back to administrator main screen\n=>\t").upper()
            if option == 'YES':
                print("Returning back to the customer booking search page.")
                cus_book_search()
            elif option == 'NO':
                print("\nYou will be redirected to the functionalities page shortly....\n")
                administrator_system()
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_search_book()
        cont_search_book()

    search_redirect()


# search on customer payment data
def cus_pay_search():
    data_type = input("""\nOptions: [Username] [Car ID] [Price] [Days] [Total Amount] [Status] [Reservation] 

What is the data type you would like to seek for: """).lower()
    search_phrase = input("Enter keyword to search: ")
    cus_pay_header()
    customer_statement = {}
    customers = []
    emp_spotter = []
    index = 0
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

    line_num = 1
    for customer in customers:
        if search_phrase == customers[index][data_type]:
            emp_spotter.append(index)
            print("{:<4}{:<10}{:<9}{:<7}{:<8}RM{:<9}{:<9}{:<5}".format(line_num, customers[index]['username'],
                                                                        customers[index]['car id'],
                                                                        customers[index]['price'],
                                                                        customers[index]['days'],
                                                                        int(customers[index]['price']) * int(customers[index]['days']),
                                                                        customers[index]['status'],
                                                                        customers[index]['payment method']))
            index += 1
            line_num += 1
        else:
            index += 1
            continue

    if not emp_spotter:
        print("There is no relevant data for the records of customer payment related to your search keyword.")

        def cont_search_pay():
            option = input("Continue searching?\n\t[YES] or [NO] "
                           "\n\n[NO] to navigate back to administrator main screen\n=>\t").upper()
            if option == 'YES':
                print("Returning back to the customer payment search page.")
                cus_pay_search()
            elif option == 'NO':
                print("\nYou will be redirected to the functionalities page shortly....\n")
                administrator_system()
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_search_pay()
        cont_search_pay()

    search_redirect()


# 5. Return a Rented Car.
# customer statement header
def cus_statement_header():
    cus_pay = ['Username', 'Car ID', 'Price', 'Days', 'Total Amount', 'Status', 'Reservation', 'Payment Method']
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


# return rent
def admin_return_rent():
    customer_statement = {}
    customers = []
    index1 = 0
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

        cus_statement_header()
        line_num = 1
        index_collector = []
        for customer in customers:
            if customers[index1]['status'] == 'Paid' and customers[index1]['reservation'] == 'Renting':
                index_collector.append(index1)
                print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}".format(line_num,
                                                                                 customers[index1]['username'],
                                                                                 customers[index1]['car id'],
                                                                                 customers[index1]['price'],
                                                                                 customers[index1]['days'],
                                                                                 int(customers[index1]['price']) * int(customers[index1]['days']),
                                                                                 customers[index1]['status'],
                                                                                 customers[index1]['reservation'],
                                                                                 customers[index1]['payment method']))
                index1 += 1
                line_num += 1
            else:
                index1 += 1
                continue

    # if the data is empty or no data to display
    if not index_collector:
        print("There is no relevant data for records of cars that should be return to the system.\n"
              "Redirecting to the administrator main screen...\n")
        administrator_system()

    return_rent = int(input("\nWhich statement you would like to return the rent car (line of statement): "))
    index_value = index_converter(return_rent)
    new_index = index_collector[index_value]
    customers[new_index]['reservation'] = 'Completed'
    car_id = customers[new_index]['car id']

    car_details = {}
    cars = []
    index2 = 0
    with open("carDatabase.txt", 'r') as read_mark_open:
        for line in read_mark_open:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    cars.append(copy_data)
                    car_details = {}
                    continue

        for car in cars:
            if cars[index2]['car_id'] == car_id:
                open_index = index2
                index2 += 1

            else:
                index2 += 1
                continue

    cars[open_index]['status'] = 'Open'
    count1 = 1
    with open('customerBookingPayment.txt', 'w') as modified:
        for information in customers:
            for key in information:
                if count1 < len(customers) * 7:
                    count1 += 1
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}\n')
                else:
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}')

    count2 = 1
    with open('carDatabase.txt', 'w') as mark_open:
        for car in cars:
            for key in car:
                if count2 < len(cars) * 7:
                    count2 += 1
                    list_of_strings = f'{key}: {car[key]}'
                    mark_open.write(f'{list_of_strings}\n')
                else:
                    list_of_strings = f'{key}: {car[key]}'
                    mark_open.write(f'{list_of_strings}')

    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM {:<8}{:<9}{:<13}{:<8}".format(customers[new_index]['username'],
                                                                    customers[new_index]['car id'],
                                                                    customers[new_index]['price'],
                                                                    customers[new_index]['days'],
                                                                    int(customers[new_index]['price']) * int(customers[new_index]['days']),
                                                                    customers[new_index]['status'],
                                                                    customers[new_index]['reservation'],
                                                                    customers[new_index]['payment method']))
    cont_return()


# Continue returning rented car?
def cont_return():
    option = input("\nContinue returning rent car?\n\t[YES] or [NO]\n=>\t").upper()
    if option == 'YES':
        admin_return_rent()
    elif option == 'NO':
        print('Returning to administrator main screen...')
        administrator_system()
    else:
        print("Invalid input, please insert YES or NO.\n")
        return cont_return()


# 6: Mark a car as Ready after the car is available upon customer's payment on confirmation for booking.
def admin_mark_ready():
    customer_statement = {}
    customers = []
    index1 = 0
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

        cus_statement_header()
        line_num = 1
        index_collector = []
        for customer in customers:
            if customers[index1]['status'] == 'Paid' and customers[index1]['reservation'] == 'In Queue':
                index_collector.append(index1)
                print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}".format(line_num,
                                                                                 customers[index1]['username'],
                                                                                 customers[index1]['car id'],
                                                                                 customers[index1]['price'],
                                                                                 customers[index1]['days'],
                                                                                 int(customers[index1]['price']) * int(customers[index1]['days']),
                                                                                 customers[index1]['status'],
                                                                                 customers[index1]['reservation'],
                                                                                 customers[index1]['payment method']))
                index1 += 1
                line_num += 1
            else:
                index1 += 1
                continue
    # if the data is empty or no data to display
    if not index_collector:
        print("\nNo data had been identified which require the action of marking the car status as ready.")

        print("Returning to administrator main screen...")
        administrator_system()

    return_rent = int(input("\nWhich statement you would like to mark as ready upon customer's booking on confirmation towards booking: "))
    index_value = index_converter(return_rent)
    new_index = index_collector[index_value]
    customers[new_index]['reservation'] = 'Ready'
    count = 1
    with open('customerBookingPayment.txt', 'w') as modified:
        for information in customers:
            for key in information:
                if count < len(customers) * 7:
                    count += 1
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}\n')
                else:
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}')
    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM {:<8}{:<9}{:<13}{:<8}".format(customers[new_index]['username'],
                                                                    customers[new_index]['car id'],
                                                                    customers[new_index]['price'],
                                                                    customers[new_index]['days'],
                                                                    int(customers[new_index]['price']) * int(
                                                                        customers[new_index]['days']),
                                                                    customers[new_index]['status'],
                                                                    customers[new_index]['reservation'],
                                                                    customers[new_index]['payment method']))

    def cont_modify_or_not():
        option = input("""\nDo you wish to mark more cars as ready?
        
\t[YES] or [NO]
[NO] to navigate back to the administrator main screen.
    
Option =>\t""").upper()
        if option == 'YES':
            print("\nYou are returning to the marking ready page,please be patient..\n")
            admin_mark_ready()
        elif option == 'NO':
            print("\nYou will be redirected to the administrator main screen..\n")
            administrator_system()
        else:
            print("\nInvalid input, please select either 1 or 2.\n")
            return cont_modify_or_not()
    cont_modify_or_not()


# 7. Analytics Dashboard
def analytics_dashboard():
    # retrieve data from customers' booking / payment database
    customer_statement = {}
    customers1 = []
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers1.append(copy_data)
                    customer_statement = {}
                    continue

    # retrieve data from car database
    car_details = {}
    car_holder = []
    with open("carDatabase.txt", "r") as display_rent:
        for line in display_rent:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue

    # retrive data from customer's information database
    customer_details = {}
    customers2 = []
    with open("customerDetails.txt", "r") as customer_file:
        for line in customer_file:
            row = line.strip().split(": ")
            customer_details[row[0]] = row[1]
            for information in range(1, custdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_details) == 5:
                    copy_data = customer_details.copy()
                    customers2.append(copy_data)
                    customer_details = {}
                    break

    # Display analytics information in a dashboard format
    print(f"""
{decoration()} OCRS Data Analytics Dashboard {decoration()}

Total cars:                         {len(car_holder)} cars
Total customers:                    {len(customers2)} customers
Total booking / payment records     {len(customers1)} statements

Keep up your great work! \U0001F592

Returning to administrator system....""")
    administrator_system()


# Customer landing page
def customer_interface():
    option = int(input("""As a visitor, select your action.

1: View all cars with any status.
2: Membership Registration \t - get access to more features.
3: Registered customers' section.
4: Exit the system.

Option  =>\t"""))
    if option == 1:
        view_cars()
        cont_main_menu()
    elif option == 2:
        cust_reg_header()
    elif option == 3:
        registered_login()
    elif option == 4:
        exit_system()
    else:
        print("Invalid input, please insert valid value (1 to 4): ")
        return customer_interface()


# Redirect customer landing page, login or register
def cont_main_menu():
    redirect = int(input("""\nDo you wish to go back to the main menu or login for more functionalities?
    
1: Main menu
2: Proceed to log in
3: Proceed to registration (For customer with no account in the server)

Option =>\t"""))

    if redirect == 1:
        print("\nReturning to the main menu...")
        return customer_interface()
    elif redirect == 2:
        print("\nRedirecting to the customer log in page....")
        return registered_login()
    elif redirect == 3:
        print("\nRedirecting to the customer registration page....")
        return customer_registration()
    else:
        print("\nInvalid input, please select either 1, 2 or 3.")
        return cont_main_menu


# Registration header
def cust_reg_header():
    print(decoration(), "Welcome to the registration page", decoration(),"\n")
    customer_registration()


# Customer Registration
def customer_registration():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("customerDetails.txt", 'r') as existing, open("customerDetails.txt", 'a') as new_customer:
        check = existing.read()
        if username in check:
            print("\nThis username had been used, please use another username.\n")
            return customer_registration()
        else:
            print("\nPlease fill in the following details to provide more information to rent a car / cars.\n")
            address = input("Address: ")
            contact_number = input("Contact number: ")
            new_customer.write(f"\nusername: {username}\npassword: {password}\naddress: {address}"
                               f"\ncontact number: {contact_number}")
            print(decoration(), " Thank you for registering ", decoration(), "\n")
            balance = 0
            print("Your balance is now: ", balance, "\nYou can recharge it from the customer functionalities page.")
            new_customer.write(f"\nbalance: {balance}")
    print("\nYou can login to the system now. Start renting your car! :D\n")
    customer_interface()


# Customer Log in
def registered_login():
    for time in range(1, 4):
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")
        with open("customerDetails.txt", 'r') as registration:
            customer_details = {}
            customers = []
            index = 0
            with open("customerDetails.txt", "r") as customer_file:
                for line in customer_file:
                    row = line.strip().split(": ")
                    customer_details[row[0]] = row[1]
                    for information in range(1, custdb_line_count()):
                        if row == "":  # empty line
                            break
                        elif len(customer_details) == 5:
                            copy_data = customer_details.copy()
                            customers.append(copy_data)
                            customer_details = {}
                            continue
        for customer in customers:
            if username == customers[index]['username'] and password == customers[index]['password']:
                print("\n", decoration(), " Welcome to the OCRS, ", username, decoration(), "\n")
                reg_customer()
                break
            index += 1
        else:
            print("\nInvalid username or password, please try again...")

            def registration_inquiry():
                register_confirm = input("""\nDo you have an account? [YES] or [NO]

Option =>\t""").upper()
                if register_confirm == "YES":
                    print("Please try again.")
                    # return registered_login()
                elif register_confirm == "NO":
                    def register_account_ask():
                        register_account = input("\nDo you wish to register a new account? [YES] or [NO]:\t")
                        if register_account == "YES":
                            print("Redirecting to the customer registration page...\n")
                            cust_reg_header()
                        elif register_account == 'NO':
                            print("\nReturning to the main menu..\n")
                            customer_interface()
                        else:
                            print("Invalid input, please key in [YES] or [NO].")
                            return register_account_ask()
                    register_account_ask()
                else:
                    print("\nInvalid input, please select [YES] or [NO].")
                    return registration_inquiry()
            registration_inquiry()
    else:
        print("\nYou had exceeded the limit to log in your account..Please try again after 1 minute..\n")
        return customer_interface()


# Customer functionalities
def reg_customer():
    print(decoration()*2, f"\nFunctionalities Page\n{decoration()*2}")
    option = int(input("""\nWhat would you like to perform?

1: View all available car for rent.
2: Modify personal details.
3: View personal rental history.
4: Book a car.
5: Pay the car that you booked earlier.
6: Top up your balance.
7: Exit the portal. 

Option =>\t"""))
    if option == 1:
        dis_all_rent()
    elif option == 2:
        modify_details()
    elif option == 3:
        rental_hist()
    elif option == 4:
        book_car()
    elif option == 5:
        pay_car()
    elif option == 6:
        top_up_header()
    elif option == 7:
        exit_system()
    else:
        print("Invalid choice, please enter valid value (1 to 6).\n")
        return reg_customer()


# retrieve all available to rent cars.
def rent_car_details():
    status = "Open"
    header()
    car_details = {}
    car_holder = []
    index = 0
    with open("carDatabase.txt", "r") as display_rent:
        for line in display_rent:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
    line_num = 1
    for car in car_holder:
        if status == car_holder[index]['status']:
            print("{:<4}{:<9}{:<10}{:<12}{:<9}{:<8}{:<7}{:<5}"
                  .format(line_num, car_holder[index]['car_id'], car_holder[index]['car_brand'],
                          car_holder[index]['car_name'], car_holder[index]['car_plate'], car_holder[index]['year'],
                          car_holder[index]['status'], car_holder[index]['price']))
            index += 1
            line_num += 1
        else:
            index += 1
            continue


# 1. View detail of cars to be rented out.
def dis_all_rent():
    rent_car_details()

    # ask to book car or back to the main menu from the open status cars
    def cont_book_car():
        car_booking = int(input("""\nDo you want to proceed to book a car or return to the main menu?

    1: Booking
    2: Customers functionalities menu

Option =>\t"""))

        if car_booking == 1:
            print("Redirecting to booking page...")
            book_car()
        elif car_booking == 2:
            print("Returning to main menu...")
            reg_customer()
        else:
            print("Invalid input, please select either [YES] or [NO]")
            return cont_book_car()
    cont_book_car()


# 2. Modify personal details
def modify_details():
    username = input("Your username is requested to check your credential for profile modification: ")
    customer_details = {}
    customers = []
    index = 0
    with open("customerDetails.txt", "r") as customer_file:
        for line in customer_file:
            row = line.strip().split(": ")
            customer_details[row[0]] = row[1]
            for information in range(1, custdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_details) == 5:
                    copy_data = customer_details.copy()
                    customers.append(copy_data)
                    customer_details = {}
                    break
                else:
                    continue
        for customer in customers:
            if customers[index]['username'] == username:
                cust_index = index
                for key, value in customer.items():
                    print(f'{key}: {value}')
                break
            index += 1
        else:
            print("Username is unidentified, please try again.")
            return modify_details()
        data_type = ['Password', 'Address', 'Contact Number']
        print("\nIMPORTANT! Note that username is immutable.\nOptions: {}".format(data_type).replace("\'", " "))
        modify_type = input("\nWhich type of data you would like to change: ").lower()
        old_data = customers[cust_index][modify_type]
        print("Original data: ", old_data)
        new_data = input("Replace with: ")
        customers[cust_index][modify_type] = new_data
    count = 1
    with open('customerDetails.txt', 'w') as modified:
        for information in customers:
            for key in information:
                if count < len(customers) * 5:
                    count += 1
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}\n')
                else:
                    list_of_strings = f'{key}: {information[key]}'
                    modified.write(f'{list_of_strings}')
    cont_modify()


# Continue profile modification?
def cont_modify():
    continue_or_not = input("Continue modifying?\n[YES] or [NO]\n=>\t").upper()
    if continue_or_not == 'YES':
        print("\nUpdating modified data...\n"
              "Continue modification based on new data and your credential will be requested again\n")
        return modify_details()
    elif continue_or_not == 'NO':
        print("\nYou will be redirected to the customer functionalities page...")
        return reg_customer()
    else:
        print("\nInvalid input, only [YES] or [NO] allowed.\n")
        return cont_modify()


# 3. View personal rental history
def rental_hist():
    username = input("\nIMPORTANT!! You are going to access customers' private data.\nEnter your credential username: ")
    customer_statement = {}
    customers = []
    index = 0
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue

    emp_spotter = []
    cus_statement_header()
    for customer in customers:
        if username == customers[index]['username']:
            emp_spotter.append(index)
            print("   {:<11}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<8}".format(customers[index]['username'],
                                                                           customers[index]['car id'],
                                                                           customers[index]['price'],
                                                                           customers[index]['days'],
                                                                           int(customers[index]['price']) * int(customers[index]['days']),
                                                                           customers[index]['status'],
                                                                           customers[index]['reservation'],
                                                                           customers[index]['payment method']))
        index += 1

    # if the data is empty or no data to display
    if not emp_spotter:
        print("\nThe rental history is empty, start to rent a car! :)")

    print("\nYou will be redirected to the functionalities page...\n")
    reg_customer()


# 4. Select and Book a car for a specific duration.
def book_car():
    rent_car_details()
    print("")
    select_car = input("Select the car ID you would like to book: ")
    username = input("Enter your username to request your booking: ")
    car_details = {}
    car_holder = []
    index = 0
    with open('carDatabase.txt', 'r') as original:
        for line in original:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
    for car in car_holder:
        if car_holder[index]['car_id'] == select_car:
            price = car_holder[index]['price']
            car_holder[index]['status'] = 'Booked'
            break
        index += 1
    days = int(input("How many day(s) you would like to book it: "))

    count = 1
    with open("carDatabase.txt", 'w') as new_status:
        for data in car_holder:
            for records in data:
                if count < len(car_holder) * 7:
                    count += 1
                    list_of_records = f'{records}: {data[records]}'
                    new_status.write(f'{list_of_records}\n')
                else:
                    list_of_records = f'{records}: {data[records]}'
                    new_status.write(f'{list_of_records}')

    with open("customerBookingPayment.txt", 'a') as new_booking:
        new_booking.write(f"\nusername: {username}\ncar id: {select_car}\nprice: {price}\ndays: {days}\n"
                          f"status: Pending\nreservation: N/A\npayment method: N/A")
    print("\nYou will be redirected to the customer functionalities page.\n\n"
          "You can make your payment by choosing option 5 to confirm your booking.")
    return reg_customer()


# 5. Do payment to confirm Booking.
def pay_car():
    username = input("\nEnter your username to pay for your booking confirmation: ")
    car_details = {}
    car_holder = []
    with open('carDatabase.txt', 'r') as original:
        for line in original:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
    customer_statement = {}
    customers = []
    index = 0
    new_index = []
    line_num = 1
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_statement[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_statement) == 7:
                    copy_data = customer_statement.copy()
                    customers.append(copy_data)
                    customer_statement = {}
                    continue
    cus_statement_header()
    for customer in customers:
        if username == customers[index]['username'] and customers[index]['status'] == 'Pending' \
                and customers[index]['payment method'] == 'N/A':
            new_index.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}".format(line_num, customers[index]['username'],
                                                                             customers[index]['car id'],
                                                                             customers[index]['price'],
                                                                             customers[index]['days'],
                                                                             int(customers[index]['price']) * int(customers[index]['days']),
                                                                             customers[index]['status'],
                                                                             customers[index]['reservation'],
                                                                             customers[index]['payment method']))
            line_num += 1
        elif username == customers[index]['username'] and customers[index]['status'] == 'Pending' \
                and customers[index]['payment method'] == 'balance':
            print("    {:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<8}".format(customers[index]['username'],
                                                                            customers[index]['car id'],
                                                                            customers[index]['price'],
                                                                            customers[index]['days'],
                                                                            int(customers[index]['price']) * int(customers[index]['days']),
                                                                            customers[index]['status'],
                                                                            customers[index]['reservation'],
                                                                            customers[index]['payment method']))
            pay_balance()
        else:
            index += 1

    # if the data is empty or no data to display
    if not new_index:
        print("\nInvalid username or customer does not have a booking request.")

        def cont_pay():
            option = input("\nContinue payment?\n\t[YES] or [NO]\n"
                           "[NO] return to customer functionalities page\n=>\t").upper()
            if option == 'YES':
                print("\nReturning to the payment page...")
                pay_car()
            elif option == 'NO':
                print("\nYou will be redirected to the functionalities page shortly....\n")
                reg_customer()
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_pay()
        cont_pay()

    pay_statement = int(input("\nWhich booking statement (line) you would like to pay? "))
    statement_index = index_converter(pay_statement)
    pay_index = new_index[statement_index]
    car_id = customers[pay_index]['car id']
    print("\nIMPORTANT!! Note that you will need to make full payment to confirm your booking.\n")
    payment_method = input("""What would you like to use to pay the booking?
[credit card] [balance]
=>\t""").lower()

    customers[pay_index]['payment method'] = payment_method

    count = 1
    with open("customerBookingPayment.txt", 'w') as update_pay_method:
        for data in customers:
            for records in data:
                if count < len(car_holder) * 7:
                    count += 1
                    list_of_records = f'{records}: {data[records]}'
                    update_pay_method.write(f'{list_of_records}\n')
                else:
                    list_of_records = f'{records}: {data[records]}'
                    update_pay_method.write(f'{list_of_records}')

    if payment_method == 'credit card':
        print("\nNote that your private information in this area will not be stored in our cookies.\n")
        credit_card_num = input("Enter your credit card number: ")
        cvv = input("Enter your credit card's CVV: ")
        expiry_date = input("Enter your credit card's expiry date: ")

        print(f"""
Transaction completed...

{decoration()} Payment details {decoration()}

Paid amount: {int(customers[pay_index]['price']) * int(customers[pay_index]['days'])}
Credit card: {credit_card_num}
""", )
        customers[pay_index]['status'] = 'Paid'
        customers[pay_index]['reservation'] = 'In Queue'

        index1 = 0
        for car in car_holder:
            if car_holder[index1]["car_id"] == car_id:
                car_holder[index1]["status"] = 'Rented'
            index1 += 1

        count1 = 1
        with open("customerBookingPayment.txt", 'w') as paid_statement:
            for information in customers:
                for key in information:
                    if count1 < len(customers) * 7:
                        list_of_strings = f'{key}: {information[key]}'
                        paid_statement.write(f'{list_of_strings}\n')
                        count1 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        paid_statement.write(f'{list_of_strings}')

        count2 = 1
        with open("carDatabase.txt", 'w') as mark_rented:
            for information in car_holder:
                for key in information:
                    if count2 < len(car_holder) * 7:
                        list_of_strings = f'{key}: {information[key]}'
                        mark_rented.write(f'{list_of_strings}\n')
                        count2 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        mark_rented.write(f'{list_of_strings}')

        print("\nRedirecting to customer functionalities page...\n")
        reg_customer()
    elif payment_method == 'balance':
        pay_balance()
    else:
        print("Invalid input, due to privacy you will be redirected to the car payment statement page again...")
        return pay_car()


# Pay with balance
def pay_balance():
    username= input("\nYou are accessing your online balance, enter your username to make sure that is you: ")
    customer_details = {}
    customers = []
    index1 = 0
    with open("customerDetails.txt", "r") as balance_checker:
        for line in balance_checker:
            row = line.strip().split(": ")
            customer_details[row[0]] = row[1]
            for information in range(1, custdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_details) == 5:
                    copy_data = customer_details.copy()
                    customers.append(copy_data)
                    customer_details = {}
                    break
                else:
                    continue
        for customer in customers:
            if customers[index1]['username'] == username:
                new_index1 = index1
                balance = int(customers[index1]["balance"])
                break
            index1 += 1

    customer_pay = {}
    statements = []
    index2 = 0

    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_pay[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_pay) == 7:
                    copy_data = customer_pay.copy()
                    statements.append(copy_data)
                    customer_pay = {}
                    continue

        for statement in statements:
            if username == statements[index2]['username'] and statements[index2]['payment method'] == 'balance' \
                    and statements[index2]['status'] == 'Pending':
                new_index2 = index2
                total = int(statements[index2]['price']) * int(statements[index2]['days'])
                car_id = statements[index2]['car id']
                print("You have to pay: RM", total, "\nCar ID: ", statements[index2]['car id'])
            index2 += 1

    car_details = {}
    car_holder = []
    index3 = 0

    with open('carDatabase.txt', 'r') as original:
        for line in original:
            row = line.strip().split(": ")
            car_details[row[0]] = row[1]
            for car in range(1, cardb_line_count()):
                if row == "":  # empty line
                    break
                elif len(car_details) == 7:
                    copy_data = car_details.copy()
                    car_holder.append(copy_data)
                    car_details = {}
                    continue
        for car in car_holder:
            if car_holder[index3]['car_id'] == car_id:
                car_holder[index3]['status'] = 'Rented'
                break
            index3 += 1

    if balance >= total:
        balance -= total
        print("\nCurrent balance: ",balance,"\nYou had paid the booking confirmation.\nTransaction completed. Your current balance is", balance)
        customers[new_index1]["balance"] = str(balance)
        statements[new_index2]['status'] = 'Paid'
        statements[new_index2]['reservation'] = 'In Queue'
        statements[new_index2]['payment method'] = 'balance'

        count1 = 1
        with open('customerDetails.txt', 'w') as paid:
            for information in customers:
                for key in information:
                    if count1 < len(customers)*5:
                        list_of_strings = f'{key}: {information[key]}'
                        paid.write(f'{list_of_strings}\n')
                        count1 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        paid.write(f'{list_of_strings}')

        count2 = 1
        with open('customerBookingPayment.txt', 'w') as paid:
            for information in statements:
                for key in information:
                    if count2 < len(statements)*7:
                        list_of_strings = f'{key}: {information[key]}'
                        paid.write(f'{list_of_strings}\n')
                        count2 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        paid.write(f'{list_of_strings}')

        count3 = 1
        with open("carDatabase.txt", 'w') as mark_rented:
            for information in car_holder:
                for key in information:
                    if count3 < len(car_holder) * 7:
                        list_of_strings = f'{key}: {information[key]}'
                        mark_rented.write(f'{list_of_strings}\n')
                        count3 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        mark_rented.write(f'{list_of_strings}')

        print("\nRedirecting to customer functionalities page...\n")
        reg_customer()

    elif balance < total:
        print("\nYour balance is insufficient...\nYour current balance: RM", balance,
              "\n\nYou will need to top up before paying your booking confirmation."
              "\nRedirecting to top up system....\n")
        top_up_header()


# 6. Top up your balance.
def top_up_header():
    print("\n", decoration(), "Welcome to the top up system.", decoration())
    top_up()


def top_up():
    username = input("\nEnter your username to check your current balance: ")
    customer_details = {}
    customers = []
    index = 0
    with open("customerDetails.txt", "r") as balance_checker:
        for line in balance_checker:
            row = line.strip().split(": ")
            customer_details[row[0]] = row[1]
            for information in range(1, custdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_details) == 5:
                    copy_data = customer_details.copy()
                    customers.append(copy_data)
                    customer_details = {}
                    break
                else:
                    continue
        for customer in customers:
            if customers[index]['username'] == username:
                cust_index = index
                balance = int(customers[index]['balance'])
                print("Your current balance: ", str(balance))
                break
            else:
                index += 1
                continue
        else:
            print("Invalid username, please try again.")
            top_up()

    payment_method = int(input(f"""Which payment method do you prefer to top up your balance with? 

1: Credit/debit card 
2: FPX online banking

Option =>\t"""))
    if payment_method == 1:
        print("\n", decoration() * 3, "\nTop up with: Credit/debit card\n", decoration() * 3)
        credit_card_num = input("Enter your credit/debit card number: ")
        cvv = input("Enter your credit/debit card's CVV: ")
        expiry_date = input("Enter your credit/debit card's expiry date: ")
    elif payment_method == 2:
        print("\n", decoration() * 3, "\nTop up with: FPX online banking","\n", decoration() * 3)

        def bank_options():
            bank_choice = int(input(f"""Select your merchant:

1: Maybank
2: Public Bank
3: Ambank 
4: RHB Bank
5: CIMB Bank

=>\t"""))
            if bank_choice <= 5:
                account_no = input("Enter your account number: ")
                account_password = input("Enter your account password: ")
            else:
                print("Invalid input, please try again.")
                return bank_options()
        bank_options()

    top_up_value = int(input("How much do you want to top up: "))
    balance += top_up_value
    customers[cust_index]['balance'] = str(balance)

    print("Top up success, current balance: ", customers[cust_index]['balance'])

    with open('customerDetails.txt', 'w') as top_up_file:
        for information in customers:
            for key in information:
                list_of_strings = f'{key}: {information[key]}'
                top_up_file.write(f'{list_of_strings}\n')

    def cont_top_up():
        cont_or_not = input("""\nDo you wish to top up more? [YES] or [NO]
Note: Selecting NO will redirect you back to the functionalities main menu.

=>\t""").upper()
        if cont_or_not == "YES":
            print("Redirecting back to the top up section....")
            top_up()
        elif cont_or_not == "NO":
            print("\nRedirecting to the customer functionalities main menu...\n")
            reg_customer()
        else:
            print("Invalid input, please enter either [YES] or [NO]. ")
            return cont_top_up()
    cont_top_up()


# First login pass
def login_system():
    role = int(input("Option =>\t"))
    if role == 1:
        administrator_login()
    elif role == 2:
        customer_interface()
    else:
        print("\nInvalid choice, please choose again.")
        return login_system()


# call function to display welcome page as default
welcome()
