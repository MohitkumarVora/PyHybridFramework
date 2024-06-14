from selenium.webdriver.common.by import By


class DashboardPage:
    link_dashboard_xpath = "//a/p[normalize-space()='Dashboard']"

    # category list and it's options
    link_category_xpath = "//a/p[normalize-space()='Catalog']"
    link_category_products_xpath = "//a/p[normalize-space()='Products']"
    link_category_categories_xpath = "//a/p[normalize-space()='Categories']"
    link_category_manufacturers_xpath = "//a/p[normalize-space()='Manufacturers']"
    link_category_product_reviews_xpath = "//a/p[normalize-space()='Product reviews']"
    link_category_product_tags_xpath = "//a/p[normalize-space()='Product tags']"

    # category attributes and it's options
    link_category_attributes_xpath = "//a/p[normalize-space()='Attributes']"
    link_category_attributes_product_attributes_xpath = "//a/p[normalize-space()='Product attributes']"
    link_category_attributes_specification_attributes_xpath = "//a/p[normalize-space()='Specification attributes']"
    link_category_attributes_checkout_attributes_xpath = "//a/p[normalize-space()='Checkout attributes']"

    # sales and it's options
    link_sales_xpath = "//a/p[normalize-space()='Sales']"
    link_sales_orders_xpath = "//a/p[contains(text(),'Orders')]"
    link_sales_shipments_xpath = "//a/p[normalize-space()='Shipments']"
    link_sales_return_requests_xpath = "//a/p[normalize-space()='Return requests']"
    link_sales_recurring_payments_xpath = "//a/p[normalize-space()='Recurring payments']"
    link_sales_gift_cards_xpath = "//a/p[normalize-space()='Gift cards']"
    link_sales_shopping_carts_and_wishlists_xpath = "//a/p[normalize-space()='Shopping carts and wishlists']"

    # customers and it's options
    link_customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_customers_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_customers_customer_roles_xpath = "//a/p[normalize-space()='Customer roles']"
    link_customers_online_customers_xpath = "//a/p[normalize-space()='Online customers']"
    link_customers_vendors_xpath = "//a/p[normalize-space()='Vendors']"
    link_customers_activity_log_xpath = "//a/p[normalize-space()='Activity log']"
    link_customers_activity_types_xpath = "//a/p[normalize-space()='Activity Types']"
    link_customers_gdpr_request_log_xpath = "//a/p[normalize-space()='GDPR requests (log)']"

    # promotions and it's options
    link_promotions_xpath = "//a/p[normalize-space()='Promotions']"
    link_promotions_discounts_xpath = "//a/p[normalize-space()='Discounts']"
    link_promotions_affiliates_xpath = "//a/p[normalize-space()='Affiliates']"
    link_promotions_Newsletter_subscribers_xpath = "//a/p[normalize-space()='Newsletter subscribers']"
    link_promotions_campaigns_xpath = "//a/p[normalize-space()='Campaigns']"

    # content management and it's options
    link_content_management_xpath = "//a/p[normalize-space()='Content management']"
    link_content_management_topics_pages_xpath = "//a/p[normalize-space()='Topics (pages)']"
    link_content_management_message_templates_xpath = "//a/p[normalize-space()='Message templates']"
    link_content_management_news_items_xpath = "//a/p[normalize-space()='News items']"
    link_content_management_news_comments_xpath = "//a/p[normalize-space()='News comments']"
    link_content_management_blog_posts_xpath = "//a/p[normalize-space()='Blog posts']"
    link_content_management_blog_comments_xpath = "//a/p[normalize-space()='Blog comments']"
    link_content_management_polls_xpath = "//a/p[normalize-space()='Polls']"
    link_content_management_forums_xpath = "//a/p[normalize-space()='Forums']"

    # Initialize the Constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators Actions methods
    # ************* Category Module Actions *************
    def click_category_menu(self):
        self.driver.find_element(By.XPATH, self.link_category_xpath).click()

    def click_category_products_item(self):
        self.driver.find_element(By.XPATH, self.link_category_products_xpath).click()

    def click_category_categories_item(self):
        self.driver.find_element(By.XPATH, self.link_category_categories_xpath).click()

    def click_category_manufacturers_item(self):
        self.driver.find_element(By.XPATH, self.link_category_manufacturers_xpath).click()

    def click_category_product_reviews_item(self):
        self.driver.find_element(By.XPATH, self.link_category_product_reviews_xpath).click()

    def click_category_product_tags_item(self):
        self.driver.find_element(By.XPATH, self.link_category_product_tags_xpath).click()

    def click_category_attributes_item(self):
        self.driver.find_element(By.XPATH, self.link_category_attributes_xpath).click()

    def click_category_attributes_product_attributes_item(self):
        self.driver.find_element(By.XPATH, self.link_category_attributes_product_attributes_xpath).click()

    def click_category_attributes_specification_attributes_item(self):
        self.driver.find_element(By.XPATH, self.link_category_attributes_specification_attributes_xpath).click()

    def click_category_attributes_checkout_attributes_item(self):
        self.driver.find_element(By.XPATH, self.link_category_attributes_checkout_attributes_xpath).click()

    # ************* Sales Module Actions *************
    def click_sales_menu(self):
        self.driver.find_element(By.XPATH, self.link_sales_xpath).click()

    def click_sales_orders_item(self):
        self.driver.find_element(By.XPATH, self.link_sales_orders_xpath).click()

    def click_sales_shipments_item(self):
        self.driver.find_element(By.XPATH, self.link_sales_shipments_xpath).click()

    def click_sales_return_requests_item(self):
        self.driver.find_element(By.XPATH, self.link_sales_return_requests_xpath).click()

    def click_sales_recurring_payments_item(self):
        self.driver.find_element(By.XPATH, self.link_sales_recurring_payments_xpath).click()

    def click_sales_gift_cards_item(self):
        self.driver.find_element(By.XPATH, self.link_sales_gift_cards_xpath).click()

    def click_sales_shopping_carts_and_wishlists_item(self):
        self.driver.find_element(By.XPATH, self.link_sales_shopping_carts_and_wishlists_xpath).click()

    # ************* Customers Module Actions *************
    def click_customers_menu(self):
        self.driver.find_element(By.XPATH, self.link_customers_xpath).click()

    def click_customers_customers_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_customers_xpath).click()

    def click_customers_roles_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_customer_roles_xpath).click()

    def click_customers_online_customers_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_online_customers_xpath).click()

    def click_customers_vendors_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_vendors_xpath).click()

    def click_customers_activity_log_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_activity_log_xpath).click()

    def click_customers_activity_types_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_activity_types_xpath).click()

    def click_customers_gdpr_request_log_item(self):
        self.driver.find_element(By.XPATH, self.link_customers_gdpr_request_log_xpath).click()

    # ************* Promotions Module Actions *************
    def click_promotions_menu(self):
        self.driver.find_element(By.XPATH, self.link_promotions_xpath).click()

    def click_promotions_discounts_item(self):
        self.driver.find_element(By.XPATH, self.link_promotions_discounts_xpath).click()

    def click_promotions_affiliates_item(self):
        self.driver.find_element(By.XPATH, self.link_promotions_affiliates_xpath).click()

    def click_promotions_newsletter_subscribers_item(self):
        self.driver.find_element(By.XPATH, self.link_promotions_Newsletter_subscribers_xpath).click()

    def click_promotions_campaigns_item(self):
        self.driver.find_element(By.XPATH, self.link_promotions_campaigns_xpath).click()

    # ************* Content Management Module Actions *************
    def click_content_management_menu(self):
        self.driver.find_element(By.XPATH, self.link_content_management_xpath).click()

    def click_content_management_topic_item(self):
        self.driver.find_element(By.XPATH, self.link_content_management_xpath).click()
