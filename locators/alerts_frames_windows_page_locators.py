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

class FramePageLocators:
    FIRST_FRAME = (By.XPATH, '//*[@id="frame1"]')
    SECOND_FRAME = (By.XPATH, '//*[@id="frame2"]')
    TITLE_FRAME = (By.XPATH, '//*[@id="sampleHeading"]')

class NestedFramePageLocators:
    PARENT_FRAME = (By.XPATH, '//*[@id="frame1"]')
    PARENT_TEXT = (By.XPATH, '//*[text()="Parent frame"]')
    CHILD_FRAME = (By.XPATH, '//*[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.XPATH, '//*[text()="Child Iframe"]')

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.XPATH, '//*[@id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.XPATH, '//*[@id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.XPATH, '//*[@class="modal-body"]')
    TITLE_SMALL_MODAL = (By.XPATH, '//*[text()="Small modal"]')

    LARGE_MODAL_BUTTON = (By.XPATH, '//*[@id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BUTTON = (By.XPATH, '//*[@id="closeLargeModal"]')
    BODY_LARGE_MODAL = (By.XPATH, '//*[@class="modal-body"]')
    TITLE_LARGE_MODAL = (By.XPATH, '//*[text()="Large Modal"]')