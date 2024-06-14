from selenium.webdriver.common.by import By


class CustomersPage:
    btn_add_new_xpath = "//a[normalize-space()='Add new']"

    # Add New Customer Info
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@name='FirstName']"
    txt_lastname_xpath = "//input[@name='LastName']"
    rd_male_gender_xpath = "//input[@id='Gender_Male']"
    rd_female_gender_xpath = "//input[@id='Gender_Female']"
    cln_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    chk_is_tax_exempt_xpath = "//input[@id='IsTaxExempt']"

    # Newsletter
    drp_newsletter_xpath = ("//label[text()='Newsletter']/parent::div/parent::"
                            "div/following-sibling::div//span[@role='combobox']")
    opt_newsletter1_xpath = "//option[contains(text(),'Your store name')]"
    opt_newsletter2_xpath = "//option[contains(text(),'Test store 2')]"

    # Customer role
    txt_customer_Roles_xpath = ("//label[text()='Customer roles']/parent::div/parent::"
                                "div/following-sibling::div//span[@role='combobox']")
    lst_item_Administrators_xpath = "//option[contains(text(),'Administrators')]"
    lst_item_Registered_xpath = "//option[contains(text(),'Registered')]"
    lst_item_Guests_xpath = "//option[contains(text(),'Guests')]"
    lst_item_Forum_Moderators_xpath = "//option[contains(text(),'Forum Moderators')]"
    lst_item_Vendors_xpath = "//option[contains(text(),'Vendors')]"

    # Vendor Dropdown
    drp_manger_vendor_xpath = "//select[@id='VendorId']"
    opt_item_vendornone_xpath = "//option[contains(text(),'Not a vendor')]"
    opt_item_vendor1_xpath = "//option[contains(text(),'Vendor 1')]"
    opt_item_vendor2_xpath = "//option[contains(text(),'Vendor 2')]"

    txt_comment_xpath = "//textarea[@name='AdminComment']"

    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_addnew(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rd_male_gender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rd_female_gender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_male_gender_xpath).click()

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, self.cln_dob_xpath).send_keys(dob)

    def set_companyname(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_company_name_xpath).send_keys(companyname)

    def set_newsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.drp_newsletter_xpath).click()
        click_expanded_nl = self.driver.find_element(By.XPATH, "//span[@aria-expanded='true']")
        if newsletter == 'Your store name':
            self.driver.find_element(By.XPATH, self.opt_newsletter1_xpath).click()
        elif newsletter == 'Test store 2':
            self.driver.find_element(By.XPATH, self.opt_newsletter2_xpath).click()
        if click_expanded_nl:
            self.driver.find_element(By.XPATH, self.drp_newsletter_xpath).click()
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click();", self.option)

    # def get_item_value(self):
    #     registered = self.driver.find_element(By.XPATH, "//li[contains(text(),'Registered')]").text

    def set_customer_role(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_Roles_xpath).click()
        registered = self.driver.find_element(By.XPATH, "//li[contains(text(),'Registered')]").text
        click_expanded_cr = self.driver.find_element(By.XPATH, "//span[@aria-expanded='true']")
        # click_expanded = self.driver.find_element(By.XPATH, "//span[@aria-expanded='true']")
        if role == 'Registered':
            if not registered:
                self.driver.find_element(By.XPATH, self.lst_item_Registered_xpath).click()
            else:
                pass
        elif role == 'Administrators':
            self.driver.find_element(By.XPATH, self.lst_item_Administrators_xpath).click()
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            self.driver.find_element(By.XPATH, "//li[@title='Registered']/span").click()
            self.driver.find_element(By.XPATH, self.lst_item_Guests_xpath).click()
        elif role == 'Vendors':
            self.driver.find_element(By.XPATH, self.lst_item_Vendors_xpath).click()
        elif role == 'Forum Moderators':
            self.driver.find_element(By.XPATH, self.lst_item_Forum_Moderators_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.lst_item_Registered_xpath).click()
        if click_expanded_cr:
            self.driver.find_element(By.XPATH, self.txt_customer_Roles_xpath).click()
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click()", self.list_item)

    def set_manage_vendors(self, vendors):
        self.driver.find_element(By.XPATH, self.drp_manger_vendor_xpath).click()
        if vendors == 'Not a vendor':
            self.driver.find_element(By.XPATH, self.opt_item_vendornone_xpath).click()
        elif vendors == 'Vendor 1':
            self.driver.find_element(By.XPATH, self.opt_item_vendor1_xpath).click()
        elif vendors == 'Vendor 2':
            self.driver.find_element(By.XPATH, self.opt_item_vendor2_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.opt_item_vendor1_xpath).click()
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click()", self.dropdown_item)

    def enter_comment(self):
        self.driver.find_element(By.XPATH, self.txt_comment_xpath).send_keys("Add New Customer from Automation.")

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
