from src.framework import BrowserUseFramework

def example_search_google():
    """
    Example script demonstrating a simple Google search.
    """
    framework = BrowserUseFramework(llm_model="gpt-4o")
    framework.run_task(
        task_description="Search for 'OpenAI' on Google and click the first result",
        url="https://www.google.com"
    )

if __name__ == "__main__":
    example_search_google()
