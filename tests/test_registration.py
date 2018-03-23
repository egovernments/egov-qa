from pages import OTPPage, AddComplaintPage
from framework.selenium_plus import *
from pages.CitizenProfile import CitizenProfilePage
from pages.ComplaintSubmitted import ComplaintSubmittedPage


def test_otp_submission():
    otp = OTPPage
    otp.navigate()

    otp.set("1234").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():
    comp = AddComplaintPage
    comp.set_complaint_type("garbage", "Overflowing Garbage Bins")

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_citizen_profile():
    CitizenProfilePage.navigate().set("ABH", "ab.se@gmail.com").set_city("Amritsar").click_continue()

def test_complain_submitted():
    ComplaintSubmittedPage.navigate()
    print(ComplaintSubmittedPage.get_complaint_number())
    ComplaintSubmittedPage.click_continue()
