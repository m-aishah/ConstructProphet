import json
from .cost_estimation import cost_estimation
from .revenue_projection import revenue_projection
from .profitability_analysis import profitability_analysis
from .risk_assesment import risk_assesment
from .scenario_planning import scenario_planning

# Wrapper Function


def project_forecast(project_name, building_type, building_size, project_time_frame, location):
    """
    Performs overall forecast for a project considering the type, size, time frame, and location.

    Args:
        project_name (str): The name of the construction project.
        building_type (str): The type of building (e.g., "Hotel Building").
        building_size (int): The size of the building.
        project_time_frame (str): The project's timeframe (e.g., "1 month").
        location (str): The location of the building project.

    Returns:
        str: A JSON string containing the overall forecast for the project, including the cost estimates, revenue projection,
        profitability analysis, risk assesment, and scenario planning.
    """
    cost_estimates = json.loads(cost_estimation(
        project_name, building_type, building_size, project_time_frame, location))
    revenue_projections = json.loads(revenue_projection(
        project_name, building_type, project_time_frame, location))
    profitability_statistics = json.loads(profitability_analysis(
        project_name, cost_estimates["total_cost"], revenue_projections["revenue_projection"], project_time_frame))
    risk_assesments = json.loads(risk_assesment(project_name, location,
                                 cost_estimates["total_cost"], project_time_frame))
    scenarios = json.loads(scenario_planning(project_name, location,
                           cost_estimates["total_cost"], project_time_frame))
    return json.dumps(cost_estimates | revenue_projections | profitability_statistics | risk_assesments | scenarios)


def main():
    result = project_forecast("CourtYard", "Hotel", "5 floor", "1 year", "Iskele")
    print(result)

if __name__ == '__main__':
    main()
