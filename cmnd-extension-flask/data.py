# Options
building_types_options = ["Hotel Building", "Bar", "Hostel"]
building_size_options = [1, 2]  # Number of floors
project_time_frame_options = ["1 month", "2 month"]
location_options = ["Lefke", "Lefkosa"]

# Records for cost estimation
cost_estimation_records = [
    {
        "building_type": "Hotel Building",
        "building_size": 1,
        "project_time_frame": "1 month",
        "location": "Lefke",
        "materials": [
            {
                "name": "Cement",
                "qty": 10,
                "price": 50
            },
            {
                "name": "Glass",
                "qty": 9,
                "price": 70
            },
            {
                "name": "Iron",
                "qty": 2,
                "price": 60
            }
        ],
        "labors": [
            {
                "category": "Architect",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 25,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Plumber",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 25,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Constructor",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 25,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            }
        ],
        "equipments": [
            {
                "name": "Cranes",
                "qty": 5,
                "price": 400
            },
            {
                "name": "Graders",
                "qty": 9,
                "price": 350
            },
            {
                "name": "Pavers",
                "qty": 2,
                "price": 700
            },
            {
                "name": "Bulldozers",
                "qty": 28,
                "price": 800
            }
        ],
        "permits": [
            {
                "type": "land_permit",
                "cost": 1000
            },
        ]
    },

    {
        "building_type": "Bar Building",
        "building_size": 2,
        "project_time_frame": "5 month",
        "location": "Iskele",
        "materials": [
            {
                    "name": "Cement",
                    "qty": 10,
                    "price": 50
            },
            {
                "name": "Glass",
                "qty": 9,
                "price": 70
            },
            {
                "name": "Iron",
                "qty": 2,
                "price": 60
            },
            {
                "name": "Wood",
                "qty": 28,
                "price": 65.4
            }
        ],
        "labors": [
            {
                "category": "Architect",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 5,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Plumber",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 5,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Constructor",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 5,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            }
        ],
        "equipments": [
            {
                "name": "Cranes",
                "qty": 5,
                "price": 400
            },
            {
                "name": "Graders",
                "qty": 9,
                "price": 350
            },
            {
                "name": "Pavers",
                "qty": 2,
                "price": 700
            },
            {
                "name": "Bulldozers",
                "qty": 28,
                "price": 800
            }
        ],
        "permits": [
            {
                "type": "land_permit",
                "cost": 1000
            },
        ]
    },

    {
        "building_type": "Mall Building",
        "building_size": 15,
        "project_time_frame": "8 month",
        "location": "Lefkosa",
        "materials": [
            {
                "name": "Cement",
                "qty": 100,
                "price": 50
            },
            {
                "name": "Glass",
                "qty": 90,
                "price": 70
            },
            {
                "name": "Iron",
                "qty": 78,
                "price": 55.5
            },
            {
                "name": "Sand in kilos",
                "qty": 10,
                "price": 50
            },
            {
                "name": "Wood",
                "qty": 9,
                "price": 70
            },
            {
                "name": "Stones",
                "qty": 27,
                "price": 60
            }
        ],
        "labors": [
            {
                "category": "Architect",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 25,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Plumber",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 25,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Constructor",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 25,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            }
        ],
        "equipments": [
            {
                "name": "Cranes",
                        "qty": 5,
                        "price": 400
            },
            {
                "name": "Graders",
                        "qty": 9,
                        "price": 350
            },
            {
                "name": "Pavers",
                        "qty": 2,
                        "price": 700
            },
            {
                "name": "Bulldozers",
                        "qty": 28,
                        "price": 800
            }
        ],
        "permits": [
            {
                "type": "land_permit",
                "cost": 1000
            },
        ]
    },

    {
        "building_type": "Hotel",
        "building_size": "5 floor",
        "project_time_frame": "1 year",
        "location": "Iskele",
        "materials": [
            {
                "name": "Cement",
                "qty": 100,
                "price": 50.3
            },
            {
                "name": "Glass",
                "qty": 90,
                "price": 70
            },
            {
                "name": "Iron",
                "qty": 78,
                "price": 44.5
            },
            {
                "name": "Sand in kilos",
                "qty": 10,
                "price": 21.11
            },
            {
                "name": "Wood",
                "qty": 9,
                "price": 71
            },
            {
                "name": "Stones",
                "qty": 27,
                "price": 60.5
            }
        ],
        "labors": [
            {
                "category": "Architect",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 19,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Plumber",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 15,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Constructor",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 17,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            }
        ],
        "equipments": [
            {
                "name": "Cranes",
                        "qty": 5,
                        "price": 400
            },
            {
                "name": "Graders",
                        "qty": 9,
                        "price": 350
            },
            {
                "name": "Pavers",
                        "qty": 2,
                        "price": 700
            },
            {
                "name": "Bulldozers",
                        "qty": 28,
                        "price": 800
            }
        ],
        "permits": [
            {
                "type": "land_permit",
                "cost": 1000
            },
        ]
    },

    {
        "building_type": "Hotel",
        "building_size": "5 floors",
        "project_time_frame": "1 year",
        "location": "Iskele",
        "materials": [
            {
                "name": "Cement",
                "qty": 100,
                "price": 50.3
            },
            {
                "name": "Glass",
                "qty": 90,
                "price": 70
            },
            {
                "name": "Iron",
                "qty": 78,
                "price": 44.5
            },
            {
                "name": "Sand in kilos",
                "qty": 10,
                "price": 21.11
            },
            {
                "name": "Wood",
                "qty": 9,
                "price": 71
            },
            {
                "name": "Stones",
                "qty": 27,
                "price": 60.5
            }
        ],
        "labors": [
            {
                "category": "Architect",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 2,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            },
            {
                "category": "Plumber",
                "occupation": 10,
                "number_of_workers": 50,
                "pay_per_hour": 2,
                "time_frame": {
                    "months": 10,
                    "weeks_per_month": 3,
                    "days_per_week": 4,
                    "hours_per_day": 3
                }
            }
        ],
        "equipments": [
            {
                "name": "Cranes",
                        "qty": 5,
                        "price": 400
            },
            {
                "name": "Graders",
                        "qty": 9,
                        "price": 350
            },
            {
                "name": "Pavers",
                        "qty": 2,
                        "price": 700
            },
            {
                "name": "Bulldozers",
                        "qty": 28,
                        "price": 800
            }
        ],
        "permits": [
            {
                "type": "land_permit",
                "cost": 1000
            },
        ]
    }
]

