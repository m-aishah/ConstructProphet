import json
from data import get_disaster_probabilities


def calculate_disaster_probability(disaster_probabilities):
    """
    Calculate the probability of a disaster  occurring.

    Args:
        disaster_probabilities (dict): The probabilities for different types of natural disasters.

    Returns:
        float: A float representing the percentage of a disaster occurring.
    """
    return sum(x for x in disaster_probabilities.values()) / len(disaster_probabilities)


def risk_assesment(project_name: str, location: str, cost: float, project_time_frame: str):
    """
    Estimates the risk for a project given its location, cost, and time frame.

    Args:
        project_name (str): The name of the construction project.
        location (str): The location of the building project.
        cost (float): The cost of building the project.
        project_time_frame (str): The project's timeframe (e.g., "1 month").

    Returns:
        float: A float number between 0 and 100 describing the estimated risk for the specified project.
    """
    no_months = int(project_time_frame.split(' ')[0])
    no_months *= 12 if 'Year' in project_time_frame or 'year' in project_time_frame else 1
    disaster_probabilities = get_disaster_probabilities(location)
    data = {
        "project": project_name
    }
    for key, value in disaster_probabilities.items():
        data[key] = str(value) + " %"
    disaster_probability = calculate_disaster_probability(disaster_probabilities)
    data["total_disaster_probability"] = disaster_probability
    risk = (disaster_probability * 30 + cost * 40 / 100 + no_months * 30 / 100) / 10000
    data["risk_level"] = risk
    return json.dumps(data)


def main():
    """Main driver program to test the functions."""
    result = calculate_disaster_probability({"flood": 3,  "fire": 1})
    print(result)
    print("\n\n")
    result = risk_assesment("Test Project", "Lefke", 600000, "1 month")
    print(result)


if __name__ == "__main__":
    main()
