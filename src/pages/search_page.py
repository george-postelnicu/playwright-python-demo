from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.result_hits = page.locator(".cmp-results-count")
        self.no_result_big_message = page.locator(".no-results__title")
        self.results = page.locator("section.cmp-searchresults__items__values")
        self.result_links = self.results.locator("//article")
