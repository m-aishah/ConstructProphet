import json
from .risk_assesment import (
    get_disaster_probabilities,
    calculate_disaster_probability
)


def scenario_planning(project_name: str, location: str, cost: float, project_time_frame: str):
    """
    Estimates risk change of a project given its location, cost and time frame.

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
    scenarios = {
        "Best Case": {
            "description": "Optimistic scenario where everything goes according to plan.",
            "cost_adjustment": 0.9,
            "time_adjustment": 0.9
        },
        "Worst Case": {
            "description": "Pessimistic scenario with potential delays and cost overruns.",
            "cost_adjustment": 1.3,
            "time_adjustment": 1.5
        },
        # Add more scenarios as needed
    }
    no_months = int(project_time_frame.split(' ')[0])
    no_months *= 12 if 'Year' in project_time_frame or 'year' in project_time_frame else 1
    disaster_probabilities = get_disaster_probabilities(location)
    disaster_probability = calculate_disaster_probability(disaster_probabilities)
    risk = (disaster_probability * 30 + cost * 40 / 100 + no_months * 30 / 100) / 10000

    scenario_analysis = {
        "project_name": project_name
    }
    for scenario, details in scenarios.items():
        adjusted_cost = cost * details["cost_adjustment"]
        adjusted_time_frame = no_months * details["time_adjustment"]
        adjusted_risk = (disaster_probability * 30 + adjusted_cost * 40 /
                         100 + adjusted_time_frame * 30 / 100) / 10000
        scenario_analysis[scenario] = {
            "description": details["description"],
            "adjusted_cost": adjusted_cost,
            "adjusted_time_frame": adjusted_time_frame,
            "base_risk": risk,
            "adjusted_risk": adjusted_risk,
            "risk_change": adjusted_risk - risk
        }

    return json.dumps(scenario_analysis)


def main():
    """Main driver program to test the functions."""
    result = scenario_planning("Test Project", "Lefke", 600000, "1 month")
    print(result)


if __name__ == "__main__":
    main()
