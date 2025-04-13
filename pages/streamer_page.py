from pages.base_page import BasePage
from locators.streamer_page_locators import StreamerPageLocators
from utils.browser_setup import BrowserSetup
from selenium.webdriver.remote.webdriver import WebDriver

class StreamerPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = StreamerPageLocators()

    def wait_for_stream_page_load(self) -> 'StreamerPage':
        try:
            accept_button = self.find_element(self.locators.CONTENT_CLASSIFICATION_ACCEPT_BUTTON)
            if accept_button.is_displayed():
                accept_button.click()
        except:
            pass

        self.wait_for_element_visible(self.locators.VIDEO_PLAYER)
        self.wait_for_element_visible(self.locators.FOLLOW_BUTTON)
            
        return self

    def take_screenshot(self, name: str = "streamer_page") -> str:
        return BrowserSetup.take_screenshot(self.driver, name)
