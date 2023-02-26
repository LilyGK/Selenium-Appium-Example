from app_tests.pages.search_wikipedia_page import SearchWikipediaPage


class SearchWikipediaActions(SearchWikipediaPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_search_container(self):
        self.click_class_index(self.search_container_class, 0)
        self.click_class_index(self.search_bar_input_class, 0)

    def type_on_search_container(self, text):
        self.write_class_index(self.search_bar_input_class, text, 0)

    def select_on_search_results(self, index):
        self.click_class_index(self.searching_result_class, index)
