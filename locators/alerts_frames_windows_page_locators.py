from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH, '//*[@id="tabButton"]')
    TITLE_NEW = (By.XPATH, '//*[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//*[@id="windowButton"]')

class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.XPATH, '//*[@id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.XPATH, '//*[@id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.XPATH, '//*[@id="confirmButton"]')
    PROMPT_BOX_ALERT_BUTTON = (By.XPATH, '//*[@id="promtButton"]')
    CONFIRM_RESULT = (By.XPATH, '//*[@id="confirmResult"]')
    PROMPT_RESULT = (By.XPATH, '//*[@id="promptResult"]')