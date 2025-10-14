"""
Utility functions for browser automation tasks.
"""
from loguru import logger
from browser_use import BrowserUse


def create_browser_session(headless: bool = False) -> BrowserUse:
    """
    Creates and returns a new browser session.

    Args:
        headless: Whether to run the browser in headless mode. Defaults to False.

    Returns:
        A new instance of BrowserUse.
    """
    logger.info("Creating new browser session (headless={})", headless)
    return BrowserUse(headless=headless)


def close_browser_session(browser: BrowserUse):
    """
    Closes the given browser session.

    Args:
        browser: The BrowserUse instance to close.
    """
    logger.info("Closing browser session")
    browser.close()