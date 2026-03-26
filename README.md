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

👩‍💻 Author

Stav Homsky
