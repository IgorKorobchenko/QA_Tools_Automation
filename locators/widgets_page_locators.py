from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, '//*[@id="section1Heading"]')
    CONTENT_FIRST = (By.XPATH, '//*[@id="section1Content"]')
    SECTION_SECOND = (By.XPATH, '//*[@id="section2Heading"]')
    CONTENT_SECOND= (By.XPATH, '//*[@id="section2Content"]')
    SECTION_THIRD = (By.XPATH, '//*[@id="section3Heading"]')
    CONTENT_THIRD = (By.XPATH, '//*[@id="section3Content"]')

class AutoCompletePageLocators:
    MULTI_INPUT = (By.XPATH, '//*[@id= "autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.XPATH, '//*[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.XPATH, '//*[@class="css-xb97g8 auto-complete__multi-value__remove"]')
    SINGLE_VALUE = (By.XPATH, '//*[@class= "auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.XPATH, '//*[@id= "autoCompleteSingleInput"]')

class DatePickerPageLocators:
    DATE_INPUT = (By.XPATH, '//*[@id= "datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.XPATH, '//*[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.XPATH, '//*[@class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.XPATH, '//*[@id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')