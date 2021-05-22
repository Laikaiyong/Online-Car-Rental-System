# LAI KAI YONG TP059040
# LIM WYE YEE TP059371

# Section A: General code functionalities
# 1. decoration style of the system section block
def decoration():
    # pattern design
    return '*' * 10


# 2. convert the line users want to modified to index value.
def index_converter(a):
    return a - 1


# Section B: Extract databases unique data line (number)
# 1. get total unique data based on lines in carDatabase file
def cardb_line_count():
    # Read file and extract data
    file = open("carDatabase.txt", "r")
    line_in_file = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            line_in_file += 1

    # total unique car details based on cars
    total = int(line_in_file / 7)

    # store total unique data in cardb_line_count() function
    return total


# 2. get total unique data based on lines in customerDetails file
def custdb_line_count():
    # Read file and extract data
    file = open("customerDetails.txt", "r")
    line_in_file = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            line_in_file += 1

    # total unique customer details based on customers
    total = int(line_in_file / 5)

    # store total unique data in custdb_line_count() function
    return total


# 3. get total unique data based on lines in customerBookingPayment file
def bookdb_line_count():
    # Read file and extract data
    file = open("customerBookingPayment.txt", "r")
    line_in_file = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            line_in_file += 1

    # total unique customer booking/payment details based on customers
    total = int(line_in_file / 7)

    # store total unique data in bookdb_line_count() function
    return total


# Section C: Headers
# 1. Car data header
def car_header():
    car_headers = ['Car ID', 'Car Brand', 'Car Model', 'Car Plate', 'Year', 'Status', 'Price']
    format_row = "{}  " * (len(car_headers) + 1)
    print("\n", format_row.format("", *car_headers))


# 2. Customer booking statement data header
def cus_book_header():
    cus_book = ['Username', 'Car ID', 'Price', 'Days', 'Total Amount', 'Status', 'Reservation']
    format_row = "{}  " * (len(cus_book) + 1)
    print("\n", format_row.format("", *cus_book))


# 3. Customer payment statement data header
def cus_pay_header():
    cus_pay = ['Username', 'Car ID', 'Price', 'Days', 'Total Amount', 'Status', 'Payment Method']
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


# 4. Customer statement data header
def cus_statement_header():
    cus_pay = ['Username', 'Car ID', 'Price', 'Days', 'Total Amount', 'Status', 'Reservation', 'Payment Method']
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


# 5. Customer registration page header
def cus_reg_header():
    print(decoration(), "Welcome to the registration page", decoration(), "\n")
    customer_registration()


# 6. Customer top up page header
def top_up_header():
    print("\n", decoration(), "Welcome to the top up system.", decoration())
    top_up()


# Section D: General Users Interface
# 1. Welcome page with text display.
def welcome():
    print(decoration(), "Welcome to the Online Car Rental System(OCRS) by Super Car Rental Services(SCRS)",
          decoration())
    print("""\nEnter the number that best describe you.

    Admin : 1
    Customer : 2
    """)
    login_system()


# 2. Role definition pass
def login_system():
    # Ask for users' role
    role = int(input("Role =>\t"))

    # Administrator pass
    if role == 1:
        administrator_login()
    # Customer pass
    elif role == 2:
        customer_interface()
    # Error if neither 1 nor 2 are entered
    else:
        print("\nInvalid choice, please choose again.")
        return login_system()


# 3. Exit system
def exit_system():
    # Asking for exit confirmation
    confirmation = input("Are you sure you want to exit the Online Car Rental System?\n\n\t[YES] or [NO]"
                         "\n[NO] will redirect you to the welcome page\n\nOption =>\t").upper()

    # Terminate the program
    if confirmation == "YES":
        print(decoration(), "Exit", decoration())
        exit()

    # Direct to the welcome page
    elif confirmation == "NO":
        print("You will be redirect to the welcome page shortly...\n")
        welcome()

    # Error when either "YES" or "NO" are not selected
    else:
        print("Invalid input, please enter YES or NO.")
        return exit_system()


# Section E: Administrator
# 1. Administrator login page
def administrator_login():
    # store administrator credential username and password in a dictionary
    administrator_credential = {}
    with open("administratorLoginInfo.txt", "r") as administrator_file:
        for data in administrator_file:
            (key, value) = data.strip().split(": ")
            administrator_credential[key] = value

    # request for admins username and password
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    # username and password validation
    if username == administrator_credential["username"] and password == administrator_credential["password"]:
        administrator_file.close()
        administrator_system()
    else:
        print("Invalid credential, please check your username and password.")
        return administrator_login()


# 2. Administrator access system
def administrator_system():
    # Admins welcome line
    print("\n", decoration(), "Welcome, administrator!", decoration())

    # Admins functionalities menu
    option = int(input("""
Choose the action you want to perform:

1: Add cars to be rented out.
2: Modify car details.
3: Display records.
4: Search specific record.
5: Return a rented car.
6: Mark a car as Ready after the car is available upon customer's payment on confirmation for booking.
7: OCRS Data Analytics Dashboard
8: Exit the system.

Select your action:\t"""))

    # Execute system based on option
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

    # Error for invalid input
    else:
        print("Invalid input, please choose options in range of 1 to 8.")

        # request for input again
        return administrator_system()


