import pytest
from time import sleep

@pytest.fixture
def open_recovery_page(driver, config):
    driver.get(config["url"]["page_recovery_url"])

def test_password_recovery_correct_phone(open_recovery_page):
    sleep(1000)
    # 0) Открыть ссылку восстановления пароля
    # 1) Нажать на "Забыл пароль"
    # 2) Выбрать вкладку телефон
    # 3) Ввести зарегестрированный телефон
    # 4) Нажать продолжить
    # 5) Ввести в поле ввода получиный код
    # 6) Ввести новый пароль, нажать сохранить
