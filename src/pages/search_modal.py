from playwright.sync_api import Page

from src.pages.search_page import SearchPage


class SearchModal:
    def __init__(self, page: Page):
        self.page = page
        self.modal = page.locator("#search-modal")
        self.__text = self.modal.locator("//input")
        self.__close = self.modal.locator("//button[contains(@class, 'close')]")
        self.__search = self.modal.locator("//button[@type='submit']")

    def search(self, text: str) -> SearchPage:
        self.__text.fill(text)
        self.__search.click()
        return SearchPage(self.page)

    def close(self) -> None:
        self.__close.click()
