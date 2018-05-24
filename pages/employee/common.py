from time import sleep

from environment import *
from framework.common import PageObject, Page
from framework.selenium_plus import goto, set, click, get
from ..components import *

__all__ = ['EmployeeLoginPage']


@PageObject
class EmployeeLoginPage(Page):
    class ID:
        txtEmployeeID = "id=employee-phone"
        txtPassword = "id=employee-password"
        errLblUsername = "xpath=//label[@for='employee-phone']/following-sibling::div[last()]"
        errLblPassword = "xpath=//label[@for='employee-password']/following-sibling::div[last()]"
        errPopUp = "div[open] span"
        btnLogin = "button#login-submit-action"
        btnProfile = "#header-profile"

    class ERROR_MESSAGE:
        errMsgRequired = "CORE_COMMON_REQUIRED_ERRMSG"
        errPop = "Invalid login credentials"
        errMsgEnterValidName = "Please enter a valid user name"
        errMsgEnterValidPassword = "Password is Incorrect"

    def navigate(self):
        url = BASE_URL + APP_EMPLOYEE_URL
        goto(url)
        return url

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

    def get_user_name_error_message(self):
        return get(self.ID.errLblUsername)

    def get_password_error_message(self):
        return get(self.ID.errLblPassword)

    def get_error_pop_up_message(self):
        return get(self.ID.errPopUp)
