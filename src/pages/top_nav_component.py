from enum import Enum

from playwright.sync_api import Page

from src.pages.search_modal import SearchModal


class Language(Enum):
    EN = "English"
    DE = "Deutsch"
    ES = "Español"
    FR = "Français"
    IT = "Italiano"
    NL = "Nederlands"


class TopNavComponent:
    def __init__(self, page: Page):
        self.page = page
        self.top_nav = page.locator("//div[@class='lnet-top-menu']")
        self.language = self.top_nav.locator("//*[contains(@class, 'language-switcher-button')]")
        self.language_dropdown = self.top_nav.locator("//*[contains(@class, 'region-switcher-list')]")
        self.search = self.top_nav.locator("//button[contains(@class, 'btn btn--search')]")

    def select_language(self, language: Language) -> None:
        self.language.click()
        # link = self.language_dropdown.locator(f"//a[contains(text(), '{language.value}')]")
        link = self.language_dropdown.get_by_role('link', name=language.value)
        link.click()

    def search_for(self) -> SearchModal:
        self.search.click()
        return SearchModal(self.page)
