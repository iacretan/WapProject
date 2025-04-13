from pages.base_page import BasePage
from locators.search_results_locators import SearchResultsLocators
from selenium.webdriver.remote.webdriver import WebDriver

class SearchResultsPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locators = SearchResultsLocators()

    def wait_for_results(self) -> 'SearchResultsPage':
        self.wait_for_element_visible(self.locators.CHANNELS_SECTION)
        return self

    def scroll_down_times(self, times: int = 1) -> 'SearchResultsPage':
        for _ in range(times):
            self.scroll_down()
        return self
        
    def select_streamer(self) -> 'SearchResultsPage':
        self.wait_for_element_visible(self.locators.CHANNELS_SECTION)
        self.scroll_to_element(self.locators.STREAMER_ITEM)
        self.js_click(self.locators.STREAMER_ITEM)
        
        try:
            accept_button = self.find_element(self.locators.CONTENT_CLASSIFICATION_ACCEPT_BUTTON)
            if accept_button.is_displayed():
                accept_button.click()
        except:
            pass

        self.wait_for_element_visible(self.locators.VIDEO_PLAYER)
        self.wait_for_element_visible(self.locators.FOLLOW_BUTTON)
            
        return self
