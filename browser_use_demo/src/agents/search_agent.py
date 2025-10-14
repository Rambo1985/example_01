"""
Agent for performing a web search.
"""
from loguru import logger
from browser_use import BrowserUse


class SearchAgent:
    def __init__(self, browser: BrowserUse):
        self.browser = browser

    def search_and_get_first_result(self, query: str) -> str:
        """
        Performs a Google search and returns the title of the first result.

        Args:
            query: The search query string.

        Returns:
            The title of the first search result.
        """
        logger.info(f"Performing search for: {query}")
        # This is a simplified example. Actual implementation with browser-use would involve
        # calling the agent's run method with a specific prompt.
        # For now, we'll simulate the action.
        # self.browser.go_to_url("https://www.google.com")
        # self.browser.type_text(query, "textarea[name='q']")
        # self.browser.click_element("input[name='btnK']")
        # first_result_title = self.browser.get_element_text("div#search div.g a:first-child h3")
        # return first_result_title

        # Placeholder return for demo
        return f"Simulated first result for '{query}'"