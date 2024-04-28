import json
from data import (
    get_materials,
    get_labors,
    get_equipments,
    get_permits
)


def calculate_material_cost_with_database(building_type, building_size, project_time_frame, location):
    """
    Estimates the total material cost for a project based on details retrieved from the database.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: The estimated total material cost for the specified project. If no project is found in the database,
            returns 0 (assuming zero cost).
    """
    materials = get_materials(building_type, building_size, project_time_frame, location)
    if not materials or materials == []:
        print("Warning: No material found for given specs")
    material_cost = sum(material['qty'] * material['price'] for material in materials)
    return material_cost


def calculate_material_cost(building_type, building_size, project_time_frame, location):
    materials = get_materials(building_type, building_size, project_time_frame, location)
    if not materials or materials == []:
        print("Warning: No material found for given specs")
    material_cost = 0
    for material in materials:
        material_cost += material["qty"] * material["price"]
    return material_cost


def calculate_labor_cost(building_type, building_size, project_time_frame, location):
    """
    Estimates the total labor cost for a project based on its details and labor data.
    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: The estimated total labor cost for the specified project. If no labor data is found,
            returns 0 (assuming zero cost).
    """
    labors = get_labors(building_type, building_size, project_time_frame, location)
    if not labors or labors == []:
        print("Warning: No labor found for given specs")
    labor_cost = 0
    for labor in labors:
        hours_required = labor["time_frame"]["months"] * labor["time_frame"]["weeks_per_month"] * \
            labor["time_frame"]["days_per_week"] * labor["time_frame"]["hours_per_day"]
        labor_cost += labor["pay_per_hour"] * hours_required * labor["pay_per_hour"]
    return labor_cost


def calculate_equipment_cost(building_type, building_size, project_time_frame, location):
    """
    Estimates the total equipment cost for a project based on its details.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: The estimated total equipment cost for the specified project. If no equipment data is found,
            returns 0 (assuming zero cost).
    """
    equipments = get_equipments(building_type, building_size, project_time_frame, location)
    if not equipments or equipments == []:
        print("Warning: No equipments found for given specs")
    equipment_cost = 0
    for equipment in equipments:
        equipment_cost += equipment["qty"] * equipment["price"]

    return equipment_cost


def calculate_permits_cost(building_type, building_size, project_time_frame, location):
    """
    Estimates the total cost of permits required for a project based on its details.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: The estimated total permit cost for the specified project. If no permit data is found,
            returns 0 (assuming zero cost).
    """
    permits = get_permits(building_type, building_size, project_time_frame, location)
    if not permits or permits == []:
        print("Warning: No permits found for given specs")
    permit_cost = 0
    for permit in permits:
        permit_cost += permit["cost"]
    return permit_cost


def calculate_overhead_cost(building_type, building_size, project_time_frame, location):
    """
    Estimates the total cost of overhead required for a project based on its details.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        location (str): The location of the building project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: The estimated total overhead cost for the specified project.
    """
    # To be Implemented.
    return 10000


# ACTUAL COST ESTIMATION FUNCTION
def cost_estimation(project_name: str, building_type: str, building_size: str, project_time_frame: str, location: str):
    """
    Estimates total project cost considering materials, labor, equipment, permits, and overhead.

    Args:
        project_name (str): The name of the construction project.
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        project_time_frame (str): The project's timeframe (e.g., "1 month").
        location (str): The location of the building project.

    Returns:
        str: A JSON string containing the cost estimates for the project, including individual cost breakdowns
            (material, labor, equipment, permits, overhead) and the total project cost.

    Raises:
        Exception: If an error occurs during cost estimation.
    """
    try:
        total_material_cost = calculate_material_cost(
            building_type, building_size, project_time_frame, location)
        total_labor_cost = calculate_labor_cost(
            building_type, building_size, project_time_frame, location)
        total_equipment_cost = calculate_equipment_cost(
            building_type, building_size, project_time_frame, location)
        total_permits_cost = calculate_permits_cost(
            building_type, building_size, project_time_frame, location)
        total_overhead_cost = calculate_overhead_cost(
            building_type, building_size, project_time_frame, location)

        total_cost = total_material_cost + total_labor_cost + \
            total_equipment_cost + total_permits_cost + total_overhead_cost
        cost_estimates = {
            "project_name": project_name,
            "total_material_cost": total_material_cost,
            "total_labor_cost": total_labor_cost,
            "total_equipment_cost": total_equipment_cost,
            "total_permits_cost": total_permits_cost,
            "total_overhead_cost": total_overhead_cost,
            "total_cost": total_cost
        }
        return json.dumps(cost_estimates)
    except Exception as e:
        print("Error in cost_estimation:", e)
        raise e


def main():
    """Main driver program to test the functions."""
    building_type = "Hotel Building"
    building_size = 1
    project_time_frame = "1 month"
    location = "Lefke"
    total_material_cost = calculate_material_cost(
        building_type, building_size, project_time_frame, location)
    total_labor_cost = calculate_labor_cost(
        building_type, building_size, project_time_frame, location)
    total_equipment_cost = calculate_equipment_cost(
        building_type, building_size, project_time_frame, location)
    total_permits_cost = calculate_permits_cost(
        building_type, building_size, project_time_frame, location)
    total_overhead_cost = calculate_overhead_cost(
        building_type, building_size, project_time_frame, location)
    total_cost = cost_estimation("Test Project", building_type,
                                 building_size, project_time_frame, location)
    print("Total Material Cost : ", total_material_cost)
    print("Total Labor Cost : ",  total_labor_cost)
    print("Total Equipment Cost : ", total_equipment_cost)
    print("Total Permits Cost : ", total_permits_cost)
    print("Total Overhead Costs : ", total_overhead_cost)
    print("\n\n")
    print("Total Project Cost : ")
    print(total_cost)
    print("---------------")


if __name__ == "__main__":
    main()
