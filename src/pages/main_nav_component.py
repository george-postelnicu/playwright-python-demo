from playwright.sync_api import Page

from src.pages.search_page import SearchPage


class MainNavComponent:
    def __init__(self, page: Page):
        self.page = page
        self.navigation_header = page.locator("//nav[contains(@id, 'navigationheader')]")
        self.search_section = page.locator("//section[@role='search']")
        self.search_field = self.search_section.locator("//input")

    def navigate(self, main_category: str, second_category: str, open_in_new_tab: bool) -> Page:
        main_nav = self.navigation_header.locator("//a[contains(@class, 'cmp-navigation__item-link')]").filter(has_text=main_category)
        main_nav.hover()

        # //div[contains(@class, 'cmp-navigation__flyout --visible')]
        second_nav = self.navigation_header.locator("//a[contains(@class, 'cmp-navigation__flyout-group-item-link')]").filter(
            has_text=second_category)
        with self.page.context.expect_page() as new_page_info:
            second_nav.click(modifiers=["ControlOrMeta"] if open_in_new_tab else None)
            new_page_info.value.bring_to_front() if open_in_new_tab else None
        return new_page_info.value if open_in_new_tab else self.page

    def open_search(self) -> None:
        self.search_section.click()

    def close_search(self) -> None:
        self.search_section.locator(".cmp-search__clear-icon").click()

    def search(self, search_term: str) -> SearchPage:
        self.search_section.click()
        self.search_field.fill(search_term)
        self.search_field.press("Enter")
        return SearchPage(self.page)