from datetime import datetime
from typing import Dict, Any, Optional

from src.crewai.hierarchical.crew import HierarchicalCrew


def run(inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Run the hierarchical crew with the given inputs.
    
    Args:
        inputs: A dictionary containing inputs for the crew tasks.
                If None, default inputs will be used.
                
    Returns:
        A dictionary with the outputs from the hierarchical crew.
    """
    if inputs is None:
        inputs = {
            'query': 'How has artificial intelligence evolved in the last 5 years and what are its applications in healthcare?',
            'web_query': 'artificial intelligence evolution last 5 years healthcare applications',
            'data_set': 'AI adoption rates in healthcare: 2018=15%, 2019=22%, 2020=35%, 2021=48%, 2022=62%, 2023=78%',
            'analysis_type': 'trends',
            'custom_query': 'Extract key healthcare AI use cases from the research and analysis'
        }

    # Get the current year
    current_year = datetime.now().year
    
    # Create and run the crew
    crew_instance = HierarchicalCrew()
    result = crew_instance.crew().kickoff(
        inputs=inputs
    )
    
    return {'result': result}


def main():
    """Main entry point for the hierarchical crew."""
    print("Starting hierarchical crew...")
    result = run()
    print("\nCrew execution completed!")
    print(f"Output saved to 'hierarchical_result.md'")
    print("\nSummary of result:")
    print(result['result'][:300] + "..." if len(result['result']) > 300 else result['result'])


if __name__ == "__main__":
    main()