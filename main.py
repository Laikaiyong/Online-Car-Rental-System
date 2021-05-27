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
                'Total Amount', 'Status', 'Reservation']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(cus_book) + 1)
    print("\n", format_row.format("", *cus_book))


# 3. Customer payment statement data header
def cus_pay_header():
    # Headers
    cus_pay = ['Username', 'Car ID', 'Price', 'Days',
               'Total Amount', 'Status', 'Payment Method']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


# 4. Customer statement data header
def cus_statement_header():
    # Headers
    cus_pay = ['Username', 'Car ID', 'Price', 'Days',
               'Total Amount', 'Status', 'Reservation', 'Payment Method']

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(cus_pay) + 1)
    print("\n", format_row.format("", *cus_pay))


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

    except:
        print("\nDatabase is corrupted..")

    return statements


# Section D: General Users Interface
# 1. Welcome page with text display.
def welcome():
    print("\n", decoration(), "Welcome to the Online Car Rental System(OCRS) by Super Car Rental Services(SCRS)",
          decoration())

    # Menu
    print("""\nEnter the number that best describe you.

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
        print("\n", decoration(), "Exit", decoration())
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

1: Car database Database
2: Customer information Database
3: Customer Booking / Payment Database
""")
                create_file = int(input("Option => "))

                # Execute based on the choices entered
                if create_file == 1:
                    create_car = open("carDatabase.txt", "w")
                    print(
                        "\nDatabase created, you will be redirected to the add car functionalities.")
                    admin_add_car()
                elif create_file == 2:
                    create_user = open("customerDetails.txt", "w")
                    print(
                        "\nDatabase created, you will be redirected to the administrator main screen.")
                    administrator_system()
                elif create_file == 3:
                    create_booking = open("customerBookingPayment.txt", "w")
                    print(
                        "\nDatabase created, you will be redirected to the administrator main screen.")
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
6: Mark a car as Ready after the car is available upon customer's payment on confirmation for booking.
7: OCRS Data Analytics Dashboard
8: Exit the system.
""")
            option = int(input("Select your action: "))
            return option

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return admin_function_validation()

    option = admin_function_validation()
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


# Section E01: Administrator functionalities
# 1. Add car
def admin_add_car():
    # Menu
    print("""
Insert car data:
[YES] to continue
[NO] to stop and display all data. Will be redirected to admin main screen.    
    """)

    # Add car choice
    add_or_not = input("Option => ").upper()

    # Extract car data to in list
    try:
        cars = car_database_read()[0]

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

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
                    input("Enter price per hour (Only numeric data): "))
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
            print("\nDatabase under maintenance.. \n"
                  "Access the database system to check database progress\n")
            maintenance_database_access()

        # Ask for admins choice on inserting more cars or stop adding
        return admin_add_car()

    # Stop adding car and display all cars
    elif add_or_not == "NO":
        print("\n", decoration(), " Displaying all data ", decoration())
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
            return data_line

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return data_line_validation()

    data_line = data_line_validation()

    car_index_convert = index_converter(data_line)

    def data_line_index():
        try:
            car_index = cars_index[car_index_convert]
            return car_index

        # Exclude non existent records
        except IndexError:
            print("\nCar line is out of range.")
            data_line_validation()

    car_index = data_line_index()
    print("\nIMPORTANT!!! Note that uniqueID can't be modified. "
          "\nIf the car had been removed from the system place X in rent status.\n")

    def data_type_validation():
        # Ask for desired data type
        item = input("Modify data type (e.g. Car Name, Price): ").replace(
            " ", '_').lower()

        if item == "car_brand":
            index = 1
            origin_word = cars[car_index][index]
            return origin_word, index

        elif item == "car_name":
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

        else:
            print("Invalid choice, please refer the data headers and make your choice.")
            return data_type_validation()

        return origin_word, index

    # Extract and display original data
    origin_word, replace_index = data_type_validation()
    print("Origin data: ", origin_word)

    # Replace data
    replace_word = input("Replaced by:  ")
    cars[car_index][replace_index] = replace_word

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
            print(
                "\nDisplaying modified data...\nContinue modification based on new data.")
            return admin_modify()

        # Stop modification and return to admnistrator functionalities menu
        elif continue_or_not == 'NO':
            print("\nDisplaying updated data.\n")
            car_header()
            print("   {:<9}{:<11}{:<11}{:<10}{:<7}{:<9}{:<6}"
                  .format(cars[car_index][0], cars[car_index][1], cars[car_index][2], cars[car_index][3], cars[car_index][4], cars[car_index][5], cars[car_index][6]))
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


# 3.1 All display dataset
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

    status = input(
        "\nCategories available [Open] [Rented] [X] [Booked]\nStatus => ").capitalize()

    # Display cars with matching status
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

    # No data spotted
    if not emp_spotter:
        print(
            "\n\nThere is no relevant data for records of cars on that particular status.\n")

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
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<5}"
                  .format(line_number, statement[0], statement[1], statement[2], statement[3], int(statement[2]) * int(statement[3]), statement[4], statement[5]))
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
    # Extract customer booking / payment statement to a list
    try:
        statements = bookpay_stmnt_read()

    # No file identified
    except:
        print("Access the database system to check database issue.\n")
        maintenance_database_access()

    # Set statement status only specify on 'Paid'
    status = 'Paid'

    # Display matching customer payment statement
    index = 0
    line_number = 1
    emp_spotter = []
    cus_pay_header()
    for statement in statements:
        if status == statement[4]:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<8}{:<5}"
                  .format(line_number, statement[0], statement[1], statement[2], statement[3], int(statement[2]) * int(statement[3]), statement[4], statement[6]))
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


# 3.2 Continue to display menu or administrator page.
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


# 4.1 Search data
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
        data_type = input("""
