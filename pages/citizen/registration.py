from time import sleep

from framework.common import PageObject, Page
from framework.selenium_plus import goto, set, click
from ..components import *

from environment import *
__all__ = ['LoginPage', 'OTPPage', 'RegistrationPage','LogoutPage']

@PageObject
class LoginPage(Page):
    class ID:
        txtMobileNumber = "input#person-phone"
        btnLogin = "button#login-submit-action"
        btnProfile = "#header-profile"

    def navigate(self):
        goto(BASE_URL + APP_CITIZEN_URL)
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


@PageObject
class OTPPage(Page):
    class ID:
        txtOTP = "input#otp"
        btnGetStarted = "button#otp-start"
        btnResend = "div#otp-resend"

    def set(self, otp):
        set(self.ID.txtOTP, otp)
        return self

    def get_started(self):
        click(self.ID.btnGetStarted)
        return self

    def resend(self):
        click(self.ID.btnResend)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp")
        return self


@PageObject
class RegistrationPage(Page, SelectCityComponent):
    class ID:
        drpCity = "input#person-city"
        txtPhoneNumber = "input#person-phone"
        txtName = "input#person-name"
        btnSubmit = "button#login-submit-action"

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

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register")
        return self


@PageObject
class LogoutPage(Page):
    class ID:
        btnLogout = "xpath=.//div[text()='Logout']"
        btnYes = "xpath=.//div[text()='Yes']"

    def navigate(self):
        goto(CITIZEN_HOME_URL)
        return self

    def submit(self):
        click(self.ID.btnLogout)
        click(self.ID.btnYes)
        return self
