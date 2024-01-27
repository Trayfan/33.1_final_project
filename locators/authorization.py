from selenium.webdriver.common.by import By

class AuthorizationPage:
    def __init__(self, driver) -> None:
        self.email_btn = driver.find_element(By.ID, 't-btn-tab-mail')
        self.username = driver.find_element(By.ID, 'username')
        self.password = driver.find_element(By.ID, 'password')
        self.login_btn = driver.find_element(By.ID, 'kc-login')
        self.phone_btn = driver.find_element(By.ID, 't-btn-tab-phone')