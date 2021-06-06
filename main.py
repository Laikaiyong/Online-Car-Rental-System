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


# Section B: Headers
# 1. Car data header
def car_header():
    # Headers
    car_headers = ['Car ID', 'Car Brand', 'Car Model',
                   'Car Plate', 'Year', 'Status', 'Price']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(car_headers) + 1)
    print("\n", format_row.format("", *car_headers))


# 2. Customer booking statement data header
def cus_book_header():
    # Headers
    cus_book = ['Username', 'Car ID', 'Price', 'Days',
                'Total Amount', 'Status', 'Reservation', 'Requested Rent Date']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(cus_book) + 1)
    print("\n", format_row.format("", *cus_book))


# 3. Customer payment statement data header
def cus_pay_header():
    # Headers
    cus_pay = ['Username', 'Car ID', 'Price', 'Days',
               'Total Amount', 'Status', 'Payment Method', 'Requested Rent Date']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


# 4. Customer statement data header
def cus_statement_header():
    # Headers
    cus_stmnt = ['Username', 'Car ID', 'Price', 'Days',
                 'Total Amount', 'Status', 'Reservation', 'Payment Method', 'Requested Rent Date']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(cus_stmnt) + 1)
    print("\n", format_row.format("", *cus_stmnt))


# 5. Customer registration page header
def cus_reg_header():
    print("\n", decoration(), "Welcome to the registration page", decoration(), "\n")

    # Direct to customer registration page
    customer_registration()


# 6. Customer top up page header
def top_up_header():
    print("\n", decoration(), "Welcome to the top up system.", decoration())

    # Direct to customer balance top up page
    top_up()


# Section C: Database/ Text File Data Management
# Read file
# 1. car database
def car_database_read():
    # Extract car data to a list
    try:
        index = 0
        cars = []
        index_collector = []
        with open("carDatabase.txt", 'r') as car_file:
            for line in car_file:
                index_collector.append(index)
                row = line.strip().split(" | ")
                cars.append(row)
                index += 1

    except:
        print("\nDatabase is corrupted..")

    return cars, index_collector


# 2. customer details
def customer_details_read():
    # Extract customer information to a list
    try:
        customers = []
        with open("customerDetails.txt", 'r') as customers_file:
            for line in customers_file:
                row = line.strip().split(" | ")
                customers.append(row)

    except:
        print("\nDatabase is corrupted..")

    return customers


# 3. customer booking / payment statement
def bookpay_stmnt_read():
    # Extract customer booking / payment statement to a list
    try:
        statements = []
        with open("customerBookingPayment.txt", 'r') as statement_file:
            for line in statement_file:
                row = line.strip().split(" | ")
                statements.append(row)

        for statement in statements:
            total = int(statement[2]) * int(statement[3])
            statement.append(total)

    except:
        print("\nDatabase is corrupted..")

    return statements


# Section D: General Users Interface
# 1. Welcome page with text display.
def welcome():
    print("\n", decoration(), "Welcome to the Online Car Rental System(OCRS) by Super Car Rental Services(SCRS)",
          decoration())

    # Menu
    print("""
Enter the number that best describe you.

    Admin : 1
    Customer : 2
    """)
    login_system()


# 2. Role definition pass
def login_system():
    # Ask for users' role
    def role_validation():
        try:
            role = int(input("Role => "))
            return role

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return role_validation()

    role = role_validation()
    # Administrator pass
    if role == 1:
        administrator_login()

    # Customer pass
    elif role == 2:
        customer_interface()

    # Error if neither 1 nor 2 are entered
    else:
        print("\nInvalid choice, please choose again.\n")
        return login_system()


# 3. Exit system
def exit_system():
    # Menu
    print("""
Are you sure you want to exit the Online Car Rental System?

    [YES] or [NO]

Note: Selecting [NO] will navigate you back to the welcome page.""")

    # Asking for exit confirmation
    confirmation = input("Option => ").upper()

    # Terminate the program
    if confirmation == "YES":
        print("\n", decoration(), "Exit", decoration(), "\n")
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
# Additional: When database corrupted and required to recreate one.
def maintenance_database_access():
    # Accessing database by verifying username and password
    maintenance_username = "SCRSLL001"
    maintenance_password = "SCRSOCRSLaiLim"

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Validation of username and password
    if username == maintenance_username and password == maintenance_password:
        print(f"\n{decoration()} Welcome administrator {decoration()}\n")

        def admin_create_file():
            # Options on new database if it is not created
            try:
                # Menu
                print("""What database you would like to create

1: Car Database
2: Customer information Database
3: Customer Booking / Payment Database
""")
                create_file = int(input("Option => "))

                # Execute based on the choices entered
                if create_file == 1:
                    create_car = open("carDatabase.txt", "w")
                    print(
                        "\nDatabase created, you will be redirected to the add car functionalities.")
                    create_car.close()
                    admin_add_car()
                elif create_file == 2:
                    create_user = open("customerDetails.txt", "w")
                    print(
                        "\nDatabase created, you will be redirected to the administrator main screen.")
                    create_user.close()
                    administrator_system()
                elif create_file == 3:
                    create_booking = open("customerBookingPayment.txt", "w")
                    print(
                        "\nDatabase created, you will be redirected to the administrator main screen.")
                    create_booking.close()
                    administrator_system()

                # Error message on inputing the shown value
                else:
                    print(
                        "Please insert a number from 1 to 3.\n")
                    return admin_create_file()

            # Exclude non numeric value
            except ValueError:
                print("\nPlease insert a numeric value.\n")
                return admin_create_file()

        admin_create_file()

    # Error message after selecting a non existent choice
    else:
        print("\nPlease try again.\n")
        return maintenance_database_access()


# 1. Administrator login page
def administrator_login():
    # request for admins username and password
    administrator_username = "SCRSLL001"
    administrator_password = "SCRSOCRSLaiLim"

    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    # username and password validation
    if username == administrator_username and password == administrator_password:
        administrator_system()
    else:
        print("Invalid credential, please check your username and password.")
        return administrator_login()


# 2. Administrator access system
def administrator_system():
    # Admins welcome line
    print("\n", decoration(), "Welcome, administrator!", decoration())

    # Admins functionalities menu
    def admin_function_validation():
        try:
            # Menu
            print("""
Choose the action you want to perform:

1: Add cars to be rented out.
2: Modify car details.
3: Display records.
4: Search specific record.
5: Return a rented car.
6: Mark a car as Ready upon customer's booking confirmation.
7: OCRS Data Analytics Dashboard
8: Exit the system.
""")
            option = int(input("Select your action: "))

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
                return admin_function_validation()

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return admin_function_validation()

    admin_function_validation()


