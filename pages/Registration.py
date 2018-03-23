from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _OTPPage(Page):
    class ID:
        # txtOTP = "xpath=//input[@id='otp']"
        # txtOTP = "input#otp"
        txtOTP = "id=otp"
        btnGetStarted = "button#otp-start"
        btnResend = "div#otp-resend"

    def set(self, otp):
        set(ID.txtOTP, otp)
        return self

    def submit(self):
        click(ID.btnGetStarted)
        return self

    def resend(self):
        click(ID.btnResend)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp")
        return self

OTPPage = _OTPPage()