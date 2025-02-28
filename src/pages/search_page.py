from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_pill = page.locator(".kesearch_searchbox")
        self.search_input = self.search_pill.get_by_placeholder("Your search phrase")
        self.result_hits = page.locator("#kesearch_num_results")
        self.results = page.locator("#kesearch_results")
        self.result_links = self.results.locator("//a")
