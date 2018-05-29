from pages.citizen.common import *
from pages.citizen.registration import *


def test_register_with_mobile_number_less_than_10():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set(876543, 'satish', 'Amritsar')
    registration.submit()


def test_register_with_mobile_number_greater_than_10():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set(87654398887773333, 'satish', 'Amritsar')
    registration.submit()


def test_register_mobile_number_with_specialchar():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set("876543Lhkjh", 'satish', 'Amritsar')
    registration.submit()


def test_duplicate_mobile_number():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set("8792101399", 'satish', 'Amritsar').submit()
    registration.navigate().set("8792101399", 'satish', 'Amritsar').submit()


def test_citizen_login_assertions():
    login_page = LoginPage()
    citizen_url = login_page.navigate()

    # Required field assertion
    citizen_url.submit()
    mobile_number_required = login_page.get_mobileno_error_message()
    assert mobile_number_required == "Invalid Mobile Number", "Mobile Number is mandatory field to be enter"

    # Mobile number validation
    citizen_url.set("1").submit()
    invalid_mobile_number = login_page.get_mobileno_error_message()
    assert invalid_mobile_number == "Invalid Mobile Number", "Mobile Number should contain 10 digits only"

    citizen_url.set("797517933").submit()
    assert invalid_mobile_number == "Invalid Mobile Number", "Mobile Number should contain 10 digits only"

    citizen_url.set("79751793345").submit()
    assert invalid_mobile_number == "Invalid Mobile Number", "Mobile Number should contain 10 digits only"

    # Mobile number existence validation
    citizen_url.set("1234567890").submit()
    user_not_found = login_page.user_not_found()
    assert user_not_found == "User not Found With this UserName", "Only Registered mobile number is valid"


def test_otp_assertions():
    login_page = LoginPage()
    otp_page = OTPPage()
    citizen_url = login_page.navigate()

    # OTP field
    citizen_url.set("7975179334").submit()
    assert otp_page.otp_sent_to() == "7975179334"
    assert otp_page.enter_otp() == "Enter OTP"

    # OTP required field validation
    otp_page.get_started()
    assert otp_page.otp_required() == "Required"

    # Validation for OTP entered
    otp_page.set("1")
    assert otp_page.invalid_otp() == "Invalid OTP"

    otp_page.set("12345")
    assert otp_page.invalid_otp() == "Invalid OTP"

    otp_page.set("1234567")
    assert otp_page.invalid_otp() == "Invalid OTP"

    # Resend OTP validation
    assert otp_page.resend() == "OTP has been Resent"


def test_add_complaint_assertion():
    pass