# Section E01: Administrator functionalities
# 1. Add car
def admin_add_car():
    # Extract car data to a database that store a list
    try:
        cars = car_database_read()[0]

    # No file identified
    except:
        print("Access the database system to check database progress\n")
        maintenance_database_access()

    # Menu
    print("""
Insert car data:
[YES] to continue
[NO] to stop and display all data. then redirected to admin main screen.
""")

    # Add car choice
    add_or_not = input("Option => ").upper()

    # Auto generate the new car id
    last_car_id = cars[-1][0].split("R")
    new_car_id_num = int(last_car_id[1]) + 1

    # Add car while admins choose 'yes'
    if add_or_not == "YES":
        new_car_details = []
        new_car_id = 'R' + f'{new_car_id_num:03d}'
        print("Car ID: ", new_car_id)
        new_car_brand = input("Enter car brand: ")
        new_car_model = input("Enter car model: ")
        new_car_plate = input("Enter car plate: ")
        new_year = input("Enter car manufacture year: ")
        new_status = input("Enter status [Open / Rented / X / Booked]: ")

        def new_price_validation():
            try:
                new_price = int(
                    input("Enter price per day (Only numeric data): "))
                return new_price

            # Exclude non numeric value
            except ValueError:
                print("\nInvalid input, please insert a numeric value..\n")
                return new_price_validation()

        new_price = new_price_validation()

        new_car_details.extend([new_car_id, new_car_brand,
                               new_car_model, new_car_plate, new_year, new_status, str(new_price)])

        # Append the new car data into carDatabase text file
        try:
            count = 1
            with open('carDatabase.txt', "a") as admin_add_details:
                admin_add_details.write("\n")
                for detail in new_car_details:
                    if count < len(new_car_details):
                        count += 1
                        admin_add_details.write(f"{detail} | ")
                    else:
                        admin_add_details.write(detail)
            print("\nInsert completed... Processing...\n")

        # No file identified
        except:
            print("Access the database system to check database progress\n")
            maintenance_database_access()

        # Ask for admins choice on inserting more cars or stop adding
        return admin_add_car()

    # Stop adding car and display all cars
    elif add_or_not == "NO":
        print("\nDisplaying all data...")
        view_cars()
        print("\n", decoration(),
              " Back to administrator main screen. ", decoration())
        administrator_system()

    # Invalid choice and ask for choice again
    else:
        print("Invalid input, please try again.")
        return admin_add_car()


# 2. Modify car
def admin_modify():
    # Display all cars data
    view_cars()

    # Extract car data to a variable that hold a list
    try:
        cars = car_database_read()[0]
        cars_index = car_database_read()[1]

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Ask for modification required details
    def data_line_validation():
        try:
            data_line = int(
                input("\nWhich line of data you want to perform the modification: "))
            car_index_convert = index_converter(data_line)
            car_index = cars_index[car_index_convert]

            if data_line <= 0:
                print("Invalid input, please try again.")
                return data_line_validation()

            else:
                return car_index

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..")
            return data_line_validation()

        # Exclude non existent records
        except IndexError:
            print("\nCar line is out of range.")
            return data_line_validation()

    car_index = data_line_validation()
    print("\nIMPORTANT!!! Note that uniqueID can't be modified. "
          "\nIf the car had been removed from the system place X in rent status.\n")

    def data_type_validation():
        # Ask for desired data type
        item = input("Modify data type (e.g. Car Model, Price): ").replace(
            " ", '_').lower()

        if item == "car_brand":
            index = 1
            origin_word = cars[car_index][index]

        elif item == "car_model":
            index = 2
            origin_word = cars[car_index][index]

        elif item == "car_plate":
            index = 3
            origin_word = cars[car_index][index]

        elif item == "year":
            index = 4
            origin_word = cars[car_index][index]

        elif item == "status":
            index = 5
            origin_word = cars[car_index][index]

        elif item == "price":
            index = 6
            origin_word = cars[car_index][index]

        elif item == "car_id":
            print("\nInvalid choice, car id is immutable.\n")
            return data_type_validation()

        else:
            print(
                "\nInvalid data type, please choose according to the data headers displayed other than car id.\n")
            return data_type_validation()

        return origin_word, index

    # Extract and display original data
    origin_word, replace_index = data_type_validation()
    print("Origin data: ", origin_word)

    # Replace data
    replace_word = input("Replaced by:  ")
    cars[car_index][replace_index] = replace_word

    # Display updated data
    print("\nDisplaying updated data.\n")
    car_header()
    print("   {:<8}{:<11}{:<11}{:<10}{:<7}{:<9}{:<6}"
          .format(cars[car_index][0], cars[car_index][1], cars[car_index][2], cars[car_index][3], cars[car_index][4], cars[car_index][5], cars[car_index][6]))

    # Transfer new data to the text file
    with open('carDatabase.txt', 'w') as modified:
        car_count = 1
        for car in cars:
            if car_count < len(cars):
                count = 1
                for details in car:
                    if count < len(car):
                        modified.write(f"{details} | ")
                        count += 1
                    else:
                        modified.write(details)
                modified.write("\n")
                car_count += 1
            else:
                count = 1
                for details in car:
                    if count < len(car):
                        modified.write(f"{details} | ")
                        count += 1
                    else:
                        modified.write(details)

    # Ask for admins' preferences on continue editing / modify data

    def cont_or_no():
        print("""
Continue modifying?

    [YES] or [NO]

Note: Selecting [NO] will redirect you back to the administrator main menu.""")
        continue_or_not = input("Option => ").upper()

        # Continue modification
        if continue_or_not == 'YES':
            print("\nContinue modification based on new data.")
            return admin_modify()

        # Stop modification and return to administrator functionalities menu
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
    def display_validation():
        try:
            # Menu
            print("""
Display data choice:

1. All Cars
2: Cars Availability
3: Customer Bookings
4: Customer Payment for a specific time duration
5: Registered customers' username in the system
6: Exit to administrator main screen.
""")
            dis_option = int(input("Option => "))
            return dis_option

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return display_validation()

    dis_option = display_validation()

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


# 3.1 Continue to display menu or administrator page.
def display_redirect():
    # Ask for admins' preference in redirection
    def redirect_validation():
        try:
            print("""
Do you wish to return to the display menu or administrator's main screen?

1: Display Menu
2: Administrator Main Screen
""")
            option = int(input("Option=> "))
            return option

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..")
            return redirect_validation()

    option = redirect_validation()

    # Return to the display menu
    if option == 1:
        print("\nYou will be redirected to the display menu...")
        admin_display()

    # Return to administrator functionalities main screen
    elif option == 2:
        print("\nYou are returning to the administrator main screen....")
        administrator_system()

    # Invalid input, ask for redirection option again
    else:
        print("\nInvalid input, please key in 1 or 2.\n")
        return display_redirect()


# 3.2 All display dataset
# 1. View all car data
def view_cars():
    # Extract car data to a list
    try:
        cars = car_database_read()[0]

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Display all car data
    car_header()
    line_num = 1
    for car in cars:
        print("{:<4}{:<7}{:<12}{:<11}{:<10}{:<6}{:<8}{:<5}"
              .format(line_num, car[0], car[1], car[2], car[3], car[4], car[5], car[6]))
        line_num += 1


# 2. Display car with different status
def dis_rent_car():
    # Extract car data to in list
    try:
        cars = car_database_read()[0]

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Menu
    print("\nCategories available [Open] [Rented] [X] [Booked]\n")

    # Request status
    status = input(
        "Status => ").capitalize()

    available_status = ["Open", "Rented", "X", "Booked"]

    # Display cars with matching status
    if status in available_status:
        index = 0
        emp_spotter = []
        line_number = 1
        car_header()
        for car in cars:
            if status == car[5]:
                emp_spotter.append(index)
                print("{:<4}{:<7}{:<12}{:<11}{:<10}{:<6}{:<8}{:<5}"
                      .format(line_number, car[0], car[1], car[2], car[3], car[4], car[5], car[6]))
                index += 1
                line_number += 1
            else:
                index += 1
                continue
    else:
        print("\nInvalid type of status, please choose again.")
        return dis_rent_car()

    # No data spotted
    if not emp_spotter:
        print(
            "\nThere is no relevant data for records of cars on that particular status.\n")

        # Admins' option on redirection
        display_redirect()

    # Admins' option on redirection
    display_redirect()


