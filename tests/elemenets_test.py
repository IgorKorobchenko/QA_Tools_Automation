import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_test_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
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


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, 'Checkboxes have not been selected'


class TestRadioButtons:
    def test_radio_buttons(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.click_on_radio_buttons('Yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_radio_buttons('Impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_radio_buttons('No')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', "'Yes' has not been selected"
        assert output_impressive == 'Impressive', "'Impressive' has not been selected"
        assert output_no == 'No', "'No' has not been selected"


