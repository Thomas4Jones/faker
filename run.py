from test import *


@pytest.mark.smoke
def test_username_press(page: Page, username_press):
    username_press()


@pytest.mark.smoke
def test_textarea(page: Page, textarea):
    textarea()


@pytest.mark.smoke
def test_set_filename(page: Page, set_filename):
    set_filename()


@pytest.mark.smoke
def test_checkbox_items(page: Page, checkbox_items):
    checkbox_items()


@pytest.mark.smoke
def test_radio_items(page: Page, radio_items):
    radio_items()


@pytest.mark.smoke
def test_multipleselect(page: Page, multipleselect):
    multipleselect()


@pytest.mark.smoke
def test_dropdown(page: Page, dropdown_items):
    dropdown_items()


@pytest.mark.smoke
def test_buttoncancel(page: Page, buttoncancel):
    buttoncancel()


@pytest.mark.smoke
def test_buttonsubmit(page: Page, buttonsubmit):
    buttonsubmit()
