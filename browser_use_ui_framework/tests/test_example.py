from src.framework import BrowserUseFramework

def test_example_task():
    """
    Example test case using the BrowserUseFramework.
    """
    framework = BrowserUseFramework(llm_model="gpt-4o")
    framework.run_task(
        task_description="Find the latest news on BBC News homepage",
        url="https://www.bbc.com/news"
    )

if __name__ == "__main__":
    test_example_task()
