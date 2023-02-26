from web_tests.pages.wikipedia_main_page import WikipediaMainPage


class WikipediaMainActions(WikipediaMainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_wikipedia_web(self):
        self.open_web('https://www.wikipedia.org/')

    def check_wikipedia_web_title(self):
        title = self.check_text(self.wikipedia_title_xpath)
        return title

    def click_on_the_search_input(self):
        self.click_xpath(self.search_input_xpath)

    def write_in_the_search_input(self, text):
        self.write_xpath(self.search_input_xpath, text)

    def click_in_the_search_button(self):
        self.click_xpath(self.search_button_xpath)
