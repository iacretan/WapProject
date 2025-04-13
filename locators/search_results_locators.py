from selenium.webdriver.common.by import By

class SearchResultsLocators:
    CHANNELS_SECTION = (By.XPATH, "//h2[contains(text(), 'CHANNELS')]")
    STREAMER_ITEM = (By.XPATH, "(//section[contains(@class, 'Layout')])[1]/div[3]/button") #Select the third stream by position
    VIDEO_PLAYER = (By.XPATH, "//div[@data-a-target='player-overlay-click-handler']")
    FOLLOW_BUTTON = (By.XPATH, "//div[contains(text(), 'Follow')]")
    CONTENT_CLASSIFICATION_ACCEPT_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")
