from browser_use import Agent

class BrowserUseFramework:
    """
    A wrapper class for browser-use Agent to provide a structured framework for UI automation.
    """
    def __init__(self, llm_model: str = "gpt-4o", max_steps: int = 100):
        self.agent = Agent(llm=llm_model, max_steps=max_steps)

    def run_task(self, task_description: str, url: str):
        """
        Executes a single task using the browser-use agent.

        Args:
            task_description (str): The description of the task to perform.
            url (str): The starting URL for the task.
        """
        print(f"Starting task: {task_description} on {url}")
        self.agent.get(url).run(task_description)
