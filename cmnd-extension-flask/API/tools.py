from pydantic import BaseModel, Field
# from database.data import get_materials
from functions.cost_estimation import cost_estimation
from functions.revenue_projection import revenue_projection
from functions.profitability_analysis import profitability_analysis
from functions.risk_assesment import risk_assesment
from functions.scenario_planning import scenario_planning
from functions.project_forecast import project_forecast

class CostEstimationSchema(BaseModel):
    project_name: str = Field(..., title="Project", description="Project name required")
    building_type: str = Field(..., title="Type of building", description="The type of building")
    building_size:  str = Field(..., title="Size of the building", description="Size of building")
    project_time_frame:  str = Field(..., title="Proposed time to build",
                                     description="Proposed time frame to complete the project")
    location: str = Field(..., title=" location to build",
                          description="Location the building is to be constructed")
    # labor_specs: list = Field( title="Labor specifications", description="Labor categories, quantities and rates required")
    # equipment_specs: list = Field(title="Equipment specifications", description="Equipment name and quantities required")
    # overhead_specs: list = Field(title="Overhead specifications", description="Overhead specifications required")


class RevenueProjectionSchema(BaseModel):
    project_name: str = Field(..., title="Project", description="Project name required")
    building_type: str = Field(..., title="Type of building", description="The type of building")
    project_time_frame: str = Field(..., title="Proposed time to build",
                                    description="Proposed time frame to complete the project")
    location: str = Field(..., title=" location to build",
                          description="Location the building is to be constructed")


class ProfitabilityAnalysisSchema(BaseModel):
    project_name: str = Field(..., title="Project", description="Project name required")
    cost: float = Field(..., title="Cost", description="Cost required")
    revenue: float = Field(..., title="Revenue", description="Revenue required")
    project_time_frame: str = Field(..., title="Proposed time to build",
                                    description="Proposed time frame to complete the project")


class RiskAssesmentSchema(BaseModel):
    project_name: str = Field(..., title="Project", description="Project name required")
    location: str = Field(..., title=" location to build",
                          description="Location the building is to be constructed")
    cost: float = Field(..., title="Cost", description="Cost required")
    project_time_frame: str = Field(..., title="Proposed time to build",
                                    description="Proposed time frame to complete the project")


class ScenarioPlanningSchema(BaseModel):
    project_name: str = Field(..., title="Project", description="Project name required")
    location: str = Field(..., title=" location to build",
                          description="Location the building is to be constructed")
    cost: float = Field(..., title="Cost", description="Cost required")
    project_time_frame: str = Field(..., title="Proposed time to build",
                                    description="Proposed time frame to complete the project")

# class TimeFrameEstimationSchema(BaseModel):
#     project_name: str = Field(..., title="Project", description="Project name required")

class ProjectForecastSchema(BaseModel):
    project_name: str = Field(..., title="Project", description="Project name required")
    building_type: str = Field(..., title="Type of building", description="The type of building")
    building_size:  str = Field(..., title="Size of the building", description="Size of building")
    project_time_frame:  str = Field(..., title="Proposed time to build",
                                     description="Proposed time frame to complete the project")
    location: str = Field(..., title=" location to build",
                          description="Location the building is to be constructed")


def custom_json_schema(model):
    schema = model.schema()
    properties_formatted = {
        k: {
            "title": v.get("title"),
            "type": v.get("type")
        } for k, v in schema["properties"].items()
    }

    return {
        "type": "object",
        "default": {},
        "properties": properties_formatted,
        "required": schema.get("required", [])
    }


tools = [
    {
        "name": "cost_estimation",
        "description": "Calculates and returns the costs of constructing a building based on the parameters passed to it.",
        "parameters": custom_json_schema(CostEstimationSchema),
        "runCmd": cost_estimation,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    },
    {
        "name": "revenue_projection",
        "description": "",
        "parameters": custom_json_schema(RevenueProjectionSchema),
        "runCmd": revenue_projection,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    },
    {
        "name": "profitability_analysis",
        "description": "",
        "parameters": custom_json_schema(ProfitabilityAnalysisSchema),
        "runCmd": profitability_analysis,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    },
    {
        "name": "risk_assesment",
        "description": "",
        "parameters": custom_json_schema(RiskAssesmentSchema),
        "runCmd": risk_assesment,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    },
    {
        "name": "scenario_planning",
        "description": "",
        "parameters": custom_json_schema(ScenarioPlanningSchema),
        "runCmd": scenario_planning,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    },
    {
        "name": "project_forecast",
        "description": "Calculates and returns the costs of constructing a building based on the parameters passed to it.",
        "parameters": custom_json_schema(ProjectForecastSchema),
        "runCmd": project_forecast,
        "isDangerous": False,
        "functionType": "backend",
        "isLongRunningTool": False,
        "rerun": True,
        "rerunWithDifferentParameters": True
    },
]
