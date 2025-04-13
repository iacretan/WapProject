import pytest
import os
from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.streamer_page import StreamerPage

def pytest_configure(config):
    """
    Pytest configuration hook to set up the environment before tests run.
    Creates the screenshots directory if it doesn't exist.
    """
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

@pytest.fixture(scope="function")
def driver():
    """
    Fixture to create and manage the WebDriver instance.
    """
    browser_setup = BrowserSetup()
    driver = browser_setup.get_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    """
    Fixture to create a HomePage instance.
    """
    return HomePage(driver)

@pytest.fixture(scope="function")
def search_results_page(driver):
    """
    Fixture to create a SearchResultsPage instance.
    """
    return SearchResultsPage(driver)

@pytest.fixture(scope="function")
def streamer_page(driver):
    """
    Fixture to create a StreamerPage instance.
    """
    return StreamerPage(driver)
