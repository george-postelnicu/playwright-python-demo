from enum import Enum

from playwright.sync_api import Page, expect


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
        self.top_nav = page.locator(".utilitybar")
        self.language = self.top_nav.locator(".languagenavigation")
        self.language_dropdown = self.language.locator("ul")
        self.search = self.top_nav.locator("section.cmp-search")

    def select_language(self, language: Language) -> None:
        self.language.click()
        expect(self.language).to_have_class('languagenavigation --open')
        link = self.language_dropdown.get_by_role('link', name=language.value)
        link.click()
