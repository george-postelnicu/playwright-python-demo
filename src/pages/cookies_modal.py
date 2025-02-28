from playwright.sync_api import Page


class CookiesModal:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.modal = page.locator("#CybotCookiebotDialog")
        self.accept_button = page.locator("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")

    def accept_cookies(self) -> None:
        self.modal.wait_for(state="visible")
        self.accept_button.click()
        self.modal.wait_for(state="hidden")
