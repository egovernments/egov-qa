from time import sleep

from environment import *
from framework.common import PageObject, Page
from framework.selenium_plus import goto, set, click
from ..components import *

__all__ = ['EmployeeLoginPage']


@PageObject
class EmployeeLoginPage(Page):
    class ID:
        txtEmployeeID = "id=employee-phone"
        txtPassword = "id=employee-password"
        btnLogin = "id=login-submit-action"
        btnProfile = "#header-profile"

    def navigate(self, end_point):
        goto(APP_HOST+end_point)
        return self

    def employee_id(self, employee_id):
        set(self.ID.txtEmployeeID, employee_id)
        return self

    def password(self, password):
        set(self.ID.txtPassword, password)
        return self

    def submit(self):
        click(self.ID.btnLogin)
        return self

    def profile(self):
        click(self.ID.btnProfile)
        return self

@PageObject
class EmployeeLogoutPage(Page):
    def logout(self):
        click(self.TopMenuNavigationComponent.ham())