# Records for revenue projection
revenue_records = [
    {
        "building_type": "Hotel Building",
        "building_size": 1,  # SIze in floors
        "project_time_frame": "1 month",
        "location": "Lefke",
        "market_demand_score": 24.5,
        "price_per_unit": 50000,
        "sales_volume": 12
    },
    {
        "building_type": "Hotel",
        "building_size": "5 floor",
        "project_time_frame": "1 year",
        "location": "Iskele",
        "market_demand_score": 72.89,
        "price_per_unit": 125000,
        "sales_volume": 10
    },
    {
        "building_type": "Hotel",
        "building_size": "5 floors",
        "project_time_frame": "1 year",
        "location": "Iskele",
        "market_demand_score": 72.89,
        "price_per_unit": 125000,
        "sales_volume": 10
    }
]

# Records for risk assessment
risk_assessment_records = {
    "hurricane": 5,
    "earthquake": 3,
    "flood": 7,
    "wildfire": 4,
    "tornado": 1,
    "tsunami": 9,
    "volcanic eruption": 6,
    "cyclone": 2,
    "drought": 8,
    "heatwave": 10,
    "cold wave": 0,
    "storm surge": 4
}

# Get functions for risk assessment


def get_disaster_probabilities(location):

    return risk_assessment_records

# Get functions for cost estimation


