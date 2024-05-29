import pytest
from Pages.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities.XLUtils import XLUtils


class Test_002_DDT_login:
    base_URL = ReadConfig.get_application_url()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.parametrize("username, password, expected", [
        # The XLUtils.get_data_from_excel method should be implemented to return data in the correct format
        *XLUtils.get_data_from_excel(path, 'Sheet1')])
    def test_login_ddt(self, setup, username, password, expected):
        self.logger.info("-------------Test_002_DDT_Login--------------------")
        self.logger.info("-------------Verifying Login Test DDT--------------")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()

        actual_dashboard_url = self.driver.current_url
        expected_dashboard = "https://admin-demo.nopcommerce.com/admin/"

        if actual_dashboard_url == expected_dashboard:
            if expected == "Pass":
                self.logger.info("-------------Login Test is Passed----------")
                self.driver.save_screenshot(".\\Screenshots\\" + f"test_login_{username}_Passed.png")
                self.driver.close()
                assert True
            else:
                self.logger.info("-------------Login Test is Failed----------")
                self.driver.save_screenshot(".\\Screenshots\\" + f"test_login_{username}_Failed.png")
                self.driver.close()
                assert False
        else:
            if expected == "Pass":
                self.logger.info("-------------Login Test is Failed----------")
                self.driver.save_screenshot(".\\Screenshots\\" + f"test_login_{username}_Failed.png")
                self.driver.close()
                assert False
            else:
                self.logger.info("-------------Login Test is Passed----------")
                self.driver.save_screenshot(".\\Screenshots\\" + f"test_login_{username}_Passed.png")
                self.driver.close()
                assert True

        self.logger.info("----- End of Login DDT Test -----")
        self.logger.info("----- Completed TC_002_DDT_Login -----")
