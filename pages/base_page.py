import os
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

load_dotenv()

class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.explicit_wait = int(os.getenv("EXPLICIT_WAIT", 20))
        self.base_url = os.getenv("BASE_URL")

    def navigate_to(self, url: str = "") -> 'BasePage':
        full_url = f"{self.base_url}{url}"
        self.driver.get(full_url)
        return self

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def click(self, locator: Tuple[str, str]) -> 'BasePage':
        element = self.find_element(locator)
        element.click()
        return self

    def send_keys(self, locator: Tuple[str, str], text: str) -> 'BasePage':
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self

    def wait_for_element_visible(self, locator: Tuple[str, str]) -> bool:
        try:
            WebDriverWait(self.driver, self.explicit_wait).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def scroll_down(self) -> 'BasePage':
        self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
        return self

    def scroll_to_element(self, locator: Tuple[str, str]) -> 'BasePage':
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self

    def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
            
    def js_click(self, locator: Tuple[str, str]) -> 'BasePage':
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        return self
