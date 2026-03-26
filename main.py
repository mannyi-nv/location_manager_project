import dummy_data
import utils
import view
import validation

# initialize the data
locations = dummy_data.first_init()

while True:
    # print the menu of app
    view.menu()
    # get choice from user
    choice = input("\nChoose an option: ")
    print("\n")
    if choice == "1":
        # calls to show location function
        utils.show_locations(locations)
        input("\nPress Enter to continue...")

    elif choice == "2":
        # calls to add location function
        utils.add_location(locations)
        input("\nPress Enter to continue...")

    elif choice == "3":
        # get location id from the user
        loc_id = int(input("Enter location ID: "))
        # check if the id exist
        is_found = validation.find_id(locations,loc_id)

        #if the id is not found - the user enter id until it valid
        if is_found == False:
            while(is_found == False):
                print('-' * 30)
                print("Error , Please try again ")
                print('-' * 30)
                loc_id = int(input("\nEnter location ID: "))
                is_found = validation.find_id(locations,loc_id)

        # calls to remove location function
        utils.remove_location(locations, loc_id)
        input("\nPress Enter to continue...")

    elif choice == "4":
        # get country name from user
        country = input("Enter country name: ")
        # checks if the country exist in the list
        is_found = validation.find_country(locations , country)

        # if the country not found in list - the user enter country until it found
        if is_found == False:
            while(is_found == False):
                print('-' * 30)
                print("Error , Please try again ")
                print('-' * 30)
                country = input("\nEnter country name: ")
                is_found = validation.find_country(locations , country)

        # calls the filter by country function
        utils.filter_by_country(locations, country)
        input("\nPress Enter to continue...")

    elif choice == "5":
        # get type of vacation from user
        type = input("Enter type of vacation: ")
        # checks if type exist
        is_found = validation.find_type(locations, type)

        # if type not found - the user enter new type until it found
        if is_found == False:
            while(is_found == False):
                print('-' * 30)
                print("Error , Please try again ")
                print('-' * 30)
                type = input("\nEnter type of vacation: ")
                is_found = validation.find_type(locations, type)

        # calls filter by type function
        utils.filter_by_type(locations, type)
        input("\nPress Enter to continue...")

    elif choice == "6":
        # get location id from user
        loc_id = int(input("Enter location ID: "))
        # checks if the id found in list
        is_found = validation.find_id(locations,loc_id)

        # if id not found - the user enter new id until it found
        while(is_found == False):
                print('-' * 30)
                print("Error , Please try again ")
                print('-' * 30)
                loc_id = int(input("\nEnter location ID: "))
                is_found = validation.find_id(locations,loc_id)

        # calls to mark visited function
        utils.mark_visited(locations, loc_id)
        input("\nPress Enter to continue...")

    elif choice == "7":
        print("1. Replace data")
        print("2. Append data")
        # get from user mode for data load
        mode = input("\nChoose mode: ")
        # checks if the mode is valid
        is_good = validation.check_load_mode(mode)
        # if the mode is not valid - user enter new mode until it valid
        while(is_good == False):
            print('-' * 30)
            print("Error , Please try again ")
            print('-' * 30)
            print("1. Replace data")
            print("2. Append data")
            mode = input("\nChoose mode: ")
            is_good = validation.check_load_mode(mode)
        # get file name to load from user
        filename = input("Enter file name: ")
        # checks if the file exist
        is_exist = validation.check_file_exist(filename)

        # if the file is not exist - user enter new file name until it valid
        while(is_exist == False):
            print("File not exist, please try again")
            filename = input("Enter file name: ")
            is_exist = validation.check_file_exist(filename)
        # load the data from the file into locations list
        locations = dummy_data.load_data(filename, mode, locations)

    elif choice == "8":
        # get file name to save from user 
        filename = input("Enter file name to save: (e.g. name.json): ")
        # calls save data function
        dummy_data.save_data(locations, filename)

    elif choice == "9":
        # if the user enter "9", it will exit the app
        break

    else:
        print('-' * 30)
        print("Error , Please try again ")
        print('-' * 30)


    

    
       