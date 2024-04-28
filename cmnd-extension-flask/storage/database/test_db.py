import sqlite3
from data import connect_to_database


# Print all tuples in Projects table
def print_all_projects():
    """
    Retrieves and prints information for all projects stored in the database.

    Args:
        None: This function does not take any arguments.

    Returns:
        None: The function directly prints project information to the console and
              doesn't return any value.
    """
    conn = connect_to_database()
    c = conn.cursor()

    # Retrieve all projects
    c.execute('''SELECT * FROM Projects''')
    projects = c.fetchall()

    if not projects:
        print("No projects found.")
    else:
        print("Projects:")
        for project in projects:
            print("ID:", project[0])
            print("Building Type:", project[1])
            print("Building Size:", project[2])
            print("Project Time Frame:", project[3])
            print("Location:", project[4])
            print("---------------------")

    conn.close()

# Print all tuples in Materials table


def print_all_materials():
    """
    Retrieves and prints information for all materials stored in the database.
    Args:
        None: This function does not take any arguments.
    """
    conn = connect_to_database()
    c = conn.cursor()

    # Retrieve all materials
    c.execute('''SELECT * FROM Materials''')
    materials = c.fetchall()

    if not materials:
        print("No materials found.")
    else:
        print("Materials:")
        for material in materials:
            print("ID:", material[0])
            print("Project ID:", material[1])
            print("Name:", material[2])
            print("Quantity:", material[3])
            print("Price:", material[4])
            print("---------------------")

    conn.close()

# Main function to call print functions


def main():
    """Main driver program to test the functions."""
    print_all_projects()
    print_all_materials()


if __name__ == "__main__":
    main()
