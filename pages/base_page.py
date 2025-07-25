from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/text-box"


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments [0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drug_and_drop_by_offset(self, element, x_coords, y_coords ):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()


    # def remove_footer(self):
    #     self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
    #     self.driver.execute_script("document.getElementsById('close-fixedban').remove();")




