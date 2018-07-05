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
        set_text(self.ID.txtUsername, username)
        return self

    def password(self,password):
        set_text(self.ID.txtPassword, password)
        return self

    def submit(self):
        click(self.ID.btnsubmit)
        return self

    def navigate(self):
        goto(BASE_URL+APP_EMPLOYEE_URL)
        return self