Options: [Username] [Car ID] [Price] [Days] [Total Amount]

What is the data type you would like to seek for: """).lower()
        if data_type == "username":
            index = 0
        elif data_type == "car id":
            index = 1
        elif data_type == "price":
            index = 2
        elif data_type == "days":
            index = 3
        elif data_type == "total amount":
            for statement in statements:
                total = int(statement[2]) * int(statement[3])
                statement.append(total)
        print(statements)

        # else:
        #     print("Invalid input, please choose from the option.\n")
        #     return data_type_validation()
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
            option = input("Continue searching?\n\n\t[YES] or [NO]\n\n"
                           "Note: Selecting [NO] will navigate you back to administrator main screen.\n"
                           "Option=> ").upper()
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
    # Extract customer booking / payment statement to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

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
                          int(customer['price']) *
                          int(customer['days']), customer['status'],
                          customer['payment method']))
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
            option = input("Continue searching?\n\n\t[YES] or [NO]\n\n"
                           "Note: Selecting [NO] will navigate you back to administrator main screen.\n"
                           "Option=> ").upper()
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


cus_book_search()
# 4.2 Continue at search menu or back to administrator main screen.


def search_redirect():
    # Ask for admins' preference in redirection
    def option_validation():
        try:
            option = int(input("""
Do you want to return to the search menu or administrator main screen?

    1: Search menu
    2: Administrator Main screen

Option => """))
            return option

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert a numeric value..\n")
            return option_validation()

    option = option_validation()

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
    try:
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

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

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
                          int(customer['price']) *
                          int(customer['days']), customer['status'],
                          customer['reservation'], customer['payment method']))
            index1 += 1
            line_num += 1
        else:
            index1 += 1
            continue

    # If the data is empty or no data to display
    if not index_collector:
        print("\nThere is no relevant data for records of cars that should be return to the system.\n"
              "Redirecting to the administrator main screen...\n")

        # Automatically redirect to administrator main screen
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
    customers[new_index]['reservation'] = 'Completed'

    car_id = customers[new_index]['car id']
    # Extract car data to dictionaries in list
    try:
        car_details = {}
        cars = []
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
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

    # Find for cars that status should be changed to 'Open'
    index2 = 0
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
    try:
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

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

    try:
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

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

    # Display updated data
    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
          .format(customers[new_index]['username'], customers[new_index]['car id'], customers[new_index]['price'],
                  customers[new_index]['days'], int(
                      customers[new_index]['price']) * int(customers[new_index]['days']),
                  customers[new_index]['status'], customers[new_index]['reservation'],
                  customers[new_index]['payment method']))

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
    # Extract customers' booking / payment statement to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

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
                          int(customer['price']) *
                          int(customer['days']), customer['status'],
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
        customers[new_index]['reservation'] = 'Ready'

    # Update text file
    try:
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
    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

    # Display returned rent car
    print("\nReturned rent statement: ")
    cus_statement_header()
    print("   {:<11}{:<8}{:<7}{:<8}RM {:<8}{:<9}{:<13}{:<8}"
          .format(customers[new_index]['username'], customers[new_index]['car id'], customers[new_index]['price'],
                  customers[new_index]['days'], int(
                      customers[new_index]['price']) * int(customers[new_index]['days']),
                  customers[new_index]['status'], customers[new_index]['reservation'],
                  customers[new_index]['payment method']))

    # Ask for admins' preference in continue marking ready or return to administrator main screen.
    def cont_modify_or_not():
        option = input("""
