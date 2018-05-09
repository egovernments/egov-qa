from framework.common import PageObject, Page
from framework.selenium_plus import *

__all__ = ['LoginEmployeePage']

from environment import *

@PageObject
class LoginEmployeePage(Page):
    class ID:
        btnSubmit="#login-submit-action"
        txtUsername="#employee-phone"
        txtPassword="#employee-password"

    def username(self,username):
        set(self.ID.txtUsername,username)
        return self

    def password(self,password):
        set(self.ID.txtPassword,password)
        return self

    def submit(self):
        click(self.ID.btnsubmit)
        return self

    def navigate(self):
        print(BASE_URL)
        print(APP_EMPLOYEE_URL)
        goto(BASE_URL+APP_EMPLOYEE_URL)
        return self


