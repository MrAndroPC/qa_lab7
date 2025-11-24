import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.device_name = 'emulator-5554'
options.app = r'c:\Users\sared\AndroidStudioProjects\QA_Lab\app\build\intermediates\apk\debug\app-debug.apk' 
options.app_package = 'com.example.qa_lab'
options.app_activity = '.MainActivity'
options.no_reset = False

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_add_note(driver):
    note_text = "Hello Appium!"

    input_field = driver.find_element(AppiumBy.ID, "com.example.qa_lab:id/noteInput")
    input_field.send_keys(note_text)

    add_btn = driver.find_element(AppiumBy.ID, "com.example.qa_lab:id/addBtn")
    add_btn.click()

    # Небольшая пауза для анимации
    time.sleep(1)
    
    added_note = driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{note_text}']")
    
    assert added_note.is_displayed(), "Заметка не отображается в списке"

def test_delete_note_gesture(driver):
    input_field = driver.find_element(AppiumBy.ID, "com.example.qa_lab:id/noteInput")
    input_field.send_keys("Delete Me")
    driver.find_element(AppiumBy.ID, "com.example.qa_lab:id/addBtn").click()
    
    note_to_delete = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Delete Me']")
    
    from selenium.webdriver.common.action_chains import ActionChains
    actions = ActionChains(driver)
    actions.click_and_hold(note_to_delete).pause(2).release().perform()

    notes = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Delete Me']")
    assert len(notes) == 0, "Заметка не была удалена после долгого нажатия"