# Section E01: Administrator functionalities
# 1. Add car
def admin_add_car():
    # Add car choice
    add_or_not = input("""
Insert car data:
[YES] to continue
[NO] to stop and display all data. Will be redirected to admin main screen.

Option =>\t""").upper()

    # Extract car data to dictionaries in list
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

    # Auto generate the new car id
    for car in car_holder:
        last_car_id = car['car_id'].split("R")
        new_car_id_num = int(last_car_id[1]) + 1

    # Add car while admins choose 'yes'
    if add_or_not == "YES":
        new_car_id = 'R' + f'{new_car_id_num:03d}'
        print("Car ID: ", new_car_id)
        new_car_brand = input("Enter car brand: ")
        new_car_model = input("Enter car model: ")
        new_car_plate = input("Enter car plate: ")
        new_year = input("Enter car manufacture year: ")
        new_status = input("Enter status [Open / Rented / X / Booked]: ")
        new_price = int(input("Enter price per hour (Only numeric data): "))

        # Append the new car data into carDatabase text file
        with open('carDatabase.txt', "a") as admin_add_file:
            admin_add_file.write("\ncar_id: {}\ncar_brand: {}\ncar_name: {}\n"
                                 "car_plate: {}\nyear: {}\nstatus: {}\nprice: {}"
                                 .format(new_car_id, new_car_brand, new_car_model, new_car_plate, new_year,
                                         new_status, new_price))
        print("\nInsert completed... Processing...\n")

        # Ask for admins choice on inserting more cars or stop adding
        return admin_add_car()

    # Stop adding car and display all cars
    elif add_or_not == "NO":
        print(decoration(), " Displaying all data ", decoration())
        view_cars()
        print("\n", decoration(), " Back to administrator main screen. ", decoration())
        return administrator_system()

    # Invalid choice and ask for choice again
    else:
        print("Invalid input, please try again.")
        return admin_add_car()


# 2. Modify car
def admin_modify():
    # Display all cars data
    view_cars()

    # Extract cars data to dictionaries in list
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

    # Ask for modification required details
    data_line = int(input("\nWhich line of data you want to perform the modification: "))
    print("\nIMPORTANT!!! Note that uniqueID can't be modified. "
          "\nIf the car had been removed from the system place X in rent status.\n\n")
    item = input("Modify data type (e.g. Car Name, Price): ").replace(" ", '_').lower()

    # Extract and display original data
    origin_word = car_holder[index_converter(data_line)][item]
    print("Origin word: ", origin_word)

    # Replace data
    replace_word = input("Replaced by: ")
    car_holder[index_converter(data_line)][item] = replace_word

    # Transfer new data to the text file
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

    # Ask for admins' preferences on continue editing / modify data
    def cont_or_no():
        continue_or_not = input("Continue modifying?\n[YES] or [NO]\n=>\t").upper()

        # Continue modification
        if continue_or_not == 'YES':
            print("\nDisplaying modified data...\nContinue modification based on new data.")
            return admin_modify()

        # Stop modification and return to admnistrator functionalities menu
        elif continue_or_not == 'NO':
            print("\nYou will be redirected to the administrator main screen...")
            return administrator_system()

        # Invalid input and ask for admins' choice again
        else:
            print("\nInvalid input, only [YES] or [NO] allowed.\n")
            return cont_or_no()

    # call function to execute in admin_modify() function
    cont_or_no()


# 3. Display all data
def admin_display():
    # data display menu
    dis_option = int(input("""\nDisplay data choice:
    
1. All Cars
2: Cars Availability
3: Customer Bookings
4: Customer Payment for a specific time duration
5: Registered customers' username in the system
6: Exit to administrator main screen.

Option =>\t"""))

    # Read option
    if dis_option == 1:
        view_cars()
        display_redirect()
    if dis_option == 2:
        dis_rent_car()
    elif dis_option == 3:
        dis_cus_booking()
    elif dis_option == 4:
        dis_cus_pay()
    elif dis_option == 5:
        registered_customer()
    elif dis_option == 6:
        administrator_system()

    # Invalid input, ask for display choice again
    else:
        print("Invalid input. Please select choices in range 1 to 6.")
        return admin_display()


# 3.1 All display dataset
# 1. View all car data
def view_cars():
    # Extract car data to dictionaries in list
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

    # Display all car data
    car_header()
    line_num = 1
    for car in car_holder:
        print("{:<4}{:<7}{:<12}{:<11}{:<10}{:<6}{:<8}{:<5}"
              .format(line_num, car['car_id'], car['car_brand'], car['car_name'], car['car_plate'], car['year'],
                      car['status'], car['price']))
        line_num += 1


# 2. Display car with different status
def dis_rent_car():
    # Extract car data to dictionaries in list
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

    # Ask for admins' preference on car status
    status = input("\nCategories available [Open] [Rented] [X] [Booked]\nStatus =>\t").capitalize()

    # Display cars with matching status
    index = 0
    emp_spotter = []
    line_number = 1
    car_header()
    for car in car_holder:
        if status == car['status']:
            emp_spotter.append(index)
            print("{:<4}{:<7}{:<12}{:<11}{:<10}{:<6}{:<8}{:<5}"
                  .format(line_number, car['car_id'], car['car_brand'], car['car_name'], car['car_plate'],
                          car['year'], car['status'], car['price']))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\n\nThere is no relevant data for records of cars on that particular status.\n")

        # Admins' option on redirection
        display_redirect()

    # Admins' option on redirection
    display_redirect()


