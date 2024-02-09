from the_internet.herokuInternet import HerokuApp
from fw import Examples


def test_element_delete_button(py, herokuapp):
    assert (herokuapp
            .navigate_to_heroku()
            .select_example(Examples.ADD_REMOVE)
            .click_example_button(Examples.ADD_ELEMENT_BUTTON)
            .store_example_button(Examples.DELETE_ELEMENT_BUTTON) == 1)


def test_element_delete_buttons(py, herokuapp):
    assert (herokuapp
            .navigate_to_heroku()
            .select_example(Examples.ADD_REMOVE)
            .click_example_button(Examples.ADD_ELEMENT_BUTTON)
            .click_example_button(Examples.ADD_ELEMENT_BUTTON)
            .store_example_button(Examples.DELETE_ELEMENT_BUTTON) == 2)


def test_dynamic_content(py, herokuapp):
    """
    Element in dynamic content contains text.
    :param
    herokuapp: Instance of HerokuApp
    py: Instance of Pylenium driver
    """
    assert (herokuapp
            .navigate_to_heroku()
            .select_example(Examples.DYNAMIC_CONTENT)
            .verify_dynamic_content()) > 1


def test_dropdown(py, herokuapp):
    """
    Element in dropdown is verified.
    :param py:
    :param herokuapp:
    """
    (herokuapp
     .navigate_to_heroku()
     .select_example(Examples.DROPDOWN)
     .click_dropdown(Examples.DROPDOWN_SELECT, 1))
