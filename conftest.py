import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def base_url():
    return 'https://staging.fintrack.example'

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
