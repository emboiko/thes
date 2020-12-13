from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_Element:
    def __init__(self, driver, by, locator_val):
        self.driver = driver
        self.by = by
        self.locator_val = locator_val
        self.locator = (self.by, self.locator_val)
        self.web_element = None
        self.find()


    def find(self):
        self.web_element = WebDriverWait(
            self.driver, 10, .25
        ).until(EC.visibility_of_element_located(locator=self.locator))


    def input_text(self, text):
        self.web_element.send_keys(text)


    def click(self):
        WebDriverWait(
            self.driver, 10, .25
        ).until(EC.element_to_be_clickable(locator=self.locator))
        self.web_element.click()


    @property
    def attribute(self, attr):
        return self.web_element.get_attribute(attr)


    @property
    def text(self):
        return self.web_element.text