# 2. Display customer booking statement
def dis_cus_booking():
    # Extract customer booking / payment statement to dictionaries in list
    customer_statement = {}
    customers = []
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

    # Set reservation only specify on booking status
    reservation = ('In Queue', 'Ready')

    # Display matching customer booking statement
    index = 0
    line_number = 1
    emp_spotter = []
    cus_book_header()
    for customer in customers:
        if reservation[0] == customer['reservation'] or reservation[1] == customer['reservation']:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<5}"
                  .format(line_number, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'], customer['reservation']))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\n\nThere is no relevant data for records of customer booking statement.\n")

        # Admins' option on redirection
        display_redirect()

    # Admins' option on redirection
    display_redirect()


# 3. Display customer payment statement
def dis_cus_pay():
    # Extract customer booking / payment statement to dictionaries in list
    customer_statement = {}
    customers = []
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

    # Set statement status only specify on 'Paid'
    status = 'Paid'

    # Display matching customer payment statement
    index = 0
    line_number = 1
    emp_spotter = []
    cus_pay_header()
    for customer in customers:
        if status == customer['status']:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<5}"
                  .format(line_number, customer['username'], customer['car id'], customer['price'],
                          customer['days'], int(customer['price']) * int(customer['days']),
                          customer['status'], customer['payment method']))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of customer payment statement.\n")

        # Admins' option on redirection
        display_redirect()

    # Admins' option on redirection
    display_redirect()


# 4. Display all registered customer username
def registered_customer():
    # Extract customer details to dictionaries in list
    customer_details = {}
    customers = []
    with open("customerDetails.txt", 'r') as get_cus_info:
        for line in get_cus_info:
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

    # Store all customers' username in a list
    customers_names = []
    for customer in customers:
        customers_names.append(customer['username'])

    # Arrange customers' username alphabetically
    customers_names.sort()

    # Display all customers' username
    line_num = 1
    print('\n\tUsername')
    for name in customers_names:
        print(f"{line_num}\t{name}", end='\n')
        line_num += 1

    print("\nThis is all of the registered customers' username.")

    # Admins' option on redirection
    display_redirect()


# 3.2 Continue to display menu or administrator page.
def display_redirect():
    # Ask for admins' preference in redirection
    option = int(input("""
Do you wish to return to the display menu or administrator's main screen?

1: Display Menu
2: Administrator Main Screen

Option=>\t"""))

    # Return to the display menu
    if option == 1:
        print("\nYou will be redirected to the display menu...")
        return admin_display()

    # Return to administrator functionalities main screen
    elif option == 2:
        print("\nYou are returning to the administrator main screen....")
        return administrator_system()

    # Invalid input, ask for redirection option again
    else:
        print("\nInvalid input, please key in 1 or 2.\n")
        return display_redirect()


# 4. Search Record
def admin_search():
    # Admin's option database search
    file_choose = int(input("""
Choose database that you want to inspect / search:

1: Customer Booking
2: Customer Payment

Option =>\t"""))

    # Booking statement searh
    if file_choose == 1:
        cus_book_search()

    # Payment statement search
    elif file_choose == 2:
        cus_pay_search()

    # Invalid input, ask for database option again
    else:
        print("Invalid input, choose only 1 or 2.\n")
        return admin_search()


# 4.1 Search data
# 1. Search on customer booking data
def cus_book_search():
    # Extract customer booking / payment statement to dictionaries in list
    customer_statement = {}
    customers = []
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

    # Ask for data users want to search
    data_type = input("""
Options: [Username] [Car ID] [Price] [Days] [Total Amount] 

What is the data type you would like to seek for: """).lower()
    search_phrase = input("Enter keyword to search: ")
    reservation = ("In Queue", "Ready")

    # Display related records based on search_phrase in customer booking statement
    index = 0
    line_num = 1
    emp_spotter = []
    cus_book_header()
    for customer in customers:
        if search_phrase == customer[data_type] and customer['reservation'] in reservation \
                and customer['status'] == "Paid":
            emp_spotter.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<5}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'], customer['reservation']))
            index += 1
            line_num += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of customer booking statement based on your search keyword.\n")

        # Ask for admins' options in continue searching or return to administrator main screen
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

    # Admins' option on redirection
    search_redirect()


# 2. Search on customer payment data
def cus_pay_search():
    # Extract customer booking / payment statement to dictionaries in list
    customer_statement = {}
    customers = []
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

    # Request for required data for search
    data_type = input("""
Options: [Username] [Car ID] [Price] [Days] [Total Amount] 

What is the data type you would like to seek for: """).lower()
    search_phrase = input("Enter keyword to search: ")

    # Display related data based on search_phrase in customer payment statement
    index = 0
    line_num = 1
    emp_spotter = []
    cus_pay_header()
    for customer in customers:
        if search_phrase == customer[data_type] and customer['status'] == 'Paid':
            emp_spotter.append(index)
            print("{:<4}{:<10}{:<9}{:<7}{:<8}RM{:<9}{:<9}{:<5}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'],
                          customer['payment method']))
            index += 1
            line_num += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("There is no relevant data for the records of customer payment related to your search keyword.")

        # Ask for admins' options in continue searching or return to administrator main screen
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

    # Admins' option on redirection
    search_redirect()


# 4.2 Continue at search menu or back to administrator main screen.
def search_redirect():
    # Ask for admins' preference in redirection
    option = int(input("""
Do you want to return to the search menu or administrator main screen?

1: Search menu
2: Administrator Main screen

Option =>\t"""))

    # Return back to the search menu
    if option == 1:
        print("\nYou will be redirected to the search menu shortly....\n")
        return admin_search()

    # Return to the administrator main screen
    elif option == 2:
        print('\nYou will be redirected to the administrator main screen shortly...\n')
        return administrator_system()

    # Invalid input, ask for input again
    else:
        print("\nInvalid input, please select 1 or 2.\n")
        return search_redirect()


