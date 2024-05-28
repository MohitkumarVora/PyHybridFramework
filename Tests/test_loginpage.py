from Pages.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig


class Test_001_login:
    base_URL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    dashboard = "https://admin-demo.nopcommerce.com/admin/"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title_failed.png")
            assert False
        self.driver.close()

    def test_login_positive(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_dashboard_url = self.driver.current_url
        if actual_dashboard_url == self.dashboard:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_positive_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_positive_failed.png")
            assert False
