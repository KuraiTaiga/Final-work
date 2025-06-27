import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.add_user_page import AddUserPage
import time
@pytest.mark.xfail
def test_add_user():
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)

    login_page = LoginPage(driver)
    add_user_page = AddUserPage(driver)

    try:
        # Шаг 1: Заходим на страницу логина и авторизация
        login_page.open()
        login_page.login("Autotest", "autoTest123!")
        time.sleep(0.5)       

        # Переход на страницу добавления пользователя
        add_user_page.open()

        # Заполняем форму пользователя и отправляем её
        add_user_page.fill_form(
            name="Анастасия",
            age=25,
            gender="1",
            date_birthday="08052025",
            is_active=True
        )
        
        time.sleep(0.5)

        add_user_page.submit()

        
        response_text = add_user_page.get_response_message()
        
        if response_text:
            print("Ответ сервера:", response_text)
        
    except Exception as e:
       print("Ошибка во время выполнения теста:", e)
       pytest.fail()
    finally:
       driver.quit()