# 5. Return a Rented Car.
def admin_return_rent():
    # Extract customer booking / payment to dictionaries in list
    customer_statement = {}
    customers = []
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

        # Display data that required to be return to the system
        index1 = 0
        line_num = 1
        index_collector = []
        cus_statement_header()
        for customer in customers:
            if customer['status'] == 'Paid' and customer['reservation'] == 'Renting':
                index_collector.append(index1)
                print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
                      .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                              int(customer['price']) * int(customer['days']), customer['status'],
                              customer['reservation'], customer['payment method']))
                index1 += 1
                line_num += 1
            else:
                index1 += 1
                continue

    # If the data is empty or no data to display
    if not index_collector:
        print("There is no relevant data for records of cars that should be return to the system.\n"
              "Redirecting to the administrator main screen...\n")

        # Automatically redirect to administrator main screen
        administrator_system()

    # Choose statement to return the rented car
    return_rent = int(input("\nWhich statement you would like to return the rent car (line of statement): "))
    index_value = index_converter(return_rent)
    new_index = index_collector[index_value]
    customers[new_index]['reservation'] = 'Completed'
    car_id = customers[new_index]['car id']

    # Extract car data to dictionaries in list
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

        # Find for cars that status should be changed to 'Open'
        for car in cars:
            if car['car_id'] == car_id:
                open_index = index2
                index2 += 1
            else:
                index2 += 1
                continue

    # Set car status to 'Open'
    cars[open_index]['status'] = 'Open'

    # Update data in text files
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

    # Display updated data
    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM {:<8}{:<9}{:<13}{:<8}"
          .format(customers[new_index]['username'], customers[new_index]['car id'], customers[new_index]['price'],
                  customers[new_index]['days'], int(customers[new_index]['price']) * int(customers[new_index]['days']),
                  customers[new_index]['status'], customers[new_index]['reservation'],
                  customers[new_index]['payment method']))

    # Ask for admins' preference in continuing returning car or back to administrator's main screen
    def cont_return():
        option = input("\nContinue returning rent car?\n\t[YES] or [NO]\n"
                       "[NO] to be redirected to administrator main screen\n\nOption=>\t").upper()
        # Continue return rent
        if option == 'YES':
            admin_return_rent()

        # Return to the administrator functionalities main screen
        elif option == 'NO':
            print('Returning to administrator main screen...')
            administrator_system()

        # Invalid input, ask for input again
        else:
            print("Invalid input, please insert YES or NO.\n")
            return cont_return()
    # Call function to execute
    cont_return()


# 6: Mark a car as Ready after the car is available upon customer's payment on confirmation for booking.
def admin_mark_ready():
    # Extract customers' booking / payment statement to dictionaries in list
    customer_statement = {}
    customers = []
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

    # Display data that required to be mark as 'Ready'
    index1 = 0
    line_num = 1
    index_collector = []
    cus_statement_header()
    for customer in customers:
        if customers[index1]['status'] == 'Paid' and customers[index1]['reservation'] == 'In Queue':
            index_collector.append(index1)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'],
                          customer['reservation'], customer['payment method']))
            index1 += 1
            line_num += 1
        else:
            index1 += 1
            continue

    # There is no data to be marked ready
    if not index_collector:
        print("\nNo data had been identified which require the action of marking the car status as ready.")

        # Automatically return to the administrator main screen
        print("Returning to administrator main screen...")
        administrator_system()

    # Choose and update car to be ready for paid booking
    return_rent = int(input(
        "\nWhich statement you would like to mark as ready upon customer's booking on confirmation towards booking: "))
    index_value = index_converter(return_rent)
    new_index = index_collector[index_value]
    customers[new_index]['reservation'] = 'Ready'

    # Update text file
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

    # Display returned rent car
    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM {:<8}{:<9}{:<13}{:<8}"
          .format(customers[new_index]['username'], customers[new_index]['car id'], customers[new_index]['price'],
                  customers[new_index]['days'], int(customers[new_index]['price']) * int(customers[new_index]['days']),
                  customers[new_index]['status'], customers[new_index]['reservation'],
                  customers[new_index]['payment method']))

    # Ask for admins' preference in continue marking ready or return to administrator main screen.
    def cont_modify_or_not():
        option = input("""\nDo you wish to mark more cars as ready?
        
\t[YES] or [NO]
[NO] to navigate back to the administrator main screen.
    
Option =>\t""").upper()

        # Continue marking ready
        if option == 'YES':
            print("\nYou are returning to the marking ready page,please be patient..\n")
            admin_mark_ready()

        # Return to administrator main screen
        elif option == 'NO':
            print("\nYou will be redirected to the administrator main screen..\n")
            administrator_system()

        # Invalid input, ask for admins' choice again
        else:
            print("\nInvalid input, please select either 1 or 2.\n")
            return cont_modify_or_not()

    # Call function to execute
    cont_modify_or_not()


# 7. Analytics Dashboard
def analytics_dashboard():
    # Extract customer booking / payment statement to dictionaries in list
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

    # Extract car data to dictionaries in list
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

    # Extract customer details to dictionaries in list
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

    # Retrieve all customer payment total amount
    payment_amount = []
    for customer in customers1:
        if customer['status'] == 'Paid':
            total = int(customer['days']) * int(customer['price'])
            payment_amount.append(total)

    # Obtain highest / lowest / total payment completed in the system
    max_paid = max(payment_amount)
    min_paid = min(payment_amount)
    total_paid = sum(payment_amount)

    # Display analytics information in a dashboard format
    print(f"""
{decoration()} OCRS Data Analytics Dashboard {decoration()}

Total cars:                         {len(car_holder)} cars
Total customers:                    {len(customers2)} customers
Total booking / payment records:    {len(customers1)} statements
Total sales / profits:              RM {total_paid}
Highest sales / profits:            RM {max_paid}
Lowest sales / profits:             RM {min_paid}

Keep up your great work! \U0001F592

Returning to administrator system....""")
    administrator_system()


