def test_element_delete_button(py):
    py.visit("https://the-internet.herokuapp.com/")
    py.should().have_title("The Internet")
    py.get("a[href='/add_remove_elements/']").click()
    py.url().endswith("/add_remove_elements")
    py.get("button[onclick='addElement()']").click()
    delete_buttons = py.find("button[onclick='deleteElement()']")
    assert delete_buttons.length() == 1


def test_element_delete_buttons(py):
    py.visit("https://the-internet.herokuapp.com/")
    py.should().have_title("The Internet")
    py.get("a[href='/add_remove_elements/']").click()
    py.url().endswith("/add_remove_elements")
    add_element_button = py.get("button[onclick='addElement()']")
    add_element_button.click()
    add_element_button.click()
    delete_buttons = py.find("button[onclick='deleteElement()']")
    assert delete_buttons.length() == 2
