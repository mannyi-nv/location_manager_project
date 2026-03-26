import json

# load data from file with 2 mode - replace or append
def load_data(filename, mode, locations):
    # open the file
    with open(filename, "r") as file:
        # load data from file to data variable
        data = json.load(file)

        if mode == "1":
            return data
        elif mode == "2":
            # add the data from file to existing data
            locations.extend(data)
            return locations
        
# load the data from json file
def first_init():
    # open the file
    with open("data.json", "r") as file:
        # load data from file
        data = json.load(file)
        return data
    
# save the data into new file
def save_data(locations, filename):
    # open the file
    with open(filename , "w") as file:
        json.dump(locations, file, indent=4)
    print("File saved successfully")