def get_materials(building_type, building_size, project_time_frame, location):
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
    materials_list = []
    try:
        for record in cost_estimation_records:
            if (record["building_type"] == building_type and
                record["building_size"] == building_size and
                record["location"] == location and
                    record["project_time_frame"] == project_time_frame):
                materials_list = record["materials"]
    except:
        print('Warning: Specification not in record!')
    return materials_list


def get_labors(building_type, building_size, project_time_frame, location):
    """
    Retrieves labor data associated with a project based on its details.

    Args:
        building_type (str): The type of building (e.g., "Resort Center, ").
        building_size (int): The size of the building.
        project_time_frame (str): The project's timeframe (e.g., "1 month").
        location (str): The location of the building project.

    Returns:
        list: A list containing labor data (potentially empty) if a matching record is found.
                An empty list if no matching record is found.

    Raises:
        Exception: (Optional) Consider adding explicit exception handling for specific errors
                encountered while accessing the data source (if applicable).
    """
    labor_list = []
    try:
        for record in cost_estimation_records:
            if (record["building_type"] == building_type and
                record["building_size"] == building_size and
                record["location"] == location and
                    record["project_time_frame"] == project_time_frame):
                labor_list = record["labors"]
    except:
        print('Warning: Specification not in record!')
    return labor_list


def get_equipments(building_type, building_size, project_time_frame, location):
    equipment_list = []
    try:
        for record in cost_estimation_records:
            if (record["building_type"] == building_type and
                record["building_size"] == building_size and
                record["location"] == location and
                    record["project_time_frame"] == project_time_frame):
                equipment_list = record["equipments"]

    except:
        print('Warning: Specification not in record!')
    return equipment_list


def get_permits(building_type, building_size, project_time_frame, location):
    permit_list = []
    try:
        for record in cost_estimation_records:
            if (record["building_type"] == building_type and
                record["building_size"] == building_size and
                record["location"] == location and
                    record["project_time_frame"] == project_time_frame):
                permit_list = record["permits"]

    except:
        print('Warning: Specification not in record!')
    return permit_list


# Get functions for revenue projection
def get_market_demand(building_type, location):
    """
    Get the market demand for a given property type and location.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        location (str): The location of the building project.

    Returns:
        int: An integer between 0 and 100 representing how much the market demand is.
    """
    market_demand_score = 0
    try:
        for record in revenue_records:
            if (record["building_type"] == building_type and
                    record["location"] == location
                ):
                market_demand_score = record["market_demand_score"]
    except:
        print('Warning: Specification not in revenue record!')
    return market_demand_score


def get_price_per_unit(building_type, location):
    """
    Get the price per unit given property type and location.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        location (str): The location of the building project.

    Returns:
        int: An integer representing the average price per one unit.
    """
    price_per_unit = 0
    try:
        for record in revenue_records:
            if (record["building_type"] == building_type and
                    record["location"] == location
                ):
                price_per_unit = record["price_per_unit"]
    except:
        print('Warning: Specification not in revenue record!')
    return price_per_unit


def get_sales_volume(building_type, location):
    """
    Get the sales volume given property type and location.

    Args:
        building_type (str): The type of building (e.g., "Hotel Building").
        location (str): The location of the building project.

    Returns:
        int: An integer representing the expected number of units sold per month.
    """
    sales_volume = 0
    try:
        for record in revenue_records:
            if (record["building_type"] == building_type and
                    record["location"] == location
                ):
                sales_volume = record["sales_volume"]
    except:
        print('Warning: Specification not in revenue record!')
    return sales_volume


# Test
if __name__ == "__main__":
    materials = get_materials("Hotel Building", 1, "1 month", "Lefke")
    print(materials)
    print()
    materials = get_labors("Hotel Building", 1, "1 month", "Lefke")
    print(materials)
    print()
    materials = get_equipments("Hotel Building", 1, "1 month", "Lefke")
    print(materials)
