from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://158.160.87.146:5000/add-user"
        # локаторы элементов формы
        self.name_input = (By.NAME, "name")
        self.age_input = (By.ID, "age")
        self.gender_input = (By.ID, "gender")
        self.date_birthday_input = (By.ID, "date_birthday")
        self.is_active_checkbox = (By.ID, "isActive")
        self.submit_button = (By.ID, "add-btn")
        self.message_container = (By.ID, "messageContainer")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, name, age, gender, date_birthday, is_active=True):
        # Заполнение имени
        name_el = self.driver.find_element(*self.name_input)
        name_el.clear()
        name_el.send_keys(name)

        # Заполнение возраста
        age_el = self.driver.find_element(*self.age_input)
        age_el.clear()
        age_el.send_keys(str(age))

        # Заполнение пола
        gender_el = self.driver.find_element(*self.gender_input)
        gender_el.clear()
        gender_el.send_keys(gender)

        # Заполнение даты рождения
        date_el = self.driver.find_element(*self.date_birthday_input)
        date_el.clear()
        date_el.send_keys(date_birthday)

        # Установка чекбокса isActive
        checkbox = self.driver.find_element(*self.is_active_checkbox)
        if is_active != checkbox.is_selected():
            checkbox.click()

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_response_message(self):
        messages = {}
        found_any = False  # флаг, указывающий, был ли найден хотя бы один элемент

        try:
            message_element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.ID, "messageContainer"))
            )
            messages['messageContainer'] = message_element.text
            found_any = True
        except:
            messages['messageContainer'] = None

        try:
            name_error_element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.ID, "nameError"))
            )
            messages['nameError'] = name_error_element.text
            found_any = True
        except:
            messages['nameError'] = None

        try:
            age_error_element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.ID, "ageError"))
            )
            messages['ageError'] = age_error_element.text
            found_any = True
        except:
            messages['ageError'] = None

        # Если ни один элемент не был найден - возвращаем None
        if not found_any:
            return None

        return messages