# Section F : Customer
# 1. Customer landing page
def customer_interface():
    option = int(input("""As a visitor, select your action.

1: View all cars with any status.
2: Membership Registration \t - get access to more features.
3: Registered customers' section.
4: Exit the system.

Option  =>\t"""))

    # Execute system based on option
    if option == 1:
        view_cars()
        cont_main_menu()
    elif option == 2:
        cus_reg_header()
    elif option == 3:
        registered_login()
    elif option == 4:
        exit_system()

    # Error if integers 1 to 4 are not entered, customers can try entering again
    else:
        print("Invalid input, please insert valid value (1 to 4): ")
        return customer_interface()


# 2. Redirect customer landing page, login or register
def cont_main_menu():
    redirect = int(input("""\nDo you wish to go back to the main menu or login for more functionalities?
    
1: Main menu
2: Proceed to log in
3: Proceed to registration (For customer with no account in the server)

Option =>\t"""))

    # Executes according to customer's option
    if redirect == 1:
        print("\nReturning to the main menu...")
        return customer_interface()
    elif redirect == 2:
        print("\nRedirecting to the customer log in page....")
        return registered_login()
    elif redirect == 3:
        print("\nRedirecting to the customer registration page....")
        return customer_registration()
    # Error if integers form 1 to 3 are not entered, customers can try entering again
    else:
        print("\nInvalid input, please select either 1, 2 or 3.")
        return cont_main_menu


# 3. Customer Registration
def customer_registration():
    # Request for customers' username and password for registration
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Open text file for validation and insertion
    with open("customerDetails.txt", 'r') as existing, open("customerDetails.txt", 'a') as new_customer:
        # Check whether the username is taken by other customer, duplicate usernames are not allowed
        check = existing.read()
        if username in check:
            print("\nThis username had been used, please use another username.\n")
            return customer_registration()

        # Obtaining and inserting new users data into customerDetails.txt as a record
        else:
            print("\nPlease fill in the following details to provide more information to rent a car / cars.\n")
            address = input("Address: ")
            contact_number = input("Contact number: ")
            new_customer.write(f"\nusername: {username}\npassword: {password}\naddress: {address}"
                               f"\ncontact number: {contact_number}")
            print(decoration(), " Thank you for registering ", decoration(), "\n")

            # Every newly registered customer will have RM 0 as their balance
            balance = 0
            print("Your balance is now: ", balance, "\nYou can recharge it from the customer functionalities page.")
            new_customer.write(f"\nbalance: {balance}")
    print("\nYou can login to the system now. Start renting your car! :D\n")

    # Automatically redirect to customer landing page
    customer_interface()


# 4. Customer Log in
def registered_login():
    # Log in attempts starts counting,  after 3 attempts customer will be terminate out of the login system
    for time in range(1, 4):
        # Request for customers' username and password
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")

        # Extract customer details to dictionaries in list
        customer_details = {}
        customers = []
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

        # Username and password validation based on customers' input
        for customer in customers:
            if username == customer['username'] and password == customer['password']:
                print("\n", decoration(), " Welcome to the OCRS, ", username, decoration(), "\n")
                reg_customer()
                break

        # Customers who keyed in the wrong username or password will be asked to try again
        else:
            print("\nInvalid username or password, please try again...")

            # Confirming whether the customer has an existing account or not
            def registration_inquiry():
                register_confirm = input("""
Do you have an account? [YES] or [NO]

Option =>\t""").upper()

                # With account, customers can try again if they have an existing account
                if register_confirm == "YES":
                    print("Please try again.")
                    return registered_login()

                # Without account, customers will be asked on whether to create a new account or not
                elif register_confirm == "NO":
                    def register_account_ask():
                        register_account = input("\nDo you wish to register a new account? [YES] or [NO]:\t")

                        # Customers will be redirected to the registration page
                        if register_account == "YES":
                            print("Redirecting to the customer registration page...\n")
                            cus_reg_header()

                        # Customers will be sent back to the customer landing page
                        elif register_account == 'NO':
                            print("\nReturning to the customer landing page..\n")
                            customer_interface()

                        # Invalid input, ask for option again
                        else:
                            print("Invalid input, please key in [YES] or [NO].")
                            return register_account_ask()
                    register_account_ask()

                # Invalid input, ask for input again
                else:
                    print("\nInvalid input, please select [YES] or [NO].")
                    return registration_inquiry()
            registration_inquiry()

    # The customer will be redirected back to the landing page after 3 attempts
    else:
        print("\nYou had exceeded the limit to log in your account..Please try again after 1 minute..\n"
              "Redirecting to customer landing page....\n")
        return customer_interface()


# 5. Customer functionalities menu
def reg_customer():
    print(decoration()*2, "Functionalities Page", decoration()*2)

    # Request for users input
    option = int(input("""
What would you like to perform?

1: View all available car for rent.
2: Modify personal details.
3: View personal rental history.
4: Book a car.
5: Pay the car that you booked earlier.
6: Top up your balance.
7: Claim car that is Ready to be rented
8: Exit the portal. 

Option =>\t"""))

    # Executes based on the options entered from customers
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
        car_claim()
    elif option == 8:
        exit_system()

    # Invalid input and request for input again
    else:
        print("Invalid choice, please enter valid value (1 to 6).\n")
        return reg_customer()


