import time

from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage, FramePage


class TestAlertsFrameWindow:

    class TestBrowserWindows:


        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "A new tab has not been opened or incorrect tab has been opened"

        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', "A new window has not been opened or incorrect window has been opened"


class TestAlertsPage:

    def test_see_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == 'You clicked a button', 'Alert did not show up'

    def test_see_alert_after_five_sec(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_alert_appear_after_five_sec()
        assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

    def test_check_confirm_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        alert_text = alert_page.check_confirm_alert()
        assert alert_text == 'You selected Ok', 'Alert did not show up'

    def test_check_prompt_alert(self, driver):
        alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()
        assert alert_text == f'You entered {text}'
        "both alerts check the same thing but in a different way"
        assert text in alert_text, 'Alert did not show up'


class TestFramesPage:

    def test_frames(self, driver):
        frame_page = FramePage(driver, 'https://demoqa.com/frames')
        frame_page.open()
        result_frame1 = frame_page.check_frame('frame1')
        result_frame2 = frame_page.check_frame('frame2')
        assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
        assert result_frame2 == ['This is a sample page', '100px', '100px'],  'The frame does not exist'
