from playwright.sync_api import Page

from src.pages.cookies_modal import CookiesModal
from src.pages.main_nav_component import MainNavComponent
from src.pages.search_modal import SearchModal
from src.pages.top_nav_component import TopNavComponent


class LucaNetHomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.main_header = page.locator(".hero-advanced__headline--default")
        self.cookies_modal = CookiesModal(page)
        self.search_modal = SearchModal(page)
        self.top_nav_component = TopNavComponent(page)
        self.main_nav_component = MainNavComponent(page)

    def load(self) -> None:
        self.page.goto("/")
