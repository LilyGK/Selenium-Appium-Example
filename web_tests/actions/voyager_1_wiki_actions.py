from web_tests.pages.voyager_1_wiki_page import Voyager1WikiPage


class Voyager1WikiActions(Voyager1WikiPage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_voyager_page(self):
        header = self.check_text(self.voyager_1_header_xpath)
        return header

