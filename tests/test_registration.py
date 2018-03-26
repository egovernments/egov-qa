from pages import OTPPage, AddComplaintPage, ComplaintTypePage, TopMenuPage, BottomMenuPage, ProfilePage
from framework.selenium_plus import *
from pages import LoginPage
from pages.ReopenComplaint import ReopenComplaintPage


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
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    quit_driver()


def test_reopen_complaint():
    ReopenComplaintPage.navigate().set("Complaint not resolved").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-submitted"
    quit_driver()


def test_complaint_details():
    ComplaintTypePage.navigate()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=filed"
    quit_driver()


def test_navigation():
    LoginPage.navigate().set("9999999999").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    BottomMenuPage.info().payments().complaints().home()
    TopMenuPage.ham()
    LoginPage.profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    TopMenuPage.back()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    quit_driver()

    # this test is for verifying navigation


def test_profile():
    LoginPage.navigate().set("9999999999").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    TopMenuPage.ham()
    LoginPage.profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    ProfilePage.profileupdate("Singh", "def@ulb.in")
    ProfilePage.profilephotoremover()
    ProfilePage.profilesave()
    TopMenuPage.back()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    quit_driver()