# 3. Display customer booking statement
def dis_cus_booking():
    # Extract customer booking / payment statement to a list
    try:
        statements = bookpay_stmnt_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Set reservation only specify on booking status
    reservation = ('In Queue', 'Ready')

    # Display matching customer booking statement
    index = 0
    line_number = 1
    emp_spotter = []
    cus_book_header()
    for statement in statements:
        if reservation[0] == statement[5] or reservation[1] == statement[5]:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<12}{:<10}"
                  .format(line_number, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[7]))
            index += 1
            line_number += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for records of customer booking statement.\n")

        # Admins' option on redirection
        display_redirect()

    # Admins' option on redirection
    display_redirect()


# 4. Display customer payment statement
def dis_cus_pay():
    # Extract customer booking / payment statement to a list
    try:
        statements = bookpay_stmnt_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    def date_request_validation():
        # Menu instruction
        print("\nDisplay rent car between the start date and end date.\n")
        try:
            # request start date
            start_date = input(
                "Insert the start date in DD/MM/YYYY Format: ").split("/")
            start_day, start_month, start_year = int(
                start_date[0]), int(start_date[1]), int(start_date[2])
            start_date = (start_year, start_month, start_day)

            # request end date
            end_date = input(
                "Insert the end date in DD/MM/YYYY Format: ").split("/")
            end_day, end_month, end_year = int(
                end_date[0]), int(end_date[1]), int(end_date[2])
            end_date = (end_year, end_month, end_day)

            if start_month not in range(1, 13) or end_month not in range(1, 13):
                print("\nInvalid date input, please insert a valid date.\n")
                return date_request_validation()

            else:
                return start_date, end_date

        except:
            print("\nInvalid input, please insert a date in DD/MM/YYYY Format.")
            return date_request_validation()

    start_date, end_date = date_request_validation()

    # Set statement status only specify on 'Paid'
    status = 'Paid'

    # Display matching customer payment statement
    index = 0
    line_number = 1
    emp_spotter = []
    cus_pay_header()
    for statement in statements:

        # make a valid date
        try:
            date = statement[7].split("/")
            date_year, date_month, date_day = int(date[2]), int(
                date[1]), int(date[0])
            date = (date_year, date_month, date_day)

        # Skip N/A value
        except:
            pass

        if status == statement[4] and start_date <= date <= end_date:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<16}{:<10}"
                  .format(line_number, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[6], statement[7]))
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


# 5. Display all registered customer username
def registered_customer():
    # Extract customer details to variable that store a list
    try:
        customers = customer_details_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Store all customers' username in a list
    customers_names = []
    for customer in customers:
        customers_names.append(customer[0])

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


# 4. Search Record
def admin_search():
    # Admin's option database search
    def search_choice_validation():
        try:
            print("""
Choose database that you want to inspect / search:

    1: Customer Booking
    2: Customer Payment
""")
            file_choose = int(input("Option => "))
            return file_choose

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return search_choice_validation()

    file_choose = search_choice_validation()

    # Booking statement search
    if file_choose == 1:
        cus_book_search()

    # Payment statement search
    elif file_choose == 2:
        cus_pay_search()

    # Invalid input, ask for database option again
    else:
        print("Invalid input, choose only 1 or 2.\n")
        return admin_search()


# 4.1 Continue at search menu or back to administrator main screen.
def search_redirect():
    # Ask for admins' preference in redirection
    def option_validation():
        try:
            # Menu
            print("""
Do you want to return to the search menu or administrator main screen?

    1: Search menu
    2: Administrator Main screen
""")
            option = int(input("Option => "))
            return option

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return option_validation()

    option = option_validation()

    # Return back to the search menu
    if option == 1:
        print("\nYou will be redirected to the search menu shortly....\n")
        admin_search()

    # Return to the administrator main screen
    elif option == 2:
        print('\nYou will be redirected to the administrator main screen shortly...\n')
        administrator_system()

    # Invalid input, ask for input again
    else:
        print("\nInvalid input, please select 1 or 2.\n")
        return search_redirect()


# 4.2 Search data
# 1. Search on customer booking data
def cus_book_search():
    # Extract customer booking / payment statement to a variable that store a list
    try:
        statements = bookpay_stmnt_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Ask for data users want to search
    def data_type_validation():
        print("\nOptions: [Username] [Car ID] [Days]\n")
        data_type = input(
            "What is the data type you would like to seek for: ").lower()
        if data_type == "username":
            index = 0
        elif data_type == "car id":
            index = 1
        elif data_type == "days":
            index = 3

        else:
            print("Invalid input, please choose from the option.\n")
            return data_type_validation()
        return index

    type_index = data_type_validation()
    search_phrase = input("Enter keyword to search: ")
    reservation = ("In Queue", "Ready")

    # Display related records based on search_phrase in customer booking statement
    index = 0
    line_num = 1
    emp_spotter = []
    cus_book_header()
    for statement in statements:
        if search_phrase == statement[type_index] and statement[5] in reservation and statement[4] == "Paid":
            emp_spotter.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<12}{:<10}"
                  .format(line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[7]))
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
            # Menu
            print("""Continue searching?

    [YES] or [NO]

Note: Selecting [NO] will navigate you back to administrator main screen.
""")
            option = input("Option => ").upper()
            if option == 'YES':
                print("Returning back to the customer booking search page.")
                cus_book_search()
            elif option == 'NO':
                print(
                    "\nYou will be redirected to the functionalities page shortly....\n")
                administrator_system()

            # Invalid input, users can only select [YES] or [NO]
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_search_book()
        cont_search_book()

    # Admins' option on redirection
    search_redirect()


# 2. Search on customer payment data
def cus_pay_search():
    # Extract customer booking / payment statement to a variable that store a list
    try:
        statements = bookpay_stmnt_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

     # Ask for data users want to search
    def data_type_validation():
        # Menu
        print("\nOptions: [Username] [Car ID] [Days]\n")
        data_type = input(
            "What is the data type you would like to seek for: ").lower()
        if data_type == "username":
            index = 0
        elif data_type == "car id":
            index = 1
        elif data_type == "days":
            index = 3

        else:
            print("Invalid input, please choose from the option.\n")
            return data_type_validation()
        return index

    type_index = data_type_validation()

    search_phrase = input("Enter keyword to search: ")

    # Display related data based on search_phrase in customer payment statement
    index = 0
    line_num = 1
    emp_spotter = []
    cus_pay_header()
    for statement in statements:
        if search_phrase == statement[type_index] and statement[4] == 'Paid':
            emp_spotter.append(index)
            print("{:<4}{:<10}{:<9}{:<7}{:<8}RM{:<9}{:<9}{:<15}{:<10}"
                  .format(line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[6], statement[7]))
            index += 1
            line_num += 1
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThere is no relevant data for the records of customer payment related to your search keyword.\n")

        # Ask for admins' options in continue searching or return to administrator main screen
        def cont_search_pay():
            # Menu
            print("""Continue searching?

    [YES] or [NO]

Note: Selecting [NO] will navigate you back to administrator main screen.
""")
            option = input("Option=> ").upper()
            if option == 'YES':
                print("\nReturning back to the customer payment search page.")
                cus_pay_search()
            elif option == 'NO':
                print(
                    "\nYou will be redirected to the functionalities page shortly....\n")
                administrator_system()

            # Invalid input, only [YES] or [NO] is allowed
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_search_pay()
        cont_search_pay()

    # Admins' option on redirection
    search_redirect()


