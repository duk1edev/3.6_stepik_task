import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_button_move_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_element_by_class_name("btn-add-to-basket") is not None, 'Должна быть кнопка'

