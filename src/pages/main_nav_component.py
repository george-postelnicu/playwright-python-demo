from playwright.sync_api import Page


class MainNavComponent:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, main_category: str, second_category: str, open_in_new_tab: bool) -> Page:
        main_nav = self.page.locator("//a[contains(@class, 'main-navigation__item')]").filter(has_text=main_category)
        main_nav.hover()

        second_nav = self.page.locator("//ul[contains(@class, 'main-navigation__sub-listitem')]//a").filter(
            has_text=second_category)
        with self.page.context.expect_page() as new_page_info:
            second_nav.click(modifiers=["ControlOrMeta"] if open_in_new_tab else None)
            new_page_info.value.bring_to_front() if open_in_new_tab else None
        return new_page_info.value if open_in_new_tab else self.page