# 5. Return a Rented Car.
def admin_return_rent():
    try:
        # Extract customer booking / payment statement to a variable that store a list
        statements = bookpay_stmnt_read()

        # Extract car data to a database that store a list
        cars = car_database_read()[0]

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Display data that required to be return to the system
    index1 = 0
    line_num = 1
    index_collector = []
    cus_statement_header()
    for statement in statements:
        if statement[4] == 'Paid' and statement[5] == 'Renting':
            index_collector.append(index1)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<15}{:<10}"
                  .format(line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[6], statement[7]))
            index1 += 1
            line_num += 1
        else:
            index1 += 1
            continue

    # If the data is empty or no data to display
    if not index_collector:
        print("\nThere is no relevant data for records of cars that should be return to the system.\n")

        # Automatically return to the administrator main screen
        print("Returning to administrator main screen...")
        administrator_system()

    # Choose statement to return the rented car
    def statement_validation():
        try:
            return_rent = int(input(
                "\nWhich statement you would like to return the rent car (line of statement): "))
            if return_rent <= 0 or return_rent > len(index_collector):
                print("Invalid choice, choose from available line statement.")
                return statement_validation()
            # Ask the question again if the answer did not meet the requirement
            else:
                return return_rent

        # Exclude non numeric value
        except ValueError:
            print("Invalid input, please insert a numeric value..\n")
            return statement_validation()

    return_rent = statement_validation()

    index_value = index_converter(return_rent)

    def index_validation():
        try:
            new_index = index_collector[index_value]
            return new_index

        # Exclude non existent lines
        except IndexError:
            print("Invalid input, please try again.")
            statement_validation()

    new_index = index_validation()

    # Change reservation to completed
    statements[new_index][5] = 'Completed'

    car_id = statements[new_index][1]

    # Find for cars that status should be changed to 'Open'
    index2 = 0
    for car in cars:
        if car[0] == car_id:
            open_index = index2

            # Set car status to 'Open'
            car[5] = 'Open'
            index2 += 1
        else:
            index2 += 1
            continue

    # Display updated data
    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<16}{:<10}"
          .format(statements[new_index][0], statements[new_index][1], statements[new_index][2], statements[new_index][3], statements[new_index][8], statements[new_index][4], statements[new_index][5], statements[new_index][6], statements[new_index][7]))

    # Update data in text files
    count1 = 1
    with open('customerBookingPayment.txt', 'w') as mark_completed:
        stmnt_count = 1
        for statement in statements:
            statement.pop()
            if stmnt_count < len(statements):
                count = 1
                for details in statement:
                    if count < len(statement):
                        mark_completed.write(f"{details} | ")
                        count += 1
                    else:
                        mark_completed.write(details)
                mark_completed.write("\n")
                stmnt_count += 1
            else:
                count = 1
                for details in statement:
                    if count < len(statement):
                        mark_completed.write(f"{details} | ")
                        count += 1
                    else:
                        mark_completed.write(details)

    # Update data in text file
    with open('carDatabase.txt', 'w') as mark_open:
        car_count = 1
        for car in cars:
            if car_count < len(cars):
                count = 1
                for details in car:
                    if count < len(car):
                        mark_open.write(f"{details} | ")
                        count += 1
                    else:
                        mark_open.write(details)
                mark_open.write("\n")
                car_count += 1
            else:
                count = 1
                for details in car:
                    if count < len(car):
                        mark_open.write(f"{details} | ")
                        count += 1
                    else:
                        mark_open.write(details)

    # Ask for admins' preference in continuing returning car or back to administrator's main screen
    def cont_return():
        option = input("\nContinue returning rent car?\n\n\t[YES] or [NO]\n\n"
                       "Note: Selecting [NO] will navigate you back to administrator main screen.\n"
                       "Option=> ").upper()
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
    try:
        # Extract customer booking / payment statement to a variable that store a list
        statements = bookpay_stmnt_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Display data that required to be mark as 'Ready'
    index1 = 0
    line_num = 1
    index_collector = []
    cus_statement_header()
    for statement in statements:
        if statement[4] == 'Paid' and statement[5] == 'In Queue':
            index_collector.append(index1)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<15}{:<10}"
                  .format(line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[6], statement[7]))
            index1 += 1
            line_num += 1
        else:
            index1 += 1
            continue

    # There is no data to be marked ready
    if not index_collector:
        print("\nThere is no relevant data for records of cars that should be return to the system.\n")

        # Automatically return to the administrator main screen
        print("Returning to administrator main screen...")
        administrator_system()

    # Choose and update car to be ready for paid booking
    def mark_ready_validation():
        try:
            mark_ready = int(input(
                "\nWhich statement you would like to mark as ready upon customer's booking on confirmation towards booking: "))
            if mark_ready <= 0 or mark_ready > len(index_collector):
                print("Invalid choice, choose from available line statement.")
                return mark_ready_validation()
            else:
                return mark_ready

        # Exclude non numeric value
        except ValueError:
            print("Invalid input, please insert a numeric value..\n")
            return mark_ready_validation()

    mark_ready = mark_ready_validation()
    index_value = index_converter(mark_ready)

    def ready_index_validation():
        try:
            new_index = index_collector[index_value]
            return new_index

        # Exclude non existent lines
        except IndexError:
            print("\nInvalid input, line out of range.\n")
            mark_ready_validation()

    new_index = ready_index_validation()

    # Do not accept line lesser than 1
    if index_value < 0:
        print("Invalid input, please try again.")
        mark_ready_validation()

    # Set reservation as Ready
    else:
        statements[new_index][5] = 'Ready'

    # Display returned rent car
    print("\nMarked ready statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<16}{:<10}"
          .format(statements[new_index][0], statements[new_index][1], statements[new_index][2], statements[new_index][3], statements[new_index][8], statements[new_index][4], statements[new_index][5], statements[new_index][6], statements[new_index][7]))

    # Update data in text files
    count = 1
    with open('customerBookingPayment.txt', 'w') as mark_ready:
        stmnt_count = 1
        for statement in statements:
            statement.pop()
            if stmnt_count < len(statements):
                count = 1
                for details in statement:
                    if count < len(statement):
                        mark_ready.write(f"{details} | ")
                        count += 1
                    else:
                        mark_ready.write(details)
                mark_ready.write("\n")
                stmnt_count += 1
            else:
                count = 1
                for details in statement:
                    if count < len(statement):
                        mark_ready.write(f"{details} | ")
                        count += 1
                    else:
                        mark_ready.write(details)

    # Ask for admins' preference in continue marking ready or return to administrator main screen.
    def cont_modify_or_not():
        print("""
Do you wish to mark more cars as ready?

    [YES] or [NO]

Note: Selecting [NO] will navigate you back to administrator main screen.""")
        option = input("Option => ").upper()

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
            print("\nInvalid input, please select either 'YES' or 'NO'.\n")
            return cont_modify_or_not()

    # Call function to execute
    cont_modify_or_not()


