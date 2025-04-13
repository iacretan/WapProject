from selenium.webdriver.common.by import By

class HomeLocators:
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[@data-a-target='consent-banner-accept']")
    BROWSER_OPTION = (By.XPATH, "//div[text()='Browse']")
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Search']")
    SEARCH_BUTTON_ICON = (By.XPATH, '//button[@aria-label="Search Button"]')
    CHANNELS_SECTION = (By.XPATH, "//h2[contains(text(), 'CHANNELS')]")