# Section F01: Registered customers' functionalities
# 1. Display all available to rent cars.
# Retrieve car that is available to be rented out
def rent_car_details():
    # Extract car data to dictionaries in list
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

    # Displaying cars based on the "open" status
    index = 0
    line_num = 1
    status = "Open"
    car_header()
    for car in car_holder:
        if status == car_holder[index]['status']:
            print("{:<4}{:<7}{:<12}{:<11}{:<10}{:<6}{:<8}{:<5}"
                  .format(line_num, car['car_id'], car['car_brand'], car['car_name'], car['car_plate'], car['year'],
                          car['status'], car['price']))
            index += 1
            line_num += 1
        else:
            index += 1
            continue


# View detail of cars to be rented out.
def dis_all_rent():
    rent_car_details()

    # ask to book car or back to the main menu from the open status cars
    def cont_book_car():
        # Request customers' option in directly book a car or back to customers' functionalities menu
        car_booking = int(input("""
Do you want to proceed to book a car or return to the functionalities menu?

    1: Booking
    2: Customers functionalities menu

Option =>\t"""))

        # Executes based on the customer's option
        if car_booking == 1:
            print("Redirecting to booking page...")
            book_car()
        elif car_booking == 2:
            print("Returning to main menu...")
            reg_customer()

        # Invalid input, ask for customers' option again
        else:
            print("Invalid input, please select either [YES] or [NO]")
            return cont_book_car()

    # Call function to execute
    cont_book_car()


# 2. Modify personal details
def modify_details():
    # Request customers' username to proceed in profile modification
    username = input("Your username is requested to check your credential for profile modification: ")

    # Extract customers' details to dictionaries in list
    customer_details = {}
    customers = []
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

    # Customers' username validation
    index = 0
    for customer in customers:
        if customers[index]['username'] == username:
            cus_index = index
            for key, value in customer.items():
                print(f'{key}: {value}')
            break
        index += 1

    # Display when the username is not in the file
    else:
        print("\nUsername is unidentified...Please try again...\n")
        return modify_details()

    # Customers' details modification
    data_type = ['Password', 'Address', 'Contact Number']
    print("\nIMPORTANT! Note that username is immutable.\nOptions: {}".format(data_type).replace("\'", " "))

    # Modify desired attributes and values
    modify_type = input("\nWhich type of data you would like to change: ").lower()
    old_data = customers[cus_index][modify_type]
    print("Original data: ", old_data)
    new_data = input("Replace with: ")
    customers[cus_index][modify_type] = new_data

    # Update new data into the text file
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

    # Continue profile modification?
    def cont_modify():
        continue_or_not = input("""Continue modifying?
[YES] or [NO]
[NO] will navigate you back to the customer functionalities page

Option =>\t""").upper()

        # Redirected to modify customer details again
        if continue_or_not == 'YES':
            print("\nUpdating modified data...\n"
                  "Continue modification based on new data and your credential will be requested again\n")
            return modify_details()

        # Redirected back to the customer functionalities menu
        elif continue_or_not == 'NO':
            print("\nYou will be redirected to the customer functionalities page...")
            return reg_customer()

        # Invalid input, ask for customers' option again
        else:
            print("\nInvalid input, only [YES] or [NO] allowed.\n")
            return cont_modify()

    # Call function to execute
    cont_modify()


# 3. View personal rental history
def rental_hist():
    # Extract customer booking details into dictionaries in list
    customer_statement = {}
    customers = []
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

    # Enter username to confirm identity
    print("\nIMPORTANT!! You are going to access customers' private data.\n")
    username = input("Enter your credential username: ")

    # username validation and print
    index = 0
    emp_spotter = []
    cus_statement_header()
    for customer in customers:
        if username == customer['username']:
            emp_spotter.append(index)
            print("   {:<11}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<8}"
                  .format(customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'], customer['reservation'],
                          customer['payment method']))
            index += 1
            continue
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThe rental history is empty, start to rent a car! :)")

    # Automatically redirect back to the customer functionalities screen
    print("\nYou will be redirected to the functionalities page...\n")
    reg_customer()


# 6. Select and Book a car for a specific duration.
def book_car():
    # Display details on available cars
    rent_car_details()

    # Select car ID
    select_car = input("\nSelect the car ID you would like to book: ")

    # Enter username to confirm
    username = input("Enter your username to request your booking: ")

    # Extract car details to dictionaries in list
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

    # Change the status of the car to "booked"
    for car in car_holder:
        if car['car_id'] == select_car:
            price = car['price']
            car['status'] = 'Booked'
            break

    # Ask to book for how many days
    days = int(input("How many day(s) you would like to book it: "))

    # Update new data into the text file
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

    # Automatically redirect to customer functionalities page
    print("\nYou will be redirected to the customer functionalities page.\n\n"
          "You can make your payment by choosing option 5 to confirm your booking.")
    return reg_customer()


