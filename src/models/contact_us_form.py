from dataclasses import dataclass
from typing import Optional


@dataclass
class ContactUsForm:
    firstname: Optional[str]
    lastname: Optional[str]
    company: Optional[str]
    email: Optional[str]
    job_title: Optional[str]
    phone: Optional[str]
    country: Optional[str]
    contact_topic: Optional[str]
    message: Optional[str]
