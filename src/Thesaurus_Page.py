from selenium.webdriver.common.by import By
from Base_Element import Base_Element
from Base_Page import Base_Page


class Thesaurus_Page(Base_Page):
    url = "https://www.thesaurus.com/"

    @property
    def search_button(self):
        return  Base_Element(
            self.driver, 
            by=By.XPATH,
            locator_val="//button[@id='search-submit']"
        )

    @property
    def search_input(self):
        return  Base_Element(
            self.driver, 
            by=By.XPATH,
            locator_val="//input[@title='Search']"
        )
