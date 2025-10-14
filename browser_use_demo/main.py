"""
Main entry point for the browser automation demo.
"""
from loguru import logger
from src.utils.browser_helpers import create_browser_session, close_browser_session
from src.agents.search_agent import SearchAgent


def main():
    """
    Main function to run the automation demo.
    """
    logger.info("Starting browser automation demo")
    browser = create_browser_session(headless=True) # Use headless mode for demo
    try:
        search_agent = SearchAgent(browser)
        result = search_agent.search_and_get_first_result("Python programming")
        logger.info(f"Search result: {result}")
    finally:
        close_browser_session(browser)
    logger.info("Demo finished")


if __name__ == "__main__":
    main()