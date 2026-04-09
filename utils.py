# function that show all the locations in the list
def show_locations(locations):
    print(f"{'ID':<5}{'Name':<15}{'Country':<15}{'Type':<10}{'Visited':<10}")
    print("-" * 55)
    # loop through locations list
    for location in locations:
        print(f"{location['id']:<5}{location['name']:<15}{location['country']:<15}{location['type']:<10}{location['visited']:<10}")

# function that show only the locations of specific country 
def filter_by_country(locations, country):
    print("\n")
    print(f"{'ID':<5}{'Name':<15}{'Country':<15}{'Type':<10}{'Visited':<10}")
    print("-" * 55)
    # loop through locations list
    for location in locations:
        if location["country"] == country:
            print(f"{location['id']:<5}{location['name']:<15}{location['country']:<15}{location['type']:<10}{location['visited']:<10}")
       
# function that show only the locations of specific type of vacation
def filter_by_type(locations , type):
    print("\n")
    print(f"{'ID':<5}{'Name':<15}{'Country':<15}{'Type':<10}{'Visited':<10}")
    print("-" * 55)
    # loop through locations list
    for location in locations:
        if location["type"] == type:
            print(f"{location['id']:<5}{location['name']:<15}{location['country']:<15}{location['type']:<10}{location['visited']:<10}")

# function that adds new location to the list
def add_location(locations):
    # get location name , country and type input from user
    name = input("Enter location name: ")
    country = input("Enter country name: ")
    type = input("Enter type of vacation: ")
    new_location = {"id": len(locations)+1 , "name": name , "country": country , "type" : type , "visited" : "❌"}
    print(f"\nnew location to be added: {new_location}")
    user_conf = input(f"\nPlease type 'YES / NO' to confirm: ").lower()
    if user_conf == "yes":
        # add the new location to the list
        locations.append(new_location)
        print("\nLocation added successfully")
    else:
        print("\nLocation not added")

# function that remove location in list by id
def remove_location(locations, loc_id):
    # remove location from list
    locations.pop(loc_id - 1)
    print("\nLocation deleted!")
       
# function that marks a location as visited
def mark_visited(locations , loc_id):
    locations[loc_id - 1]["visited"] = "✅"
    print("\nLocation marked as visited")
