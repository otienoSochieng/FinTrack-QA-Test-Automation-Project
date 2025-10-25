from automation.pages.login_page import LoginPage

def test_valid_login(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open()
    login.login('testuser@example.com', 'Password123')
    assert login.is_logged_in()
