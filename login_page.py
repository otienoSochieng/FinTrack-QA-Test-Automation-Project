from selenium.webdriver.common.by import By

class LoginPage:
    URL = "/login"
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    PROFILE = (By.ID, "profile")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.URL)

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def is_logged_in(self):
        return len(self.driver.find_elements(*self.PROFILE)) > 0
