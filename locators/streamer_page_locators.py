from selenium.webdriver.common.by import By

class StreamerPageLocators:
    VIDEO_PLAYER = (By.XPATH, "//div[@data-a-target='player-overlay-click-handler']")
    FOLLOW_BUTTON = (By.XPATH, "//div[contains(text(), 'Follow')]")
    CONTENT_CLASSIFICATION_ACCEPT_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")
