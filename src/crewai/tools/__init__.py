"""
Tools for CrewAI.
"""
from typing import List, Dict, Any, Callable, Optional, Union, Type

class BaseTool:
    """Base class for all CrewAI tools."""
    name: str = "base_tool"
    description: str = "Base tool class"
    
    def _run(self, **kwargs):
        """Execute the tool's functionality."""
        raise NotImplementedError("Tool not implemented")