# 7. Analytics Dashboard
def analytics_dashboard():
    try:
        # Extract customer booking / payment statement to a variable that store a list
        statements = bookpay_stmnt_read()

        # Extract car data to a variable that store list
        cars = car_database_read()[0]

        # Extract customer details to a variable that store list
        customers = customer_details_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Retrieve all customer payment total amount
    payment_amount = []
    for statement in statements:
        if statement[4] == 'Paid':
            payment_amount.append(statement[8])

    # Obtain highest / lowest / total payment completed in the system
    max_paid = max(payment_amount)
    min_paid = min(payment_amount)
    total_paid = sum(payment_amount)

    # Display analytics information in a dashboard format
    print(f"""
{decoration()} OCRS Data Analytics Dashboard {decoration()}

Total cars:                         {len(cars)} cars
Total customers:                    {len(customers)} customers
Total booking / payment records:    {len(statements)} statements
Total sales / profits:              RM {total_paid}
Highest sales / profits:            RM {max_paid}
Lowest sales / profits:             RM {min_paid}

Keep up your great work! \U0001F44D

Returning to administrator system....""")
    administrator_system()


# Section F : Customer
# 1. Customer landing page
def customer_interface():
    # Menu
    print("""
As a visitor, select your action.

1: View all available car for rent.
2: Membership Registration  - get access to more features.
3: Registered customers' section.
4: Exit the system.
""")
    # Input validation
    try:
        option = int(input("Option  => "))

        # Execute system based on option
        if option == 1:
            rent_car_details()
            cont_main_menu()
        elif option == 2:
            cus_reg_header()
        elif option == 3:
            registered_login()
        elif option == 4:
            exit_system()

        # Error if integers 1 to 4 are not entered, customers can try entering again
        else:
            print("Invalid input, please insert valid value (1 to 4).")
            return customer_interface()

    # Non numeric value validation
    except ValueError:
        print("Invalid input, please insert a valid numeric value.")
        return cont_main_menu()


# 2. Redirect customer landing page, login or register
def cont_main_menu():
    try:
        # Menu
        print("""
Do you wish to go back to the main menu or login for more functionalities?

1: Main menu
2: Proceed to log in
3: Proceed to registration (For customer with no account in the server)
4: Exit the customer system
""")
        redirect = int(input("Option => "))

        # Executes according to customer's option
        if redirect == 1:
            print("\nReturning to the main menu...")
            customer_interface()
        elif redirect == 2:
            print("\nRedirecting to the customer log in page....")
            registered_login()
        elif redirect == 3:
            print("\nRedirecting to the customer registration page....")
            customer_registration()
        elif redirect == 4:
            exit_system()

        # Error if integers from 1 to 4 are not entered, customers can try entering again
        else:
            print("\nInvalid input, please select either 1, 2, 3 or 4.")
            return cont_main_menu()

    # Non numeric value validation
    except ValueError:
        print("Invalid input, please insert a valid numeric value.")
        return cont_main_menu()


# 3. Customer Registration
def customer_registration():
    # Request for customers' username and password for registration
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        # Extract customer details to a variable that store list
        customers = customer_details_read()

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Extract all the username
    username_holder = []
    for customer in customers:
        username_holder.append(customer[0])

    # Usernames are in the database / usernames must be unique
    if username in username_holder:
        print("\nThis username had been used, please use another username.\n")
        return customer_registration()

    # Obtaining new customers' details
    else:
        print(
            "\nPlease fill in the following details to provide more information to rent a car / cars.\n")
        address = input("Address: ")
        contact_number = input("Contact number: ")

    # Every newly registered customer will have RM 0 as their balance
    balance = 0

    # Registration Completed
    print(f"""Your balance is now: RM{balance}
You can recharge it from the customer functionalities page.

{decoration()} Thank you for registering {decoration()}
""")

    new_customer_details = []
    new_customer_details.extend(
        [username, password, address, contact_number, balance])

    try:
        # Inserting new users data into customerDetails.txt as a new record
        count = 1
        with open('customerDetails.txt', "a") as new_customer:
            new_customer.write("\n")
            for detail in new_customer_details:
                if count < len(new_customer_details):
                    new_customer.write(f"{detail} | ")
                    count += 1
                else:
                    new_customer.write(str(detail))

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    print("\nYou can login to the system now. Start renting your car! \U0001F601 \n")

    # Automatically redirect to customer landing page
    customer_interface()


# 4. Customer Log in
def registered_login():
    # Log in attempts starts counting,  after 3 attempts customer will be terminate out of the login system
    for time in range(1, 4):
        print("\nAttempt: ", time, "\n")
        # Request for customers' username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        try:
            # Extract customer details to a variable that store list
            customers = customer_details_read()

        # No file spotted
        except:
            print(
                "Due to unstable database, You will be redirected to the welcome page..\n")
            welcome()

        # Username and password validation based on customers' input
        for customer in customers:
            if username == customer[0] and password == customer[1]:
                print("\n", decoration(), " Welcome to the OCRS, ",
                      username, decoration(), "\n")
                reg_customer()
                break

        # Customers who keyed in the wrong username or password will be asked to try again
        else:
            print("\nInvalid username or password, please try again...")

            # Confirming whether the customer has an existing account or not
            def registration_inquiry():
                # Menu
                print("""
Do you have an account?
[YES] or [NO]
""")
                register_confirm = input("Option => ").upper()

                # With account, customers can try again if they have an existing account
                if register_confirm == "YES":
                    print("Please try again.")

                # Without account, customers will be asked on whether to create a new account or not
                elif register_confirm == "NO":
                    def register_account_ask():
                        # Menu
                        print("""
Do you wish to register a new account?

    [YES] or [NO]

Note: Selecting [NO] will redirect you to customer landing page.""")
                        register_account = input("Option => ").upper()

                        # Customers will be redirected to the registration page
                        if register_account == "YES":
                            print(
                                "Redirecting to the customer registration page...\n")
                            cus_reg_header()

                        # Customers will be sent back to the customer landing page
                        elif register_account == 'NO':
                            print("\nReturning to the customer landing page..\n")
                            customer_interface()

                        # Invalid input, ask for option again
                        else:
                            print(
                                "Invalid input, please key in [YES] or [NO].")
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
        customer_interface()


# 5. Customer functionalities menu
def reg_customer():
    print(decoration()*2, "Functionalities Page", decoration()*2)

    # Request for users input
    def option_validation():
        try:
            # Menu
            print("""
What would you like to perform?

1: View all available car for rent.
2: Modify personal details.
3: View personal rental history.
4: Book a car.
5: Pay the car that you booked earlier.
6: Top up your balance.
7: Claim car that is Ready to be rented
8: Exit the portal.
""")
            option = int(input("Option => "))
            return option

        # Exclude non-numeric value
        except ValueError:
            print("Invalid input, please insert a numeric value.")
            return option_validation()

    option = option_validation()
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
        print("Invalid choice, please enter valid value (1 to 8).\n")
        return reg_customer()


# Section F01: Registered customers' functionalities
# 1. Display all available to rent cars.
# Retrieve car that is available to be rented out
def rent_car_details():
    try:
        # Extract car data to a variable that store list
        cars = car_database_read()[0]

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Displaying cars based on the "open" status
    available_rent_car = []
    index_holder = []
    index = 0
    line_num = 1
    status = "Open"
    car_header()
    for car in cars:
        if status == car[5]:
            available_rent_car.append(car)
            index_holder.append(index)
            print("{:<4}{:<7}{:<12}{:<11}{:<10}{:<6}{:<8}{:<5}"
                  .format(line_num, car[0], car[1], car[2], car[3], car[4], car[5], car[6]))
            index += 1
            line_num += 1
        else:
            index += 1
            continue
    return available_rent_car, index_holder


