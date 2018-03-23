from pages import OTPPage, AddComplaintPage, ReopenComplaintPage
from framework.selenium_plus import *
from pages import LoginPage


def test_otp_submission():
    otp = OTPPage
    otp.navigate()

    otp.set("1234").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():
    comp = AddComplaintPage
    comp.set_complaint_type("garbage", "Overflowing Garbage Bins")

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/stv3/citizen/add-complaint"


def test_login():
    LoginPage.navigate().set("1234567890").submit()
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    # quit_driver()


def test_reopen_complaint():
    ReopenComplaintPage.navigate().set("Complaint not resolved").submit()
