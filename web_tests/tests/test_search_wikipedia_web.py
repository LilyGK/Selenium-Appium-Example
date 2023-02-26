from web_tests.tests.base_test import BaseTest
from web_tests.actions.wikipedia_main_actions import WikipediaMainActions
from web_tests.actions.voyager_1_wiki_actions import Voyager1WikiActions


class TestWikipediaSearching(BaseTest):

    def test_open_wikipedia(self):
        start = WikipediaMainActions(self.driver)
        start.open_wikipedia_web()
        expected_title = "Wikipedia"
        actual_tittle = start.check_wikipedia_web_title()
        assert actual_tittle == expected_title
        self.lambda_report(actual_tittle, expected_title)

    def test_search_voyager(self):
        search = WikipediaMainActions(self.driver)
        search.click_on_the_search_input()
        search.write_in_the_search_input("voyager 1")
        search.click_in_the_search_button()
        voyager = Voyager1WikiActions(self.driver)
        expected_page_header = "Voyager 1"
        actual_page_header = voyager.check_voyager_page()
        assert actual_page_header == expected_page_header
        self.lambda_report(actual_page_header, expected_page_header)




























