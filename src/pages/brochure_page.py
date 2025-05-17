from playwright.sync_api import Page, Locator

class BrochurePage:
    def __init__(self, page: Page):
        self.page = page
        self.header: Locator = page.get_by_role('heading', level=1)
        self.__download_infographic: Locator = page.locator("//iframe[@title='Embedded CTA']").first.content_frame.get_by_text("Download infographic")

    def load(self, resource: str) -> None:
        self.page.goto(resource)

    def download(self) -> str:
        # Start waiting for the download
        with self.page.expect_download() as download_info:
            # Perform the action that initiates download
            self.__download_infographic.click()
        download = download_info.value

        # Wait for the download process to complete and save the downloaded file somewhere
        download_path = f"./downloads/{download.suggested_filename}"
        download.save_as(download_path)
        return download_path