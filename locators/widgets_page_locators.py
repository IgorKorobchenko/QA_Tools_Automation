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