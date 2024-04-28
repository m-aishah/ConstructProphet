from flask import Blueprint, request, jsonify, abort
from .tools import tools


cmnd_tools = Blueprint('cmnd_tools', __name__)


@cmnd_tools.route("/cmnd-tools", methods=['GET'])
def cmnd_tools_endpoint():
    tools_response = [
        {
            "name": tool["name"],
            "description": tool["description"],
            "jsonSchema": tool["parameters"],
            "isDangerous": tool.get("isDangerous", False),
            "functionType": tool["functionType"],
            "isLongRunningTool": tool.get("isLongRunningTool", False),
            "rerun": tool["rerun"],
            "rerunWithDifferentParameters": tool["rerunWithDifferentParameters"],
        } for tool in tools
    ]
    return jsonify({"tools": tools_response})


@cmnd_tools.route("/run-cmnd-tool", methods=['POST'])
def run_cmnd_tool_endpoint():
    data = request.json
    tool_name = data.get('toolName')
    props = data.get('props', {})
    tool = next((t for t in tools if t['name'] == tool_name), None)
    if not tool:
        abort(404, description="Tool not found")
    try:
        result = tool["runCmd"](**props)
        return jsonify(result)
    except Exception as e:
        abort(500, description=str(e))
