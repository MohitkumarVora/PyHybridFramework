from Pages.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import setup_logger


class Test_001_login:
    base_URL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    dashboard = "https://admin-demo.nopcommerce.com/admin/"
    logger = setup_logger()

    def test_home_page_title(self, setup):

        self.logger.info("-------------Test_001_Login---------------------")
        self.logger.info("-------------Verifying Home Page Title----------")
        self.driver = setup
        self.driver.get(self.base_URL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title_passed.png")
            assert True
            self.logger.info("-------------Home Page Title test is Passed-------------")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title_failed.png")
            self.logger.info("-------------Home Page Title test is Failed-------------")
            assert False
        self.driver.close()

    def test_login_positive(self, setup):

        self.logger.info("-------------Verifying Login Test--------------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_dashboard_url = self.driver.current_url
        if actual_dashboard_url == self.dashboard:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_positive_passed.png")
            assert True
            self.logger.info("-------------Login Test is Passed----------")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_positive_failed.png")
            self.logger.info("-------------Login Test is Passed----------")
            assert False
        self.driver.close()
