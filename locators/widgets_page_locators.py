from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, '//*[@id="section1Heading"]')
    CONTENT_FIRST = (By.XPATH, '//*[@id="section1Content"]')
    SECTION_SECOND = (By.XPATH, '//*[@id="section2Heading"]')
    CONTENT_SECOND= (By.XPATH, '//*[@id="section2Content"]')
    SECTION_THIRD = (By.XPATH, '//*[@id="section3Heading"]')
    CONTENT_THIRD = (By.XPATH, '//*[@id="section3Content"]')