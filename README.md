📍 Locations Manager Project

📖 Description:

This project is a simple command-line application written in Python that allows users to manage a list of locations.

Each location includes:

* ID
* Name
* Country
* Type (e.g., city, nature, etc.)
* Visited status


⚙️ Features:

🔹 Show Locations

Display all saved locations in a clean format.

🔹 Filter Locations by type

Filter locations by type (e.g., show only cities).

🔹 Filter Locations by country

Filter locations by country (e.g., show only France).

🔹 Add Locations

Add a new location.

🔹 Remove Location

Remove location from list. 

🔹 Mark as Visited

Update a location’s visited status.

🔹 Load Data (Challenge 1)

Load locations from a JSON file:

* **Replace** – overwrite current data
* **Append** – add new locations to existing list

🔹 Save Data (Challenge 2)

Save current locations to a JSON file with a custom filename.


 🗂️ Project Structure

`main.py` – handles the menu and user interaction
`utils.py` – helper functions (e.g., printing)
`validation.py` – validate the user input
`dummy_data.py` – loading and saving data
`view.py` - user menu
`data.json` – initial data file

---

▶️ How to Run

1. Make sure you have Python installed
2. Run the main file:

```bash
python main.py
```

---

💡 Notes

* Data is stored in a list of dictionaries
* JSON is used for file storage
* The program supports dynamic user input

---

Open for contribution
-----------------------
Three features to implement:
1. Delete all locations - add an option in the menu that allows the user to delete all the locations at once.
   When the user selects this option the system should ask for confirmation ("Are you sure you want to delete all locations? (y/n)")
   only if the user enters 'y' all locations should be deleted. Else, the operation should be canceled. after delete display a message: "All locations have been deleted".

2. Sort locations by location name - add an option in the menu that allows the user to sort the locations by name (A-Z).
   When the user selects this option , display the sorted list to the user

3. Count locations - add an option in the menu that displays the total number of locations . Example output ("Total locations: 5")
   
   
   
   


