import pytest
from Pages.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils_SDET


class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils_SDET.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils_SDET.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils_SDET.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils_SDET.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