# View detail of cars to be rented out.
def dis_all_rent():
    rent_car_details()

    # ask to book car or back to the main menu from the open status cars
    def cont_book_car():
        try:
            # Menu
            print("""
Do you want to proceed to book a car or return to the functionalities menu?

    1: Booking
    2: Customers functionalities menu
""")
            # Request customers' option in directly book a car or back to customers' functionalities menu
            car_booking = int(input("Option => "))

            # Executes based on the customer's option
            if car_booking == 1:
                print("\nRedirecting to booking page...")
                book_car()
            elif car_booking == 2:
                print("\nReturning to main menu...")
                reg_customer()

            # Invalid input, ask for customers' option again
            else:
                print("\nInvalid input, please select either 1 or 2.\n")
                return cont_book_car()

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value.\n")
            return cont_book_car()

    # Call function to execute
    cont_book_car()


# 2. Modify personal details
def modify_details():
    # Request customers' username to proceed in profile modification
    username = input(
        "Your username is requested to check your credential for profile modification: ")

    try:
        # Extract customer details to a variable that store list
        customers = customer_details_read()

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Customers' username validation
    index = 0
    for customer in customers:
        if customer[0] == username:
            cus_index = index
            print(f"""
username: {customer[0]}
password: {customer[1]}
address: {customer[2]}
contact number: {customer[3]}
""")
            break
        index += 1

    # Display when the username is not in the file
    else:
        print("\nUsername is unidentified...Please try again...\n")
        return modify_details()

    # Modify desired attributes and values

    def data_type_validation():
        # Customers' modification choice
        data_type = ['Password', 'Address', 'Contact Number']
        print("\nIMPORTANT! Note that username is immutable.\nOptions: {}\n".format(
            data_type).replace("\'", " "))

        modify_type = input(
            "Which type of data you would like to change: ").lower()

        # Extract index based on users' choices
        if modify_type == "password":
            index = 1
        elif modify_type == "address":
            index = 2
        elif modify_type == "contact number":
            index = 3

        # Invalid choice, request modify type again
        elif modify_type == "username":
            print(
                "\nInvalid choice, username is unable to modify, please choose from available options.")
            return data_type_validation()
        else:
            print("\nInvalid input, please choose from the choices given")
            return data_type_validation()
        return index

    modify_index = data_type_validation()
    old_data = customers[cus_index][modify_index]
    print("Original data: ", old_data)
    new_data = input("Replace with: ")
    customers[cus_index][modify_index] = new_data

    # Update data in text files
    count = 1
    with open('customerDetails.txt', 'w') as modified:
        customer_count = 1
        for customer in customers:
            if customer_count < len(customers):
                count = 1
                for details in customer:
                    if count < len(customer):
                        modified.write(f"{details} | ")
                        count += 1
                    else:
                        modified.write(details)
                modified.write("\n")
                customer_count += 1
            else:
                count = 1
                for details in customer:
                    if count < len(customer):
                        modified.write(f"{details} | ")
                        count += 1
                    else:
                        modified.write(details)

    # Continue profile modification?
    def cont_modify():
        # Menu
        print("""
Continue modifying?

    [YES] or [NO]

Note: Selecting [NO] will navigate you back to the customer functionalities page""")

        # Request option
        continue_or_not = input("Option => ").upper()

        # Redirected to modify customer details again
        if continue_or_not == 'YES':
            print("\nUpdating modified data...\n"
                  "Continue modification based on new data and your credential will be requested again\n")
            modify_details()

        # Redirected back to the customer functionalities menu
        elif continue_or_not == 'NO':
            print("\nYou will be redirected to the customer functionalities page...")
            reg_customer()

        # Invalid input, ask for customers' option again
        else:
            print("\nInvalid input, only [YES] or [NO] allowed.\n")
            return cont_modify()

    # Call function to execute
    cont_modify()


# 3. View personal rental history
def rental_hist():
    try:
        # Extract customer booking / payment statement to a variable that store a list
        statements = bookpay_stmnt_read()

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Enter username to confirm identity
    print("\nIMPORTANT!! You are going to access customers' private data.\n")

    def username_validation():
        username = input("Enter your credential username: ")

        for statement in statements:
            if username == statement[0]:
                return username

        # Username not found in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return username_validation()

    username = username_validation()
    # username validation and display statement
    index = 0
    line_num = 1
    emp_spotter = []
    cus_statement_header()
    for statement in statements:
        if username == statement[0]:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<15}{:<10}".format(
                line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[6], statement[7]))
            index += 1
            line_num += 1
            continue
        else:
            index += 1
            continue

    # No data spotted
    if not emp_spotter:
        print("\nThe rental history is empty, start to rent a car! \U0001F60A")

    # Automatically redirect back to the customer functionalities screen
    print("\nYou will be redirected to the functionalities page...\n")
    reg_customer()


# 4. Select and Book a car for a specific duration.
def book_car():
    # Display details on available cars and transfer the statements data to this function
    available_rent_car, available_rent_index = rent_car_details()

    try:
        # Extract customer details to a variable that store list
        customers = customer_details_read()

        # Extract car data to a variable that store list
        cars = car_database_read()[0]

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Select car based on line of statement
    def select_car_validation():
        try:
            select_line = int(
                input("\nSelect the car (line of statement) you would like to book: "))
            if select_line <= 0 or select_line > len(available_rent_car):
                print("Invalid choice, choose from available line statement.")
                return select_car_validation()
            else:
                return select_line

        except ValueError:
            print(
                "\nInvalid input, please insert a numeric value within the available car range.\n")
            return select_car_validation()

    select_line = select_car_validation()
    index_value = index_converter(select_line)

    def car_statement_index_validation():
        try:
            new_index = available_rent_index[index_value]
            return new_index

        # Exclude non existent lines
        except IndexError:
            print("Invalid input, please try again.")
            select_car_validation()

    new_index = car_statement_index_validation()

    # Enter username to confirm
    def booking_username_validation():
        username = input("Enter your username to request your booking: ")

        for customer in customers:
            if username == customer[0]:
                return username

        # Username not available in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return booking_username_validation()

    username = booking_username_validation()
    select_car = cars[new_index][0]

    # Extract car price
    for car in cars:
        if car[0] == select_car:
            price = car[6]
            break

    # Ask to book for how many days
    def days_validation():
        try:
            days = int(input("How many day(s) you would like to book it: "))
            return days

        # Non-numeric value validation
        except ValueError:
            print("\nInvalid input, please insert numeric value.\n")
            return days_validation()

    days = days_validation()

    new_booking_details = []
    new_booking_details.extend([username, select_car, price, days])

    try:
        with open("customerBookingPayment.txt", 'a') as new_booking:
            new_booking.write("\n")
            for detail in new_booking_details:
                new_booking.write(f"{detail} | ")
            new_booking.write("Pending | N/A | N/A | N/A")

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Automatically redirect to customer functionalities page
    print("\nYou will be redirected to the customer functionalities page.\nNote: Your booking is not confirm yet.\n"
          "You can make your payment by choosing option 5 to confirm your booking.\n")
    return reg_customer()


