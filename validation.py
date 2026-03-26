import os

# function that checks if country is found in list
def find_country(locations, country):
    is_found = False
    # loop through locations
    for location in locations:
        # if the country is in list - is found = true
        if location['country'] == country:
            is_found = True
    return is_found

# function that checks if type is found in list
def find_type(locations , type):
    is_found = False
    # loop through locations
    for location in locations:
        # if the type is in list - is found = true
        if location['type'] == type:
            is_found = True
    return is_found

# function that checks if id of location is found in list
def find_id(locations, loc_id):
    is_found = False
    # loop through locations
    for location in locations:
        # if the id of location is in list - is found = true
        if location['id'] == loc_id:
            is_found = True
    return is_found

# function that check load mode - if is 1 or 2 is true , else its false
def check_load_mode(mode):
    is_good = False
    if mode == "1":
        is_good = True
    elif mode == "2":
        is_good = True
    return is_good

# function that check if the file exist
def check_file_exist(filename):
    is_exist = True
    if not os.path.exists(filename):
        is_exist = False
    return is_exist