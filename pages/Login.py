from framework.common import PageObject, Page
from framework.selenium_plus import *


@PageObject
class _LoginPage(Page):
    class ID:
        txtMobileNumber = "input[id='mobile-number-field']"
        btnLogin = "button[id='login-submit-action']"

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/login")
        return self

    def set(self, mobile_number):
        set(self.ID.txtMobileNumber, mobile_number)
        return self

    def submit(self):
        click(self.ID.btnLogin)
        return self


LoginPage = _LoginPage()