# 5. Do payment to confirm Booking.
def pay_car():
    try:
        # Extract car data to a variable that store list
        cars = car_database_read()[0]

        # Extract customer booking / payment statement to a variable that store a list
        statements = bookpay_stmnt_read()

        # Extract customer details to a variable that store list
        customers = customer_details_read()

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Enter username to confirm booking
    username = input(
        "\nEnter your username to pay for your booking confirmation: ")

    index = 0
    new_index = []
    line_num = 1
    cus_statement_header()
    for statement in statements:
        # Display booking that need to be paid
        if username == statement[0] and statement[4] == 'Pending' and statement[6] == 'N/A':
            new_index.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<15}{:<10}".format(
                line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[6], statement[7]))
            line_num += 1
            index += 1

        # Display pay with balance statement / Redirected to pay with balance
        elif username == statement[0] and statement[4] == 'Pending' and statement[6] == 'balance':
            new_index.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<15}{:<10}\t\t--uncompleted payment due to insufficient balance before".format(
                line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[6], statement[7]))
            line_num += 1
            index += 1
        else:
            index += 1
            continue

    # No data spotted
    if not new_index:
        print("\nInvalid username or customer does not have a booking request.")

        # Ask to continue to pay or not
        def cont_pay():
            # Menu
            print("""
Continue payment?

    [YES] or [NO]

Note: Select [NO] return to customer functionalities page
""")
            # Request option
            option = input("Option => ").upper()

            # Return to payment page
            if option == 'YES':
                print("\nReturning to the payment page...")
                pay_car()

            # Return to customer functionalities page
            elif option == 'NO':
                print(
                    "\nYou will be redirected to the functionalities page shortly....\n")
                reg_customer()

            # Invalid input, ask for option again
            else:
                print("Invalid input, please insert [YES] or [NO].")
                return cont_pay()
        cont_pay()

    # Select the booking that customers wish to pay
    def booking_pay():
        try:
            pay_statement = int(
                input("\nWhich booking statement (line) you would like to pay? "))
            if pay_statement <= 0 or pay_statement > len(new_index):
                print("Invalid choice, choose from available line statement.")
                return booking_pay()
            else:
                return pay_statement

        # Non numeric value validation
        except ValueError:
            print("\nInvalid input, please insert numeric value.\n")
            return booking_pay()

    pay_statement = booking_pay()
    statement_index = index_converter(pay_statement)

    def pay_line_validation():
        try:
            pay_index = new_index[statement_index]
            return pay_index

        # Exclude non existent lines
        except IndexError:
            print("\nThere is no relevant line statement available for payment.")
            booking_pay()

    pay_index = pay_line_validation()
    car_id = statements[pay_index][1]

    # Note information
    print("""
IMPORTANT!!
Note:
\U00002022 you will need to make full payment to confirm your booking.
\U00002022 you can overwrite your previous payment method if you had not paid the booking
""")

    def payment_method_request():
        # Menu
        print("""What would you like to use to pay the booking?

[credit card] [balance]""")

        # Request customers to select their preferred payment method
        payment_method = input("Option => ").lower()

        # Update data
        statements[pay_index][6] = payment_method

        # Credit card payment method
        if payment_method == 'credit card':
            print(
                "\nNote that your private information in this area will not be stored in our cookies.\n")
            credit_card_num = input("Enter your credit card number: ")
            cvv = input("Enter your credit card's CVV: ")
            expiry_date = input("Enter your credit card's expiry date: ")

            # Display payment details
            print(f"""
Transaction completed...

{decoration()} Payment details {decoration()}

Paid amount: RM{statements[pay_index][8]}
Credit card: {credit_card_num}
    """)

            date = input("Please insert your desired rent date (DD/MM/YYYY): ")
            print(
                "\nDate had been recorded and please be patient and wait for the preparation process\n")

            # Update data
            statements[pay_index][4] = 'Paid'
            statements[pay_index][5] = 'In Queue'
            statements[pay_index][7] = date

            for car in cars:
                if car[0] == car_id:
                    car[5] = 'Booked'

        # Redirect to balance payment page
        elif payment_method == 'balance':
            index1 = 0
            for customer in customers:
                if customer[0] == username:
                    new_index1 = index1
                    balance = int(customer[4])
                    break
                index1 += 1

            # Calculating the total amount customers should pay
            total = statements[pay_index][8]

            # Display how much the customer should pay and car ID
            print(f"""
Your initial balance: RM{balance}
You have to pay: RM{total}
Car ID: {car_id}
    """)

            # Deduct from balance if it is more than total
            if balance >= total:
                new_balance = balance - total

                # Display remaining balance
                print(
                    "You had paid the booking confirmation.\nTransaction completed. Your current balance is RM", new_balance)

                date = input(
                    "Please insert your desired rent date (DD/MM/YYYY): ")
                print(
                    "\nDate had been recorded and please be patient and wait for the preparation process\n")

                # Change data to paid situation
                customers[new_index1][4] = str(new_balance)
                statements[pay_index][4] = 'Paid'
                statements[pay_index][5] = 'In Queue'
                statements[pay_index][6] = 'balance'
                statements[pay_index][7] = date

                for car in cars:
                    if car[0] == car_id:
                        car[5] = 'Booked'

            # Insufficient balance to pay will be automatically redirected to the top up screen
            elif balance < total:
                print(f"""
Your balance is insufficient...
Your current balance: RM{balance}

You will need to top up before paying your booking confirmation.

Redirecting to top up system....
    """)
                top_up_header()

        # Invalid input, reboot car payment page
        else:
            print("Invalid input, Please choose from the available option")
            return payment_method_request()

    payment_method_request()

    # Update data to text files
    count = 1
    statement_count = 1
    with open('customerBookingPayment.txt', 'w') as update_pay_method:
        for statement in statements:
            statement.pop()
            if statement_count < len(statements):
                count = 1
                for details in statement:
                    if count < len(statement):
                        update_pay_method.write(f"{details} | ")
                        count += 1
                    else:
                        update_pay_method.write(details)
                update_pay_method.write("\n")
                statement_count += 1
            else:
                count = 1
                for details in statement:
                    if count < len(statement):
                        update_pay_method.write(f"{details} | ")
                        count += 1
                    else:
                        update_pay_method.write(details)

    count = 1
    car_count = 1
    with open('carDatabase.txt', 'w') as mark_rented:
        for car in cars:
            if car_count < len(cars):
                count = 1
                for details in car:
                    if count < len(car):
                        mark_rented.write(f"{details} | ")
                        count += 1
                    else:
                        mark_rented.write(details)
                mark_rented.write("\n")
                car_count += 1
            else:
                count = 1
                for details in car:
                    if count < len(car):
                        mark_rented.write(f"{details} | ")
                        count += 1
                    else:
                        mark_rented.write(details)

    count = 1
    customer_count = 1
    with open('customerDetails.txt', 'w') as balance_reduce:
        for customer in customers:
            if customer_count < len(customers):
                count = 1
                for details in customer:
                    if count < len(customer):
                        balance_reduce.write(f"{details} | ")
                        count += 1
                    else:
                        balance_reduce.write(details)
                balance_reduce.write("\n")
                customer_count += 1
            else:
                count = 1
                for details in customer:
                    if count < len(customer):
                        balance_reduce.write(f"{details} | ")
                        count += 1
                    else:
                        balance_reduce.write(details)

    # Automatically redirect to the customer functionalities page
    print("\nRedirecting to customer functionalities page...\n")
    reg_customer()


