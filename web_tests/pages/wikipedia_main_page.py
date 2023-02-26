from web_tests.utilities.web_page_utils import WebPageUtils


class WikipediaMainPage(WebPageUtils):

    wikipedia_title_xpath = "// *[ @ id ='www-wikipedia-org'] / div[1] / h1 / span"
    search_input_xpath = "//*[@id='searchInput']"
    suggestion_dropdown_xpath = "//*[@id='typeahead-suggestions']/div"
    search_button_xpath = "//*[@id='search-form']/fieldset/button"
