from pages.base_page import BasePage
from locators.home_locators import HomeLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

class HomePage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = HomeLocators()

    def navigate_to_twitch_tv(self) -> 'HomePage':
        self.navigate_to()
        return self

    def accept_cookies_if_present(self) -> 'HomePage':
        try:
            if self.is_element_displayed(self.locators.COOKIE_ACCEPT_BUTTON):
                self.click(self.locators.COOKIE_ACCEPT_BUTTON)
        except:
            pass
        return self

    def search_for(self, search_term: str) -> 'HomePage':
        self.wait_for_element_visible(self.locators.BROWSER_OPTION)
        self.click(self.locators.BROWSER_OPTION)
        self.click(self.locators.SEARCH_INPUT_FIELD)
        self.send_keys(self.locators.SEARCH_INPUT_FIELD, search_term + Keys.ENTER)
        self.wait_for_element_visible(self.locators.CHANNELS_SECTION)
        
        return self
