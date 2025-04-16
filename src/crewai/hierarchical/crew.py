from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool

# Import our tools from MCP
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
try:
    from mcp.tools import WebSearchTool, DataAnalysisTool
    from src.crewai.tools.custom_tool import MyCustomTool
except ImportError:
    # Mock implementations if imports fail
    from typing import Type
    from pydantic import BaseModel, Field
    
    class BaseTool:
        name: str = "base_tool"
        description: str = "Base tool description"
        
        def _run(self, **kwargs):
            return "Base tool implementation"
    
    class WebSearchTool(BaseTool):
        name: str = "web_search"
        description: str = "Searches the web for information"
        
        def _run(self, query: str, num_results: int = 5) -> str:
            return f"Mock search results for '{query}'"
            
    class DataAnalysisTool(BaseTool):
        name: str = "data_analysis"
        description: str = "Analyzes data and provides insights"
        
        def _run(self, data: str, analysis_type: str) -> str:
            return f"Mock analysis of data with type {analysis_type}"
            
    class MyCustomTool(BaseTool):
        name: str = "Name of my tool"
        description: str = "Description of my custom tool"
        
        def _run(self, argument: str) -> str:
            return f"Mock output for custom tool with argument: {argument}"


@CrewBase
class HierarchicalCrew():
    """Hierarchical Crew with tool-specific agents"""

    # Load configs from hierarchical config files
    agents_config = 'hierarchical/config/agents.yaml'
    tasks_config = 'hierarchical/config/tasks.yaml'

    # Define tools
    web_search_tool = WebSearchTool()
    data_analysis_tool = DataAnalysisTool()
    custom_tool = MyCustomTool()

    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
            verbose=True
        )

    @agent
    def web_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['web_researcher'],
            tools=[self.web_search_tool],
            verbose=True
        )

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst'],
            tools=[self.data_analysis_tool],
            verbose=True
        )

    @agent
    def custom_tool_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['custom_tool_specialist'],
            tools=[self.custom_tool],
            verbose=True
        )

    @task
    def manager_task(self) -> Task:
        return Task(
            config=self.tasks_config['manager_task'],
            output_file='hierarchical_result.md'
        )

    @task
    def web_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_research_task'],
        )

    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis_task'],
        )

    @task
    def custom_tool_task(self) -> Task:
        return Task(
            config=self.tasks_config['custom_tool_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates a hierarchical crew with tool-specific agents"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=self.manager,
        )