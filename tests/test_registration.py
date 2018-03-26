from pages import OTPPage, AddComplaintPage, RegistrationPage, ComplaintRejected, ComplaintResolved
from framework.selenium_plus import *


def test_otp_submission():
    otp = OTPPage
    otp.navigate()

    otp.set("1234").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"

def test_create_complaint():
    comp = AddComplaintPage
    comp.set_complaint_type("garbage", "Overflowing Garbage Bins")

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"

def test_user_registration():
    userRegistration = RegistrationPage
    userRegistration.navigate()
    userRegistration.set("9988776655", "FirstName", "Bathi").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"

def test_complaint_rejected():
    complaintRejected = ComplaintRejected
    complaintRejected.navigate()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=rejected"

def test_complaint_resolved():
    complaintResolved = ComplaintResolved
    complaintResolved.navigate()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=resolved"