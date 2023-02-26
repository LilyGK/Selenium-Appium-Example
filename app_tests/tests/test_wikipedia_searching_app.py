from app_tests.actions.wikipedia_onboarding_actions import WikipediaOnboardingActions
from app_tests.actions.search_wikipedia_actions import SearchWikipediaActions
from app_tests.tests.base_test import BaseTest


class TestWikipediaSearching(BaseTest):

    def test_go_though_onboarding(self):
        start = WikipediaOnboardingActions(self.driver)
        start.go_though_onboarding()

    def test_search_in_wikipedia(self):
        search = SearchWikipediaActions(self.driver)
        search.click_on_search_container()
        search.type_on_search_container("voyager 1")
        search.select_on_search_results(1)
