from app_tests.utilities.page_utils import PageUtils


class SearchWikipediaPage(PageUtils):

    search_container_class = "androidx.cardview.widget.CardView"
    search_bar_input_class = "android.widget.AutoCompleteTextView"
    searching_result_class = "android.widget.TextView"