Do you wish to mark more cars as ready?

\t[YES] or [NO]

Note: Selecting [NO] will navigate you back to administrator main screen.
Option => """).upper()

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
    # Extract customer booking / payment statement to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

    # Extract car data to dictionaries in list
    try:
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

    # No file spotted
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

    # Extract customer details to dictionaries in list
    try:
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

    # No file spotted
    except:
        print("\nDatabase under maintenance.. \n"
              "Access the database system to check database progress\n")
        maintenance_database_access()

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
    try:
        option = int(input("""\nAs a visitor, select your action.

1: View all cars with any status.
2: Membership Registration \t - get access to more features.
3: Registered customers' section.
4: Exit the system.

Option  => """))

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

    # Non numeric value validation
    except ValueError:
        print("Invalid input, please insert a valid numeric value.")
        return cont_main_menu()


# 2. Redirect customer landing page, login or register
def cont_main_menu():
    try:
        redirect = int(input("""
Do you wish to go back to the main menu or login for more functionalities?

1: Main menu
2: Proceed to log in
3: Proceed to registration (For customer with no account in the server)

Option => """))

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
        # Error if integers form 1 to 3 are not entered, customers can try entering again
        else:
            print("\nInvalid input, please select either 1, 2 or 3.")
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

    # Open text file for validation and insertion
    username_holder = []
    try:
        with open("customerDetails.txt", 'r') as existing:
            # Check whether the username is taken by other customer, duplicate usernames are not allowed
            for line in existing:
                row = line.strip()
                if row[0] == username:
                    username_holder.append()
                    continue
                else:
                    names = {}
                    continue

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # When usernames are available in the database
    for name in username_holder:
        if username == name['username']:
            print("\nThis username had been used, please use another username.\n")
            return customer_registration()

        # Obtaining new customers' details
        else:
            print(
                "\nPlease fill in the following details to provide more information to rent a car / cars.\n")
            address = input("Address: ")
            contact_number = input("Contact number: ")
            break

    # Every newly registered customer will have RM 0 as their balance
    balance = 0
    print(f"""Your balance is now: RM{balance}
You can recharge it from the customer functionalities page.

{decoration()} Thank you for registering {decoration()}
""")

    try:
        # Inserting new users data into customerDetails.txt as a record
        with open("customerDetails.txt", 'a') as new_customer:
            new_customer.write(f"\nusername: {username}\npassword: {password}\naddress: {address}"
                               f"\ncontact number: {contact_number}\nbalance: {balance}")

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

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
        try:
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

        # No file spotted
        except:
            print("\nDatabase is corrupted..\n"
                  "Due to unstable database, You will be redirected to the welcome page..\n")
            welcome()

        # Username and password validation based on customers' input
        for customer in customers:
            if username == customer['username'] and password == customer['password']:
                print("\n", decoration(), " Welcome to the OCRS, ",
                      username, decoration(), "\n")
                reg_customer()
                break

        # Customers who keyed in the wrong username or password will be asked to try again
        else:
            print("\nInvalid username or password, please try again...")

            # Confirming whether the customer has an existing account or not
            def registration_inquiry():
                register_confirm = input("""
Do you have an account? 
[YES] or [NO]

