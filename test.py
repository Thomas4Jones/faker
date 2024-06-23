import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from BasicHtmlFormTest.data.data import *
from locator import *


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def username_press(page: Page):
    def username_press_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.locator(locator_username).fill(data_username)
        page.locator(locator_password).fill(data_password)
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/username.png')
    return username_press_func


@pytest.fixture
def textarea(page: Page):
    def textarea_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        def key_textarea(locator_textarea: str, data_textarea: str):
            page.click(locator_textarea)
            page.keyboard.down("Shift")
            for _ in range(8):
                page.keyboard.press("ArrowLeft")
            page.keyboard.up("Shift")
            page.keyboard.type(data_textarea)
        key_textarea(locator_textarea, data_textarea)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/textarea.png')
        page.click(locator_submit)
        page.screenshot(path='screen/textarea2.png')
    return textarea_func


@pytest.fixture
def set_filename(page: Page):
    def set_filename_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', data_filename_path_2)
        page.wait_for_timeout(2000)
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        set_filename = page.locator(locator_filename_2).inner_text()
        page.wait_for_timeout(2000)
        assert set_filename == 'filename.txt'
        page.screenshot(path="screen/set_filename2.png")
        page.wait_for_timeout(2000)
    return set_filename_func


@pytest.fixture()
def checkbox_items(page: Page):
    def checkbox_items_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_checkbox1)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/checkbox1.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 300)
        page.screenshot(path='screen/checkbox1.1.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
        page.click(locator_checkbox2)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/checkbox2.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 500)
        page.screenshot(path='screen/checkbox2.1.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
    return checkbox_items_func


@pytest.fixture()
def radio_items(page: Page):
    def radio_items_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_radio1)
        page.mouse.wheel(0, 500)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/radio1.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 300)
        page.screenshot(path='screen/radio1.2.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
        page.click(locator_radio3)
        page.mouse.wheel(0, 500)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/radio3.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 300)
        page.screenshot(path='screen/radio3.2.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
    return radio_items_func


@pytest.fixture()
def multipleselect(page: Page):
    def multipleselect_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.select_option(locator_multiple_select_values, data_multipleselect_1)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/multipleselect_1.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 500)
        page.screenshot(path='screen/multipleselect_1.2.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
        page.wait_for_timeout(1000)
        page.select_option(locator_multiple_select_values, data_multipleselect_4)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/multipleselect_4.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.screenshot(path='screen/multipleselect_4.2.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
    return multipleselect_func


@pytest.fixture()
def dropdown_items(page: Page):
    def dropdown_items_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)
        page.select_option(locator_dropdown, data_dropdown_item_1)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/dropdown_1.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 500)
        page.screenshot(path='screen/dropdown_1.2.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)
        page.select_option(locator_dropdown, data_dropdown_item_6)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/dropdown_6.png')
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.screenshot(path='screen/dropdown_6.2.png')
        page.wait_for_timeout(1000)
        page.click(locator_gobacktotheform)
    return dropdown_items_func


@pytest.fixture()
def buttoncancel(page: Page):
    def buttoncancel_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.locator(locator_username).fill(data_username)
        page.locator(locator_password).fill(data_password)  # ввели имя и пароль
        page.wait_for_timeout(1000)
        page.click(locator_cancel)  # отменяем действие
        page.wait_for_timeout(1000)
        page.click(locator_submit)  # проверяем отмену действия
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/after_press_cancel.png')  # делаем скрин, что действие отменено
    return buttoncancel_func


@pytest.fixture()
def buttonsubmit(page: Page):
    def buttonsubmit_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(3000)
        page.screenshot(path='screen/after_press_submit.png')
        assert "https://testpages.eviltester.com/styled/the_form_processor.php" in page.url.lower()
        page.click(locator_gobacktotheform)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(3000)
        assert "https://testpages.eviltester.com/styled/basic-html-form-test.html" in page.url.lower()
        page.screenshot(path='screen/after_press_gobacktotheform.png')
        page.wait_for_timeout(1000)
    return buttonsubmit_func
