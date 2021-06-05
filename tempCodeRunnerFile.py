def car_header():
    # Headers
    car_headers = ['Car ID', 'Car Brand', 'Car Model',
                   'Car Plate', 'Year', 'Status', 'Price']
    print(car_headers)

    # Setting / Display format of displaying all headers
    format_row = "{}  " * (len(car_headers) + 1)
    print("\n", format_row.format("", *car_headers))


car_header()