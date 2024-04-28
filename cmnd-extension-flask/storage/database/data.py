import sqlite3
import os

# Connect to the database


def connect_to_database():
    """Connect to the database using sqlite3."""
    conn = sqlite3.connect('building_projects.db')
    return conn

# Create tables


def create_tables():
    """
        Establishes essential tables  data management:
        - Projects: Stores project details like type, size, timeframe, and location.
        - Materials: Links to projects and stores material names, quantities, and prices.
    """
    conn = connect_to_database()
    c = conn.cursor()

    # Create Projects table
    c.execute('''CREATE TABLE IF NOT EXISTS Projects
                 (id INTEGER PRIMARY KEY,
                  building_type TEXT,
                  building_size INTEGER,
                  project_time_frame TEXT,
                  location TEXT)''')

    # Create Materials table
    c.execute('''CREATE TABLE IF NOT EXISTS Materials
                 (id INTEGER PRIMARY KEY,
                  project_id INTEGER,
                  name TEXT,
                  qty INTEGER,
                  price INTEGER,
                  FOREIGN KEY(project_id) REFERENCES Projects(id))''')

    conn.commit()
    conn.close()

# Insert data into tables


def insert_data():
    """
        Populates material tables with sample data:
        - Projects table receives sample project entries with type, size, timeframe, and location.
        - Materials table receives sample material entries linked to projects, including name, quantity, and price.
    """
    projects_data = [
        ("Hotel Building", 1, "1 month", "Lefke"),
        ("Bar", 2, "1 month", "Lefkosa"),
        ("Hotel Building", 3, "1 month", "Lefke")
    ]

    materials_data = [
        (1, "Cement", 10, 50),
        (1, "Glass", 9, 70),
        (1, "Iron", 2, 60)
    ]

    conn = connect_to_database()
    c = conn.cursor()

    # Insert data into Projects table
    c.executemany(
        "INSERT INTO Projects (building_type, building_size, project_time_frame, location) VALUES (?, ?, ?, ?)", projects_data)

    # Insert data into Materials table
    c.executemany(
        "INSERT INTO Materials (project_id, name, qty, price) VALUES (?, ?, ?, ?)", materials_data)

    conn.commit()
    conn.close()

# Get materials for a project


def get_materials(building_type, building_size, location, project_time_frame):
    """
    Retrieves materials associated with a project based on its details.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        list: A list of dictionaries containing material information (name, quantity, price)
              for the specified project. If no project is found, returns an empty list.
    """
    conn = connect_to_database()
    c = conn.cursor()

    # Retrieve project_id based on project details
    c.execute('''SELECT id FROM Projects
                 WHERE building_size=? AND building_type=? AND location=? AND project_time_frame=?''',
              (building_size, building_type, location, project_time_frame))
    project_id = c.fetchone()

    if not project_id:
        print("Project not found.")
        return []

    # Retrieve materials for the project
    c.execute('''SELECT name, qty, price FROM Materials
                 WHERE project_id=?''', (project_id[0],))
    materials = [{'name': row[0], 'qty': row[1], 'price': row[2]} for row in c.fetchall()]

    conn.close()
    return materials

# Calculate material cost for a project


def calculate_material_cost(building_size, building_type, location, project_time_frame):
    """
    Estimates the total material cost for a project based on its details.

    Args:
        building_size (int): The size of the building.
        building_type (str): The type of building (e.g., "Hotel Building").
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: The estimated total material cost for the specified project. If no project
        is found, returns 0 (assuming zero cost).
    """
    materials = get_materials(building_size, building_type, location, project_time_frame)
    material_cost = sum(material['qty'] * material['price'] for material in materials)
    return material_cost

# Function to delete the database file


def delete_database():
    """
    Safely deletes the specified database file (if it exists).

    Args:
        database_file (str, optional): The path to the database file to be deleted.
          Defaults to "building_projects.db".

    Returns:
        None: The function modifies the file system and doesn't return a value.
    """

    db_file = 'building_projects.db'
    if os.path.exists(db_file):
        os.remove(db_file)
        print("Database deleted successfully.")
    else:
        print("Database file does not exist.")

# Main function


def main():
    """Main driver program to test the functions."""
    delete_database()  # Optional: delete existing database
    create_tables()
    insert_data()

    # Example usage of get_material_cost function
    building_size = 1
    building_type = "Hotel Building"
    location = "Lefke"
    project_time_frame = "1 month"

    material_cost = calculate_material_cost(
        building_size, building_type, location, project_time_frame)
    print("Total material cost:", material_cost)


if __name__ == "__main__":
    main()
