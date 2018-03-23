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
#for Each Button Make one method

    def set(self, otp):
        set(self.ID.txtOTP, otp)
        return self

    def submit(self):
        click(self.ID.btnGetStarted)
        return self

    def resend(self):
        click(self.ID.btnResend)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp")
        return self

OTPPage = _OTPPage()