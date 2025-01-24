from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # FORM FIELDS
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//*[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//*[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//*[@id='submit']")
    # CREATED FORM
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BTN = (By.XPATH, "//button[@aria-label='Expand all']")
    COLLAPSE_ALL_BTN = (By.XPATH, "//button[@aria-label='Collapse all']")
    ITEM_LIST = (By.XPATH, "//span[@class='rct-checkbox']")
    CHECKED_ITEMS = (By.XPATH, "//*[@class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_BUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_BUTTON = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//*[@class="text-success"]')
