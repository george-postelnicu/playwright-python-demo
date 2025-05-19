import gettext
from typing import Optional

import pytest
from faker import Faker
from playwright.sync_api import Page, expect, Locator

from src.models.contact_us_form import ContactUsForm
from src.pages.brochure_page import BrochurePage
from src.pages.contact_us_page import ContactUsPage, FieldsetEnum
from src.pages.lucanet_home_page import LucaNetHomePage
from src.pages.main_nav_component import MainNavComponent
from src.pages.search_page import SearchPage
from src.pages.top_nav_component import Language
from src.utils.utils import sha256sum

# Set the local directory
domain = 'lokalise'
localedir = './locales'


@pytest.fixture(scope="function", autouse=True)
def home_page(page: Page):
    home_page: LucaNetHomePage = LucaNetHomePage(page)
    home_page.load()
    home_page.cookies_modal.accept_cookies()
    yield home_page

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.mark.title
def test_has_title(home_page) -> None:
    expect(home_page.page).to_have_title("The CFO Solution Platform. Cloud-first. AI-elevated :: Lucanet")
    expect(home_page.main_header).to_have_text("The CFO Solution Platform for future-ready finance leaders")


@pytest.mark.language
@pytest.mark.parametrize("language", [
    "de",
    "en",
    "es",
    "fr",
    "it",
    "nl"
])
def test_can_change_language(home_page, language) -> None:
    i18n = gettext.translation(domain, localedir, fallback=False, languages=[language])
    i18n.install()
    if language != "en":
        home_page.top_nav_component.select_language(Language[language.upper()])
    expect(home_page.page).to_have_title(_("home_page.title"))
    expect(home_page.main_header).to_have_text(_("home_page.header"))


@pytest.mark.search
def test_can_close_search_modal(home_page) -> None:
    main_nav: MainNavComponent = home_page.main_nav_component
    main_nav.open_search()
    expect(main_nav.search_field).to_be_visible()
    main_nav.close_search()
    expect(main_nav.search_field).to_be_hidden()


@pytest.mark.search
def test_wrong_search_returns_no_results(home_page) -> None:
    main_nav: MainNavComponent = home_page.main_nav_component
    search_page: SearchPage = main_nav.search("abcd")
    expect(search_page.result_hits).to_have_text("Showing 0 search results")
    expect(search_page.no_result_big_message).to_have_text("Sorry, no results matched your search terms.")
    expect(search_page.result_links).to_have_count(0)


@pytest.mark.search
def test_ifrs_search_returns_results(home_page) -> None:
    main_nav: MainNavComponent = home_page.main_nav_component
    search_page: SearchPage = main_nav.search("IFRS")
    expect(search_page.result_hits).to_have_text("Showing 92 search results")
    expect(search_page.no_result_big_message).to_be_hidden()
    expect(search_page.result_links).to_have_count(92)


@pytest.mark.window
def test_multi_window_contact_page(home_page) -> None:
    main_nav: MainNavComponent = home_page.main_nav_component
    navigation_links = [
        {"main": "Solutions", "secondary": "Solutions", "header": "Integrated solutions for all CFO jobs-to-be-done"},
        {"main": "Platform", "secondary": "Innovation Hub", "header": "Innovation Hub"},
        {"main": "Customers", "secondary": "Our partners", "header": "Meet our trusted partners"},
        {"main": "Resources", "secondary": "Blog", "header": "Insights"},
        {"main": "Why Lucanet", "secondary": "About Us", "header": "We're Lucanet"}]
    for navigation in navigation_links:
        new_page: Page = main_nav.navigate(navigation["main"], navigation["secondary"], True)
        expect(new_page.get_by_role('heading', level=1)).to_have_text(navigation["header"])
        new_page.close()


@pytest.mark.form
def test_contact_us_form_with_missing_phone(home_page) -> None:
    contact_page: ContactUsPage = home_page.main_nav_component.click_contact_us()
    form: ContactUsForm = get_contact_form()
    contact_page.fill_form(form)
    contact_page.submit()
    expect(contact_page.form_errors).to_have_text("Please complete all required fields.")
    for field in FieldsetEnum:
        label: Locator = contact_page.get_form_field_error_label(field)
        value_to_check: Optional[str] = ContactUsPage.get_value_of_form(field, form)
        if isinstance(value_to_check, str):
            expect(label).to_be_hidden()
        else:
            expect(label).to_have_text("Please complete this required field.")


@pytest.mark.download
def test_download_brochure_file(page: Page) -> None:
    brochure_page: BrochurePage = BrochurePage(page)
    brochure_page.load('/en/resource-hub/infographics/find-the-right-consolidation-software/')
    expect(brochure_page.header).to_have_text('How Do I find the right financial consolidation software?')
    file_path: str = brochure_page.download()
    assert sha256sum(file_path) == (
        '6d35cedf7d1cbcf75a3b94f204fa5af987355b9da54bd821d85f096d55ce1b54'
    )


def get_contact_form() -> ContactUsForm:
    fake = Faker(locale="de_DE")
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f'{first_name.lower()}.{last_name.lower()}@abc.com'
    return ContactUsForm(
        firstname=first_name,
        lastname=last_name,
        company=fake.company(),
        email=email,
        job_title=fake.job(),
        phone=None,
        country='Romania',
        contact_topic="Appointment request",
        message=fake.text(max_nb_chars=100)
    )
