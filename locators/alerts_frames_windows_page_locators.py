from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH, '//*[@id="tabButton"]')
    TITLE_NEW = (By.XPATH, '//*[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//*[@id="windowButton"]')
