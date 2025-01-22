import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage

url = "https://demoqa.com/text-box"


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_test_box_page = TextBoxPage(driver, url)
            text_test_box_page.open()
            full_name, email, current_address, permanent_address = text_test_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_address = text_test_box_page.check_filled_form()
            time.sleep(15)
            updated_current_address = current_address.replace("\n", " ")
            updated_permanent_address = permanent_address.replace("\n", " ")
            assert full_name == output_name, "the Full name doesn't match"
            assert email == output_email, "the Email name doesn't match"
            assert updated_current_address == output_current_address, "the Current Address name doesn't match"
            assert updated_permanent_address == output_address, "the Permanent Address name doesn't match"
