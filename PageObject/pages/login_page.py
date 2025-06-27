from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://158.160.87.146:5000/login"
        self.login_input = (By.NAME, "login")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.ID, "add-btn")  

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.login_input).clear()
        self.driver.find_element(*self.login_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        