Option => """).upper()

                # With account, customers can try again if they have an existing account
                if register_confirm == "YES":
                    print("Please try again.")

                # Without account, customers will be asked on whether to create a new account or not
                elif register_confirm == "NO":
                    def register_account_ask():
                        register_account = input("\nDo you wish to register a new account?\n\n\t[YES] or [NO]"
                                                 "\n\nNote: Selecting [NO] will redirect you to customer landing page."
                                                 "\nOption => ").upper()

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

Option => """))
            return option

        # Non numeric value validation
        except:
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
    # Extract car data to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

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
        try:
            # Request customers' option in directly book a car or back to customers' functionalities menu
            car_booking = int(input("""
Do you want to proceed to book a car or return to the functionalities menu?

    1: Booking
    2: Customers functionalities menu

Option => """))

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

    # Extract customers' details to dictionaries in list
    try:
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

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

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
    print("\nIMPORTANT! Note that username is immutable.\nOptions: {}".format(
        data_type).replace("\'", " "))

    # Modify desired attributes and values
    modify_type = input(
        "\nWhich type of data you would like to change: ").lower()
    old_data = customers[cus_index][modify_type]
    print("Original data: ", old_data)
    new_data = input("Replace with: ")
    customers[cus_index][modify_type] = new_data

    # Update new data into the text file
    try:
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

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Continue profile modification?
    def cont_modify():
        continue_or_not = input("""
Continue modifying?

    [YES] or [NO]
    
Note: Selecting [NO] will navigate you back to the customer functionalities page
Option => """).upper()

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
    try:
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

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    booking_details.close()

    # Enter username to confirm identity
    print("\nIMPORTANT!! You are going to access customers' private data.\n")

    def username_validation():
        username = input("Enter your credential username: ")

        for customer in customers:
            if username == customer["username"]:
                return username

        # Username not found in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return username_validation()

    username = username_validation()
    # username validation and print
    index = 0
    line_num = 1
    emp_spotter = []
    cus_statement_header()
    for customer in customers:
        if username == customer['username']:
            emp_spotter.append(index)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<8}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']
                                                       ), customer['status'], customer['reservation'],
                          customer['payment method']))
            index += 1
            line_num += 1
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


# 4. Select and Book a car for a specific duration.
def book_car():
    # Display details on available cars
    rent_car_details()

    # Extract customer details into dictionaries in list
    try:
        customer_details = {}
        customers = []
        with open("customerDetails.txt", "r") as username_verification:
            for line in username_verification:
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

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    username_verification.close()

    # Select car ID
    select_car = input("\nSelect the car ID you would like to book: ")

    # Enter username to confirm
    def booking_username_validation():
        username = input("Enter your username to request your booking: ")

        for customer in customers:
            if username == customer["username"]:
                return username

        # Username not available in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return booking_username_validation()

    username = booking_username_validation()

    # Extract car details to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    original.close()

    # Change the status of the car to "booked"
    for car in car_holder:
        if car['car_id'] == select_car:
            price = car['price']
            break

    # Ask to book for how many days
    def days_validation():
        try:
            days = int(input("How many day(s) you would like to book it: "))
            return days

        # Non-numeric value validation
        except:
            print("\nInvalid input, please insert numeric value.\n")
            return days_validation()

    days = days_validation()
    # Update new data into the text file
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    new_status.close()

    try:
        with open("customerBookingPayment.txt", 'a') as new_booking:
            new_booking.write(f"\nusername: {username}\ncar id: {select_car}\nprice: {price}\ndays: {days}\n"
                              f"status: Pending\nreservation: N/A\npayment method: N/A")

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Automatically redirect to customer functionalities page
    print("\nYou will be redirected to the customer functionalities page.\n"
          "You can make your payment by choosing option 5 to confirm your booking.\n")
    return reg_customer()


