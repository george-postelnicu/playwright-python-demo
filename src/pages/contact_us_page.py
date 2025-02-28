from enum import Enum
from typing import Optional

from playwright.sync_api import Page, Locator

from src.models.contact_us_form import ContactUsForm


class FieldsetEnum(Enum):
    FIRSTNAME = "hs-firstname"
    LASTNAME = "hs-lastname"
    COMPANY = "hs-company"
    EMAIL = "hs-email"
    JOB_TITLE = "hs-jobtitle"
    PHONE = "hs-phone"
    COUNTRY = "hs-country"
    CONTACT_TOPIC = "hs-contact_topic"
    MESSAGE = "hs-situation__c"


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.get_by_role('heading', level=1)
        self.form_errors = page.locator("//div[contains(@class, 'hs_error_rollup')]//label")

    def fill_form(self, form: ContactUsForm) -> None:
        if form.firstname is not None:
            self.page.locator("//input[@name='firstname']").fill(form.firstname)
        if form.lastname is not None:
            self.page.locator("//input[@name='lastname']").fill(form.lastname)
        if form.company is not None:
            self.page.locator("//input[@name='company']").fill(form.company)
        if form.email is not None:
            self.page.locator("//input[@name='email']").fill(form.email)
        if form.job_title is not None:
            self.page.locator("//input[@name='jobtitle']").fill(form.job_title)
        if form.phone is not None:
            self.page.locator("//input[@name='phone']").fill(form.phone)
        if form.country is not None:
            self.page.locator("//select[@name='country']").select_option(label=form.country)
        if form.contact_topic is not None:
            self.page.locator("//select[@name='contact_topic']").select_option(label=form.contact_topic)
        if form.message is not None:
            self.page.locator("//textarea[@name='situation__c']").fill(form.message)

    def get_form_field_error_label(self, field: FieldsetEnum) -> Locator:
        return self.page.locator(f"//form//fieldset/div[contains(@class, '{field.value}')]").locator(
            "//label[contains(@class, 'hs-error-msg')]")

    @staticmethod
    def get_value_of_form(field: FieldsetEnum, form: ContactUsForm) -> Optional[str]:
        match field:
            case FieldsetEnum.FIRSTNAME:
                return form.firstname
            case FieldsetEnum.LASTNAME:
                return form.lastname
            case FieldsetEnum.COMPANY:
                return form.company
            case FieldsetEnum.EMAIL:
                return form.email
            case FieldsetEnum.JOB_TITLE:
                return form.job_title
            case FieldsetEnum.PHONE:
                return form.phone
            case FieldsetEnum.COUNTRY:
                return form.country
            case FieldsetEnum.CONTACT_TOPIC:
                return form.contact_topic
            case FieldsetEnum.MESSAGE:
                return form.message
            case _:
                return None

    def submit(self) -> None:
        self.page.locator("//input[@value='Send Request']").click()
