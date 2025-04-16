"""
Custom tool implementation for CrewAI MCP integration.
"""
from typing import Type
from pydantic import BaseModel, Field

# Ensure BaseTool is available
try:
    from src.crewai.tools import BaseTool
except ImportError:
    # Fallback implementation if BaseTool is not found
    class BaseTool:
        name: str = "base_tool"
        description: str = "Base tool class"
        
        def _run(self, **kwargs):
            raise NotImplementedError("Tool not implemented")

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    text: str = Field(..., description="The text to process.")

class MyCustomTool(BaseTool):
    """Example custom tool for demonstration purposes."""
    name: str = "my_custom_tool"
    description: str = "A custom tool that demonstrates CrewAI tool integration with MCP."
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, text: str) -> str:
        """Process the input text and return a result."""
        return f"Processed text: {text}\nThis is a custom CrewAI tool integrated with MCP."
