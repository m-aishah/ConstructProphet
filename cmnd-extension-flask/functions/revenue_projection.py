import json
from data import (
    get_market_demand,
    get_price_per_unit,
    get_sales_volume
)


def revenue_projection(project_name: str, building_type: str, project_time_frame: str, location: str):
    """
    Get the revenue projection given building_type, time frame, and location.

    Args:
        project_name (str): The name of the project.
        building_type (str): The type of building (e.g., "Hotel Building").
        project_time_frame (str): The  length of time that the project will take to complete (e.g., "1 Year", "6 Months").
        location (str): The location of the building project.

    Returns:
        dict: A dictionary containing the market_demand, price_per_unit, sales_volume ,and the total revenue projection
        in the specified time frame in a json format.
    """
    market_demand = get_market_demand(building_type, location)
    price_per_unit = get_price_per_unit(building_type, location)
    sales_volume = get_sales_volume(building_type, location)
    no_months = int(project_time_frame.split(' ')[0])
    no_months *= 12 if 'Year' in project_time_frame or 'year' in project_time_frame else 1
    project_revenue_projection = market_demand / 100 * \
        (price_per_unit * sales_volume * no_months / 10)
    data = {
        "project": project_name,
        "market_demand": market_demand,
        "price_per_unit": price_per_unit,
        "sales_volume": sales_volume,
        "revenue_projection": project_revenue_projection
    }
    return json.dumps(data)


def main():
    """Main driver program to test the functions."""
    result = revenue_projection("Test Project", "Hotel Building", "1 month", "Lefke")
    print(result)


if __name__ == "__main__":
    main()
