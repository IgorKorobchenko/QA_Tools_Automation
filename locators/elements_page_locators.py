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


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, '//*[@id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="userEmail"]')
    # AGE_INPUT = (By.XPATH, '//*[@id="age"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.XPATH, '//*[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH, '//*[@id="department"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')

    # tables
    FULL_PEOPLE_LIST = (By.XPATH, "//*[@class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    # UPDATE_BUTTON = (By.XPATH, '//span[@id="edit-record-1"]')
