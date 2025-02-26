import random

from selenium.webdriver.common.by import By

class FormPageLocators:

    FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//*[@id="lastName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    GENDER = (By.XPATH, f'//div[@class="custom-control custom-radio custom-control-inline"]//label[@for="gender-radio-{random.randint(1,3)}"]')
    MOBILE = (By.XPATH, '//*[@id="userNumber"]')
    DATE_OF_BIRTH_INPUT = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    SUBJECTS_INPUT = (By.XPATH, '//*[@id="subjectsInput"]')
    HOBBIES = (By.XPATH, f'//div[@class="custom-control custom-checkbox custom-control-inline"]//label[@for="hobbies-checkbox-{random.randint(1,3)}"]')
    FILE_INPUT = (By.XPATH, '//*[@id="uploadPicture"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    SELECT_STATE = (By.XPATH, '//*[@id="state"]')
    STATE_INPUT = (By.XPATH, '//*[@id="react-select-3-input"]')
    SELECT_CITY = (By.XPATH, '//*[@id="city"]')
    CITY_INPUT = (By.XPATH, '//*[@id="react-select-4-input"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')

    #table results
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')

