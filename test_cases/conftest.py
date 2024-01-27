import pytest
from selenium import webdriver
import configparser


@pytest.fixture(autouse=True)
def driver():
    s = webdriver.ChromeService(executable_path=r"C:\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture(autouse=True)
def config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    yield config