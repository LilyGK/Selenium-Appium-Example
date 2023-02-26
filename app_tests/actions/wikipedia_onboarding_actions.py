from app_tests.pages.wikipedia_onboarding_page import WikipediaOnboardingPage


class WikipediaOnboardingActions(WikipediaOnboardingPage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_though_onboarding(self):
        self.click_class_index(self.continue_button_id, 1)
        self.click_class_index(self.continue_button_id, 1)
        self.click_class_index(self.continue_button_id, 1)
        self.click_class_index(self.continue_button_id, 1)