# 7. Do payment to confirm Booking.
def pay_car():
    # Extract car details to dictionaries in list
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

    # Extract customer booking details into dictionaries in list
    customer_statement = {}
    customers = []
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

    # Enter username to confirm booking
    username = input("\nEnter your username to pay for your booking confirmation: ")

    index = 0
    new_index = []
    line_num = 1
    for customer in customers:
        # Display booking that need to be paid
        if username == customer['username'] and customer['status'] == 'Pending' and customer['payment method'] == 'N/A':
            new_index.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'], customer['reservation'],
                          customer['payment method']))
            line_num += 1

        # Display pay with balance statement / Redirected to pay with balance
        elif username == customers[index]['username'] and customers[index]['status'] == 'Pending' \
                and customers[index]['payment method'] == 'balance':
            print("    {:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<8}"
                  .format(customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'], customer['reservation'],
                          customer['payment method']))
            pay_balance()
        else:
            index += 1

    # No data spotted
    if not new_index:
        print("\nInvalid username or customer does not have a booking request.")

        # Ask to continue to pay or not
        def cont_pay():
            option = input("\nContinue payment?\n\t[YES] or [NO]\n"
                           "[NO] return to customer functionalities page\n=>\t").upper()

            # Return to payment page
            if option == 'YES':
                print("\nReturning to the payment page...")
                pay_car()

            # Return to customer functionalities page
            elif option == 'NO':
                print("\nYou will be redirected to the functionalities page shortly....\n")
                reg_customer()

            # Invalid input, ask for option again
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_pay()
        cont_pay()

    # Select the booking that customers wish to pay
    pay_statement = int(input("\nWhich booking statement (line) you would like to pay? "))
    statement_index = index_converter(pay_statement)
    pay_index = new_index[statement_index]
    car_id = customers[pay_index]['car id']

    # Request customers to select their preferred payment method
    print("\nIMPORTANT!! Note that you will need to make full payment to confirm your booking.\n")
    payment_method = input("""What would you like to use to pay the booking?
[credit card] [balance]
=>\t""").lower()

    # Update data
    customers[pay_index]['payment method'] = payment_method

    # Update new data to the text file
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

    # Credit card payment method
    if payment_method == 'credit card':
        print("\nNote that your private information in this area will not be stored in our cookies.\n")
        credit_card_num = input("Enter your credit card number: ")
        cvv = input("Enter your credit card's CVV: ")
        expiry_date = input("Enter your credit card's expiry date: ")

        # Display payment details
        print(f"""
Transaction completed...

{decoration()} Payment details {decoration()}

Paid amount: {int(customers[pay_index]['price']) * int(customers[pay_index]['days'])}
Credit card: {credit_card_num}
""", )
        # Update data
        customers[pay_index]['status'] = 'Paid'
        customers[pay_index]['reservation'] = 'In Queue'

        for car in car_holder:
            if car["car_id"] == car_id:
                car["status"] = 'Rented'

        # Update new data to the text file
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
            # Transfer new car data into the text file
            for information in car_holder:
                for key in information:
                    if count2 < len(car_holder) * 7:
                        list_of_strings = f'{key}: {information[key]}'
                        mark_rented.write(f'{list_of_strings}\n')
                        count2 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        mark_rented.write(f'{list_of_strings}')

        # Automatically redirect to the customer functionalities page
        print("\nRedirecting to customer functionalities page...\n")
        reg_customer()

    # Redirect to balance payment page
    elif payment_method == 'balance':
        pay_balance()

    # Invalid input, reboot car payment page
    else:
        print("Invalid input, due to privacy you will be redirected to the car payment statement page again...")
        return pay_car()


# Pay with balance
def pay_balance():
    # Request username
    username = input("\nYou are accessing your online balance, enter your username to make sure that is you: ")

    # Extracts customer Details into dictionaries in list
    customer_details = {}
    customers = []
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

    # Verifying username
    index1 = 0
    for customer in customers:
        if customer['username'] == username:
            new_index1 = index1
            balance = int(customer["balance"])
            break
        index1 += 1

    # Extracts customer booking/payment details into dictionaries in list
    customer_pay = {}
    statements = []
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

    # Search for relevant payment / booking statement
    index2 = 0
    for statement in statements:
        if username == statement['username'] and statement['payment method'] == 'balance' \
                and statement['status'] == 'Pending':
            new_index2 = index2

            # Calculating the total amount customers should pay
            total = int(statement['price']) * int(statement['days'])
            car_id = statement['car id']

            # Display how much the customer should pay and car ID
            print("You have to pay: RM", total, "\nCar ID: ", statement['car id'])
        index2 += 1

    # Extracts car details to dictionaries in list
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

    # Deduct from balance if it is more than total
    if balance >= total:
        balance -= total

        # Display remaining balance
        print("\nCurrent balance: ", balance, "\nYou had paid the booking confirmation."
                                              "\nTransaction completed. Your current balance is", balance)

        # Change data to paid situation
        customers[new_index1]["balance"] = str(balance)
        statements[new_index2]['status'] = 'Paid'
        statements[new_index2]['reservation'] = 'In Queue'
        statements[new_index2]['payment method'] = 'balance'

        # Change specified car status to rented after payment
        for car in car_holder:
            if car['car_id'] == car_id:
                car['status'] = 'Rented'
                break

        # Update new data to the text file
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

        # Automatically redirect to customer functionalities page
        print("\nRedirecting to customer functionalities page...\n")
        reg_customer()

    # Insufficient balance to pay will be automatically redirected to the top up screen
    elif balance < total:
        print("\nYour balance is insufficient...\nYour current balance: RM", balance,
              "\n\nYou will need to top up before paying your booking confirmation."
              "\nRedirecting to top up system....\n")
        top_up_header()


