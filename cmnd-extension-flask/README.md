
# ConstructProphet AI

## Description

This project provides a suite of tools for construction planning and decision-making. These tools enable users to perform various tasks such as cost estimation, revenue projection, profitability analysis, risk assessment, and scenario planning for construction projects.

The project consists of the following components:
- `tools.py`: Defines Pydantic schemas for input parameters and implements functions for each tool.
- `endpoints.py`: Implements Flask endpoints to expose the CMND tools as REST APIs.
- `functions/`: Directory containing Python modules for each CMND tool.

## Tools Overview

### Cost Estimation
- **Description:** Calculates the costs of constructing a building based on input parameters.
- **Parameters:**
  - Project Name
  - Type of Building
  - Size of the Building
  - Proposed Time to Build
  - Location to Build
- **Function:** `cost_estimation`

### Revenue Projection
- **Description:** Projects revenue for a construction project based on market demand, price per unit, and sales volume.
- **Parameters:**
  - Project Name
  - Type of Building
  - Proposed Time to Build
  - Location to Build
- **Function:** `revenue_projection`

### Profitability Analysis
- **Description:** Analyzes the profitability of a construction project based on costs and revenue.
- **Parameters:**
  - Project Name
  - Cost
  - Revenue
  - Proposed Time to Build
- **Function:** `profitability_analysis`

### Risk Assessment
- **Description:** Assesses the risk level of a construction project based on location, cost, and project time frame.
- **Parameters:**
  - Project Name
  - Location to Build
  - Cost
  - Proposed Time to Build
- **Function:** `risk_assessment`

### Scenario Planning
- **Description:** Provides scenarios for construction projects considering best and worst-case scenarios.
- **Parameters:**
  - Project Name
  - Location to Build
  - Cost
  - Proposed Time to Build
- **Function:** `scenario_planning`

### Project Forecast
- **Description:** Combines cost estimation, revenue projection, profitability analysis, risk assessment, and scenario planning to provide a comprehensive forecast for a construction project.
- **Parameters:**
  - Project Name
  - Type of Building
  - Size of the Building
  - Proposed Time to Build
  - Location to Build
- **Function:** `project_forecast`

## Setup and Usage

### Installation
1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.

### Running the API
1. Navigate to the `API` directory.
2. Run `python app.py` to start the Flask server.
3. The API will be accessible at `http://localhost:5000` or using ngrok to create a server.

### Using the Tools
- Make POST requests to `/run-cmnd-tool` endpoint with tool name and parameters to execute specific tools.
- Make GET requests to `/cmnd-tools` endpoint to get information about available tools and their parameters.

## Folder Structure
- `API/`: Contains Flask application files.
- `functions/`: Contains Python modules for CMND tools.

## Contributors
- [Aishah Mabayoje](https://github.com/m-aishah)
- [Abdelrahman Mostafa](https://github.com/abdomody35)
- [Godfrey Dekera](https://github.com/godfreydekew)

## License
This project is licensed under the [MIT License](LICENSE).
