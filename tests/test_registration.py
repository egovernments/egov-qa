from pages import OTPPage, AddComplaintPage, RegistrationPage
from framework.selenium_plus import *
from pages.CitizenProfile import CitizenProfilePage
from pages.ComplaintSubmitted import ComplaintSubmittedPage
from pages.MyComplaints import MyComplaintsPage


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
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"

def test_my_complaints():
    complaints = MyComplaintsPage
    complaints.navigate()
    cards = complaints.get_all_complaints()
    card = cards[2]

    print (card.get_complaint_header())
    print( card.get_complaint_status())
    print(card.get_complaint_no())
    print(card.get_complaint_date())
    card.track_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=rejected"

def test_user_registration():
    userRegistration = RegistrationPage
    userRegistration.navigate()
    userRegistration.set("9988776655", "FirstName", "Bathi").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"
