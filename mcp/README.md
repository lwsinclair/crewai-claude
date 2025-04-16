# CrewAI MCP Server

This directory contains the Model Control Protocol (MCP) server implementation for CrewAI. The MCP server provides an API for external systems to interact with CrewAI tools.

## Features

- RESTful API to list available tools
- Execute tools remotely through HTTP endpoints
- Integrates with existing CrewAI tools
- Easy to extend with new tools

## Prerequisites

- Python 3.10 or higher
- Dependencies: fastapi, uvicorn, pydantic

## Installation

The dependencies are automatically installed with the main project:

```bash
pip install -e .
```

## Starting the MCP Server

You can start the MCP server using the provided script:

```bash
python -m mcp.start_mcp
```

Or use the entry point after installation:

```bash
start_mcp
```

By default, the server runs on `0.0.0.0:8000`. You can customize this:

```bash
start_mcp --host 127.0.0.1 --port 9000
```

## Available Endpoints

- `GET /`: Root endpoint
- `POST /mcp/tools`: List all available tools
- `POST /mcp/execute`: Execute a tool

## Example Usage

### List all tools

```bash
curl -X POST http://localhost:8000/mcp/tools
```

### Execute a tool

```bash
curl -X POST http://localhost:8000/mcp/execute \
  -H "Content-Type: application/json" \
  -d '{"tool_name": "web_search", "parameters": {"query": "CrewAI tutorial", "num_results": 3}}'
```

## Adding New Tools

To add a new tool to the MCP server:

1. Create a new tool class in `mcp/tools.py`
2. Add the tool to the `MCP_TOOLS` list in `mcp/tools.py`

Example:

```python
class MyNewTool(BaseTool):
    name: str = "my_new_tool"
    description: str = "Description of what my tool does"
    args_schema: Type[BaseModel] = MyNewToolInput

    def _run(self, param1: str, param2: int) -> str:
        # Implementation
        return "Result"

# Add to MCP_TOOLS list
MCP_TOOLS = [
    WebSearchTool(),
    DataAnalysisTool(),
    MyNewTool(),  # Add your new tool here
]
```

## Integrating with Claude

To use this MCP server with Claude:

1. Start the MCP server
2. Configure Claude to use the MCP server URL
3. Claude will automatically discover and use the available tools