# 5. Do payment to confirm Booking.
def pay_car():
    # Extract car details to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    original.close()

    # Extract customer booking details into dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    booking_details.close()

    # Enter username to confirm booking
    def payment_username_validation():
        username = input(
            "\nEnter your username to pay for your booking confirmation: ")

        for customer in customers:
            if username == customer["username"]:
                return username

        # Username not available in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return payment_username_validation()

    username = payment_username_validation()

    index = 0
    new_index = []
    line_num = 1
    cus_statement_header()
    for customer in customers:
        # Display booking that need to be paid
        if username == customer['username'] and customer['status'] == 'Pending' and customer['payment method'] == 'N/A':
            new_index.append(index)
            print("{:<4}{:<10}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']
                                                       ), customer['status'], customer['reservation'],
                          customer['payment method']))
            line_num += 1

        # Display pay with balance statement / Redirected to pay with balance
        elif username == customers[index]['username'] and customers[index]['status'] == 'Pending' \
                and customers[index]['payment method'] == 'balance':
            print("    {:<10}{:<8}{:<7}{:<8}RM{:<9}{:<9}{:<13}{:<8}"
                  .format(customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) * int(customer['days']
                                                       ), customer['status'], customer['reservation'],
                          customer['payment method']))
            pay_balance()
        else:
            index += 1

    # No data spotted
    if not new_index:
        print("\nInvalid username or customer does not have a booking request.")

        # Ask to continue to pay or not
        def cont_pay():
            option = input("\nContinue payment?\n\n\t[YES] or [NO]\n\n"
                           "Note: Select [NO] return to customer functionalities page\nOption => ").upper()

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
    car_id = customers[pay_index]['car id']

    # Request customers to select their preferred payment method
    print("\nIMPORTANT!! Note that you will need to make full payment to confirm your booking.\n")
    payment_method = input("""What would you like to use to pay the booking?
[credit card] [balance]
=> """).lower()

    # Update data
    customers[pay_index]['payment method'] = payment_method

    # Update new data to the text file
    count = 1
    with open("customerBookingPayment.txt", 'w') as update_pay_method:
        for data in customers:
            for records in data:
                if count < len(customers) * 7:
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
                car["status"] = 'Booked'

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
    # Extracts customer Details into dictionaries in list
    try:
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

    # No file identitifed
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Request username
    def balance_username_validation():
        username = input(
            "\nYou are accessing your online balance, enter your username to make sure that is you: ")

        for customer in customers:
            if username == customer["username"]:
                return username
        else:
            print("There is no such customer, please insert a valid username.\n")
            return balance_username_validation()

    username = balance_username_validation()

    # Verifying username
    index1 = 0
    for customer in customers:
        if customer['username'] == username:
            new_index1 = index1
            balance = int(customer["balance"])
            break
        index1 += 1

    # Extracts customer booking/payment details into dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

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
            print("You have to pay: RM", total, "\nCar ID: ", car_id)
            break
        index2 += 1

    # Extracts car details to dictionaries in list
    try:
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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Deduct from balance if it is more than total
    if balance >= total:
        new_balance = balance - total

        # Display remaining balance
        print("\nCurrent balance: RM", balance, "\nYou had paid the booking confirmation."
                                                "\nTransaction completed. Your current balance is RM", new_balance)

        # Change data to paid situation
        customers[new_index1]["balance"] = str(new_balance)
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
        with open('customerDetails.txt', 'w') as deduct_balance:
            for information in customers:
                for key in information:
                    if count1 < len(customers)*5:
                        list_of_strings = f'{key}: {information[key]}'
                        deduct_balance.write(f'{list_of_strings}\n')
                        count1 += 1
                    else:
                        list_of_strings = f'{key}: {information[key]}'
                        deduct_balance.write(f'{list_of_strings}')

        count2 = 1
        with open('customerBookingPayment.txt', 'w') as paid:
            for information in statements:
                for key in information:
                    if count2 < len(statements) * 7:
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
    try:
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

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

    # Request username
    def check_balance_validation():
        username = input(
            "\nEnter your username to check your current balance: ")

        for customer in customers:
            if username == customer["username"]:
                return username

        # Username not available in the database
        else:
            print("There is no such customer, please insert a valid username.\n")
            return check_balance_validation()

    username = check_balance_validation()

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
    def payment_type():
        try:
            payment_method = int(input(f"""
Which payment method do you prefer to top up your balance with? 

    1: Credit/debit card 
    2: FPX online banking

Option => """))
            return payment_method

        # Exclude non numeric value
        except ValueError:
            print("\nInvalid input, please insert numeric value.\n")
            return payment_type()

    payment_method = payment_type()
    # Credit card payment method
    if payment_method == 1:
        print("\n", decoration() * 3,
              "\nTop up with: Credit/debit card\n", decoration() * 3)
        credit_card_num = input("Enter your credit/debit card number: ")
        cvv = input("Enter your credit/debit card's CVV: ")
        expiry_date = input("Enter your credit/debit card's expiry date: ")

    # FPX online banking payment method
    elif payment_method == 2:
        print("\n", decoration() * 3,
              "\nTop up with: FPX online banking\n", decoration() * 3)

        # Bank options to proceed payment in FPX
        def bank_options():
            try:
                bank_choice = int(input(f"""
Select your merchant:

    1: Maybank
    2: Public Bank
    3: Ambank 
    4: RHB Bank
    5: CIMB Bank

Option => """))
                return bank_choice

            # Exclude non numeric value
            except ValueError:
                print("\nInvalid input, please insert numeric value.\n")
                return bank_options()

        bank_choice = bank_options()
        # Execute based on options by customers
        if bank_choice <= 5:
            account_no = input("Enter your bank account number: ")
            account_password = input("Enter your bank account password: ")
            print("\nTop up with", account_no)

        # Error if numbers less than 5 are not entered and request bank again
        else:
            print("Invalid input, please select in range 1 to 5.")
            return bank_options()

    # Error if integer 1 or 2 are not entered
    else:
        print("Invalid input, please enter either 1 or 2.")
        payment_type()

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
    customers[cus_index]['balance'] = str(balance)
    print("Top up success, current balance: RM",
          customers[cus_index]['balance'])

    # Transfer new data into the text file
    with open('customerDetails.txt', 'w') as top_up_file:
        for information in customers:
            for key in information:
                list_of_strings = f'{key}: {information[key]}'
                top_up_file.write(f'{list_of_strings}\n')

    # Continue top up?
    def cont_top_up():
        cont_or_not = input("""
Do you wish to top up more? 

    [YES] or [NO]
    
Note: Selecting [NO] will redirect you back to the functionalities main menu.
Option => """).upper()

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

    # No file identified
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()
    booking_details.close()

    # Request username to check car that is able to claim
    def claim_car_username_validation():
        username = input("Enter your username to confirm your identity: ")

        for customer in customers:
            if username == customer["username"]:
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
    for customer in customers:
        if customer['username'] == username and customer['status'] == 'Paid' and customer['reservation'] == 'Ready':
            index_collector.append(index1)
            print("{:<4}{:<11}{:<8}{:<7}{:<8}RM{:<8}{:<9}{:<13}{:<8}"
                  .format(line_num, customer['username'], customer['car id'], customer['price'], customer['days'],
                          int(customer['price']) *
                          int(customer['days']), customer['status'],
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
    def claim_line_statement():
        try:
            claim_car = int(input(
                "\nWhich statement you would like to claim your car (line of statement): "))
            return claim_car

        # Validation for non numeric value
        except ValueError:
            print("Invalid input, please insert numeric value..")
            return claim_line_statement()

    claim_car = claim_line_statement()
    try:
        index_value = index_converter(claim_car)
        new_index = index_collector[index_value]

    # validation for invalid line of statement
    except IndexError:
        print("\nThere is no relevant line statement that appear to be claimed.")
        claim_line_statement()

    # Change status
    customers[new_index]['reservation'] = 'Renting'
    car_id = customers[new_index]['car id']

    # Extract car details to dictionaries in list
    try:
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

    # No file spotted
    except:
        print("\nDatabase is corrupted..\n"
              "Due to unstable database, You will be redirected to the welcome page..\n")
        welcome()

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
                  customers[new_index]['days'], int(
                      customers[new_index]['price']) * int(customers[new_index]['days']),
                  customers[new_index]['status'], customers[new_index]['reservation'],
                  customers[new_index]['payment method']))

    # Continue claiming cars or not?
    def cont_claim():
        cont_or_not = input(
            "\nDo you wish to claim other cars you own? [YES] or [NO]\n\nOption => ").upper()

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
