from time import sleep

from environment import *
from framework.common import PageObject, Page
from framework.selenium_plus import goto, set, click, get, wait_for_appear_then_disappear
from ..components import *

__all__ = ['LoginPage', 'OTPPage', 'RegistrationPage', 'LogoutPage']


@PageObject
class LoginPage(Page):
    class ID:
        txtMobileNumber = "input#person-phone"
        btnLogin = "button#login-submit-action"
        btnProfile = "#header-profile"
        lblMobileNumber = "//label[contains(text(), 'Mobile Number')]"
        lblMobileNumberErrrorMessage = "xpath=//label[@for='person-phone']/following-sibling::div[last()]"
        lblUserNameValidation = "div#root>div>div>div"

    def navigate(self):
        url = BASE_URL + APP_CITIZEN_URL
        goto(url)
        return self

    def set(self, mobile_number):
        set(self.ID.txtMobileNumber, mobile_number)
        return self

    def submit(self):
        click(self.ID.btnLogin)
        return self

    def profile(self):
        click(self.ID.btnProfile)
        return self

    def get_mobileno_error_message(self):
        required = get(self.ID.lblMobileNumberErrrorMessage)
        return required

    def get_citizen_login_id(self):
        return get(self.ID.lblMobileNumber)

    def user_not_found(self):
        return get(self.ID.lblUserNameValidation)


@PageObject
class OTPPage(Page):
    class ID:
        txtOTP = "input#otp"
        btnGetStarted = "button#otp-start"
        btnResend = "div#otp-resend"
        lblOTPSentTo = "xpath=//div[@class='label-text otp-mobile-number']"
        lblErrorMsg = "xpath=//label[@for='otp']/following-sibling::div[last()]"
        lblResentOTPMsg = "xpath=//span[text()='OTP has been Resent']"
        lblToaster = "div#toast-message span"

    def set(self, otp):
        set(self.ID.txtOTP, otp)
        return self

    def get_started(self):
        click(self.ID.btnGetStarted)
        return self

    def resend(self):
        click(self.ID.btnResend)
        return wait_for_appear_then_disappear(self.ID.lblToaster)

    def otp_sent_to(self):
        return get(self.ID.lblOTPSentTo)

    def otp_required(self):
        return get(self.ID.lblErrorMsg)

    def invalid_otp(self):
        return get(self.ID.lblErrorMsg)

    def otp_has_resent(self):
        return get(self.ID.lblResentOTPMsg)


@PageObject
class RegistrationPage(Page, SelectCityComponent):
    class ID:
        drpCity = "input#person-city"
        txtPhoneNumber = "input#person-phone"
        txtName = "input#person-name"
        btnSubmit = "button#login-submit-action"
        btnLogin = "div#otp-resend"

    def set_city(self, city):
        click(self.ID.drpCity)
        super(RegistrationPage, self).set_city(city)

    def set(self, phone_number, name, city):
        set(self.ID.txtPhoneNumber, phone_number)
        set(self.ID.txtName, name)
        self.set_city(city)
        return self

    def submit(self):
        sleep(1)
        click(self.ID.btnSubmit)
        return self

    def login(self):
        click(self.ID.btnLogin)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register")
        return self


@PageObject
class LogoutPage(Page):
    class ID:
        btnLogout = "xpath=.//div[text()='Logout']"
        btnYes = "xpath=.//div[text()='Yes']"

    def submit(self):
        click(self.ID.btnLogout)
        click(self.ID.btnYes)
        return self
