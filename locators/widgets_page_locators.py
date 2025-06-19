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

class SliderPageLocators:
    INPUT_SLIDER = (By.XPATH, '//*[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.XPATH, '//*[@id="sliderValue"]')

class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.XPATH, '//*[@id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.XPATH, '//*[@class="progress-bar bg-info"]')

class TabsPageLocators:
    TABS_WHAT = (By.XPATH, '//*[@id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.XPATH, '//*[@id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.XPATH, '//*[@id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.XPATH, '//*[@id="demo-tabpane-origin"]')
    TABS_USE = (By.XPATH, '//*[@id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.XPATH, '//*[@id="demo-tabpane-use"]')
    TABS_MORE = (By.XPATH, '//*[@id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.XPATH, '//*[@//*[@id="demo-tabpane-more"]]')

class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')

