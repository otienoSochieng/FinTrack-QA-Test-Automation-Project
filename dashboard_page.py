from selenium.webdriver.common.by import By

class DashboardPage:
    BALANCE = (By.ID, "balance")
    ADD_EXPENSE = (By.ID, "add-expense-btn")

    def __init__(self, driver):
        self.driver = driver

    def get_balance(self):
        return self.driver.find_element(*self.BALANCE).text

    def click_add_expense(self):
        self.driver.find_element(*self.ADD_EXPENSE).click()
