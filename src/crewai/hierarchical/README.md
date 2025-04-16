# Hierarchical CrewAI Implementation

This directory contains a hierarchical implementation of CrewAI, where each agent is specialized in using a specific tool. This approach follows the recommended pattern in the [CrewAI documentation](https://docs.crewai.com/how-to/hierarchical-process).

## Structure

- `config/`: Configuration files for agents and tasks
  - `agents.yaml`: Agent definitions with tool specializations
  - `tasks.yaml`: Task definitions for each specialized agent
- `crew.py`: Implementation of the hierarchical crew
- `main.py`: Entry point for running the hierarchical crew

## Agents

The hierarchical implementation includes the following agents:

1. **Manager**: Coordinates the overall process and delegates to specialized agents
2. **Web Researcher**: Specializes in using the web search tool
3. **Data Analyst**: Specializes in using the data analysis tool
4. **Custom Tool Specialist**: Specializes in using the custom tool

## Running the Hierarchical Crew

You can run the hierarchical crew using the following command:

```bash
python -m crewai.hierarchical.main
```

Or, if you've installed the package:

```bash
hierarchical
```

Or:

```bash
run_hierarchical
```

## Custom Inputs

You can customize the inputs to the hierarchical crew by modifying the `inputs` dictionary in `main.py`:

```python
inputs = {
    'query': 'Your main query here',
    'web_query': 'Web search specific query',
    'data_set': 'Data to analyze',
    'analysis_type': 'Type of analysis (summary, trends, correlations)',
    'custom_query': 'Query for custom tool'
}
```

## Integration with MCP

This hierarchical implementation uses tools that are also exposed through the MCP server. This allows:

1. Claude to access the same tools via the MCP server
2. The CrewAI agents to use the tools directly through their specialized roles

## Output

The hierarchical crew saves its output to `hierarchical_result.md` in the project root directory.