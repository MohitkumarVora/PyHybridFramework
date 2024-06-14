import time

from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
from Pages.CustomersPage import CustomersPage
from Utilities.readProperties import ReadConfig
from Utilities.random_generator import random_email_generator
import datetime


class Test_addCustomer:
    base_URL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    dashboard = "https://admin-demo.nopcommerce.com/admin/"

    def test_addcustomer_click(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.db = DashboardPage(self.driver)
        self.db.click_customers_menu()
        self.db.click_customers_customers_item()

        self.add_customer = CustomersPage(self.driver)
        self.add_customer.click_addnew()
        self.add_customer.set_email(random_email_generator())
        time.sleep(5)
        self.add_customer.set_password("Test@123")
        self.add_customer.set_firstname("Test")
        self.add_customer.set_lastname("Customer")
        self.add_customer.set_gender("Female")

        # Get the current date - 10 years ago date
        date_of_birth = datetime.datetime.now() - datetime.timedelta(days=365*10)
        date_of_birth = date_of_birth.strftime("%dd/%mm/%YYYY")

        self.add_customer.set_dob(date_of_birth)
        self.add_customer.set_companyname("Test Company")
        self.add_customer.set_newsletter("Test store 2")
        self.add_customer.set_customer_role("Administrators")
        self.add_customer.set_manage_vendors("Vendor 1")
        self.add_customer.enter_comment()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_passed.png")
        self.driver.close()