# 8. Top up your balance.
def top_up():
    # Extract customer details to dictionaries in list
    try:
        # Extract customer details to a variable that store list
        customers = customer_details_read()

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Request username
    def check_balance_validation():
        username = input(
            "\nEnter your username to check your current balance: ")

        for customer in customers:
            if username == customer[0]:
                return username

        # Username not available in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return check_balance_validation()

    username = check_balance_validation()

    # Display current balance based on username
    index = 0
    for customer in customers:
        if customer[0] == username:
            cus_index = index
            balance = int(customer[4])
            print("Your current balance: ", str(balance))
            break
        else:
            index += 1
            continue

    # Error message if username does not exist and request username again
    else:
        print("Invalid username, please try again.")
        return top_up()

    # Select desired payment method
    def payment_type():
        try:
            # Menu
            print("""
Which payment method do you prefer to top up your balance with?

    1: Credit/debit card
    2: FPX online banking
""")
            payment_method = int(input("Option => "))

            # Credit card payment method
            if payment_method == 1:
                print("\n", decoration() * 3,
                      "\nTop up with: Credit/debit card\n", decoration() * 3)
                credit_card_num = input(
                    "Enter your credit/debit card number: ")
                cvv = input("Enter your credit/debit card's CVV: ")
                expiry_date = input(
                    "Enter your credit/debit card's expiry date: ")

            # FPX online banking payment method
            elif payment_method == 2:
                print("\n", decoration() * 3,
                      "\nTop up with: FPX online banking\n", decoration() * 3)

                # Bank options to proceed payment in FPX
                def bank_options():
                    # Menu
                    print("""
Select your merchant:

    1: Maybank
    2: Public Bank
    3: Ambank
    4: RHB Bank
    5: CIMB Bank
""")
                    try:
                        bank_choice = int(input("Option => "))

                        # Execute based on options by customers
                        if bank_choice <= 5:
                            account_no = input(
                                "Enter your bank account number: ")
                            account_password = input(
                                "Enter your bank account password: ")
                            print("\nTop up with", account_no)

                        # Error if numbers less than 5 are not entered and request bank again
                        else:
                            print("Invalid input, please select in range 1 to 5.")
                            return bank_options()

                    # Exclude non numeric value
                    except ValueError:
                        print("\nInvalid input, please insert numeric value.\n")
                        return bank_options()

                bank_option = bank_options()

            # Error if integer 1 or 2 are not entered
            else:
                print("Invalid input, please enter either 1 or 2.")
                return payment_type()

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert numeric value (1 or 2).\n")
            return payment_type()

    payment_method = payment_type()
    # Request top up amount

    def top_up_amount():
        try:
            top_up_value = int(input("How much do you want to top up: "))
            return top_up_value

        # Validation for non numeric value
        except ValueError:
            print("Invalid input, please insert numeric value..")
            return top_up_amount()

    top_up_value = top_up_amount()
    balance += top_up_value
    customers[cus_index][4] = str(balance)
    print("Top up success, current balance: RM",
          customers[cus_index][4])

   # Update data to text files
    count = 1
    customer_count = 1
    with open('customerDetails.txt', 'w') as top_up_balance:
        for customer in customers:
            if customer_count < len(customers):
                count = 1
                for details in customer:
                    if count < len(customer):
                        top_up_balance.write(f"{details} | ")
                        count += 1
                    else:
                        top_up_balance.write(details)
                top_up_balance.write("\n")
                customer_count += 1
            else:
                count = 1
                for details in customer:
                    if count < len(customer):
                        top_up_balance.write(f"{details} | ")
                        count += 1
                    else:
                        top_up_balance.write(details)
    # Continue top up?

    def cont_top_up():
        # Menu
        print("""
Do you wish to top up more? 

    [YES] or [NO]
    
Note: Selecting [NO] will redirect you back to the functionalities main menu.""")
        cont_or_not = input("Option => ").upper()

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
    try:
        # Extract customer booking / payment statement to a variable that store a list
        statements = bookpay_stmnt_read()

        # Extract car data to a variable that store list
        cars = car_database_read()[0]

    # No file spotted
    except:
        print("Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Request username to check car that is able to claim
    def claim_car_username_validation():
        username = input("Enter your username to confirm your identity: ")

        for statement in statements:
            if username == statement[0]:
                return username

        # Username not available in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return claim_car_username_validation()

    username = claim_car_username_validation()

    # Display information based on username and fits the requirement to claim
    index1 = 0
    line_num = 1
    index_collector = []
    cus_statement_header()
    for statement in statements:
        if statement[0] == username and statement[4] == 'Paid' and statement[5] == 'Ready':
            index_collector.append(index1)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<15}{:<10}".format(
                line_num, statement[0], statement[1], statement[2], statement[3], statement[8], statement[4], statement[5], statement[6], statement[7]))
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
    def claim_line_statement():
        try:
            claim_car = int(input(
                "\nWhich statement you would like to claim your car (line of statement): "))
            if claim_car <= 0 or claim_car > len(index_collector):
                print("Invalid choice, choose from available line statement.")
                return claim_line_statement()
            else:
                return claim_car

        # Validation for non numeric value
        except ValueError:
            print("Invalid input, please insert numeric value..")
            return claim_line_statement()

    claim_car = claim_line_statement()
    index_value = index_converter(claim_car)

    # Select the booking that customers wish to pay
    def claim_index():
        try:
            new_index = index_collector[index_value]
            return new_index

        # validation for invalid line of statement
        except IndexError:
            print("\nThere is no relevant line statement that appear to be claimed.")
            claim_line_statement()

    new_index = claim_index()

    # Change status
    statements[new_index][5] = 'Renting'
    car_id = statements[new_index][1]

    # Display claimed car statement
    print("\nClaimed car statement: ")
    cus_statement_header()
    print("    {:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<16}{:<10}".format(
        statements[new_index][0], statements[new_index][1], statements[new_index][2], statements[new_index][3], statements[new_index][8], statements[new_index][4], statements[new_index][5], statements[new_index][6], statements[new_index][7]))

    # Change car status to rented
    index2 = 0
    for car in cars:
        if car[0] == car_id:
            car[5] = 'Rented'
            index2 += 1
        else:
            index2 += 1
            continue

    # Update new data to text file
    count = 1
    statement_count = 1
    with open('customerBookingPayment.txt', 'w') as paid:
        for statement in statements:
            statement.pop()
            if statement_count < len(statements):
                count = 1
                for details in statement:
                    if count < len(statement):
                        paid.write(f"{details} | ")
                        count += 1
                    else:
                        paid.write(details)
                paid.write("\n")
                statement_count += 1
            else:
                count = 1
                for details in statement:
                    if count < len(statement):
                        paid.write(f"{details} | ")
                        count += 1
                    else:
                        paid.write(details)

    count = 1
    car_count = 1
    with open('carDatabase.txt', 'w') as mark_rented:
        for car in cars:
            if car_count < len(cars):
                count = 1
                for details in car:
                    if count < len(car):
                        mark_rented.write(f"{details} | ")
                        count += 1
                    else:
                        mark_rented.write(details)
                mark_rented.write("\n")
                car_count += 1
            else:
                count = 1
                for details in car:
                    if count < len(car):
                        mark_rented.write(f"{details} | ")
                        count += 1
                    else:
                        mark_rented.write(details)

    # Continue claiming cars or not?
    def cont_claim():
        # Menu
        print("""
Do you wish to claim other cars you own? 

    [YES] or [NO]

Note: Selecting [NO] will redirect you to the customer functionalities menu.""")
        cont_or_not = input("Option => ").upper()

        # Execute options made by customers
        if cont_or_not == "YES":
            print("\nYou will be redirected back to claim your other cars....\n")
            car_claim()
        elif cont_or_not == "NO":
            print("Returning to the customer functionalities menu....")
            reg_customer()

        # Invalid input, request option again
        else:
            print("Invalid input, you can only enter either 'YES' or 'NO'.")
            return cont_claim()
    cont_claim()


# Call function to execute the OCRS system
welcome()