# 8. Top up your balance.
def top_up():
    # Extract customer details to dictionaries in list
    customer_details = {}
    customers = []
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

    # Request username
    username = input("\nEnter your username to check your current balance: ")

    # Display current balance based on username
    index = 0
    for customer in customers:
        if customer['username'] == username:
            cus_index = index
            balance = int(customer['balance'])
            print("Your current balance: ", str(balance))
            break
        else:
            index += 1
            continue
    # Error message if username does not exist and request username again
    else:
        print("Invalid username, please try again.")
        top_up()

    # Select desired payment method
    payment_method = int(input(f"""Which payment method do you prefer to top up your balance with? 

1: Credit/debit card 
2: FPX online banking

Option =>\t"""))

    # Credit card payment method
    if payment_method == 1:
        print("\n", decoration() * 3, "\nTop up with: Credit/debit card\n", decoration() * 3)
        credit_card_num = input("Enter your credit/debit card number: ")
        cvv = input("Enter your credit/debit card's CVV: ")
        expiry_date = input("Enter your credit/debit card's expiry date: ")
        print("\nTop up completed with ", credit_card_num)

    # FPX online banking payment method
    elif payment_method == 2:
        print("\n", decoration() * 3, "\nTop up with: FPX online banking\n", decoration() * 3)

        # Bank options to proceed payment in FPX
        def bank_options():
            bank_choice = int(input(f"""Select your merchant:

1: Maybank
2: Public Bank
3: Ambank 
4: RHB Bank
5: CIMB Bank

Option =>\t"""))

            # Execute based on options by customers
            if bank_choice <= 5:
                account_no = input("Enter your bank account number: ")
                account_password = input("Enter your bank account password: ")
                print("\nTop up with", account_no)

            # Error if numbers less than 5 are not entered and request bank again
            else:
                print("Invalid input, please select in range 1 to 5.")
                return bank_options()
        bank_options()

    # Request top up amount
    top_up_value = int(input("How much do you want to top up: "))
    balance += top_up_value
    customers[cus_index]['balance'] = str(balance)
    print("Top up success, current balance: ", customers[cus_index]['balance'])

    with open('customerDetails.txt', 'w') as top_up_file:
        # Transfer new data into the text file
        for information in customers:
            for key in information:
                list_of_strings = f'{key}: {information[key]}'
                top_up_file.write(f'{list_of_strings}\n')

    # Continue top up?
    def cont_top_up():
        cont_or_not = input("""
Do you wish to top up more? 
[YES] or [NO]
[NO] will redirect you back to the functionalities main menu.

Option =>\t""").upper()
        # Execute choices made by customers
        if cont_or_not == "YES":
            print("Redirecting back to the top up section....")
            top_up()
        elif cont_or_not == "NO":
            print("\nRedirecting to the customer functionalities main menu...\n")
            reg_customer()
        # Invalid input and request for customers' option again
        else:
            print("Invalid input, please enter either [YES] or [NO]. ")
            return cont_top_up()
    cont_top_up()


# 9. Claim car that is ready to be rented
def car_claim():
    # Extracts customer booking/payment details into dictionaries in list
    customers = []
    customer_details = {}
    with open("customerBookingPayment.txt", 'r') as booking_details:
        for line in booking_details:
            row = line.strip().split(": ")
            customer_details[row[0]] = row[1]
            for customer in range(1, bookdb_line_count()):
                if row == "":  # empty line
                    break
                elif len(customer_details) == 7:
                    copy_data = customer_details.copy()
                    customers.append(copy_data)
                    customer_details = {}
                    continue

    # Request username to check car that is able to claim
    username = input("Enter your username to confirm your identity: ")

    # Display information based on username and fits the requirement to claim
    index1 = 0
    line_num = 1
    index_collector = []
    cus_statement_header()
    for customer in customers:
        if customer['username'] == username and customer['status'] == 'Paid' and customer['reservation'] == 'Ready':
            index_collector.append(index1)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']), customer['status'],
                          customer['reservation'], customer['payment method']))
            index1 += 1
            line_num += 1
        else:
            index1 += 1
            continue

    # No data spotted and automatically redirect to customer functionalities page
    if not index_collector:
        print("\nThere is no relevant data for records of cars that are available to claim.\n"
              "Redirecting to the customer functionalities menu...\n")
        reg_customer()

    # Select a car statement to claim
    claim_car = int(input("\nWhich statement you would like to claim your car (line of statement): "))
    index_value = index_converter(claim_car)
    new_index = index_collector[index_value]

    # Change status
    customers[new_index]['reservation'] = 'Renting'
    car_id = customers[new_index]['car id']

    # Extract car details to dictionaries in list
    car_details = {}
    cars = []
    with open("carDatabase.txt", 'r') as car_data:
        for line in car_data:
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

    # Change car status
    index2 = 0
    for car in cars:
        if car['car_id'] == car_id:
            car['status'] = 'Rented'
            index2 += 1
        else:
            index2 += 1
            continue

    # Update new data to text file
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

    # Display claimed car statement
    print("\nClaimed car statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM {:<8}{:<9}{:<13}{:<8}"
          .format(customers[new_index]['username'], customers[new_index]['car id'], customers[new_index]['price'],
                  customers[new_index]['days'], int(customers[new_index]['price']) * int(customers[new_index]['days']),
                  customers[new_index]['status'], customers[new_index]['reservation'],
                  customers[new_index]['payment method']))

    # Continue claiming cars or not?
    def cont_claim():
        cont_or_not = input("Do you wish to claim other cars you own? [YES] or [NO]").upper()

        # Execute options made by customers
        if cont_or_not == "YES":
            print("You will be redirected back to claim your other cars....")
            car_claim()
        elif cont_or_not == "NO":
            print("Returning to the customer functionalities menu....")
            reg_customer()

        # Invalid input, request option again
        else:
            print("Invalid input, you can only enter either 'YES' or 'NO'.")
            return cont_claim()
    cont_claim()

car_claim()
# Call function to execute the OCRS system
welcome()
