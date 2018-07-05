from time import sleep

from environment import *
from framework.common import PageObject, Page
from framework.selenium_plus import goto, set_text, click, get, click_using_js
from ..components import *

__all__ = ['EmployeeLoginPage', 'EmployeeComplaintAcknowledgementPage']


@PageObject
class EmployeeLoginPage(Page):
    class ID:
        txtEmployeeID = "id=employee-phone"
        txtPassword = "id=employee-password"
        txtCitySearch = "input#city-picker-search"
        drpCity = "input#person-city"
        errLblUsername = "xpath=//label[@for='employee-phone']/following-sibling::div[last()]"
        errLblPassword = "xpath=//label[@for='employee-password']/following-sibling::div[last()]"
        errPopUp = "div[open] span"
        btnLogin = "button#login-submit-action"
        btnProfile = "#header-profile"
        prmLblCity = "xpath=//div[contains(text(), '{}')]"

    class ERROR_MESSAGE:
        errMsgRequired = "CORE_COMMON_REQUIRED_ERRMSG"
        errPop = "Invalid login credentials"
        errMsgEnterValidName = "Please enter a valid user name"
        errMsgEnterValidPassword = "Password is Incorrect"

    def navigate(self):
        url = BASE_URL + APP_EMPLOYEE_URL
        goto(url)
        return self

    def employee_id(self, employee_id):
        set_text(self.ID.txtEmployeeID, employee_id)
        return self

    def password(self, password):
        set_text(self.ID.txtPassword, password)
        return self

    def submit(self):
        click_using_js(self.ID.btnLogin) # TODO : fix this issue
        return self

    def city(self, city):
        click(self.ID.drpCity)
        set_text(self.ID.txtCitySearch, city)
        click(self.ID.prmLblCity.format(city))
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


@PageObject
class EmployeeComplaintAcknowledgementPage(Page):
    class ID:
        lblAssignedTo = "div.label-container.thankyou-text"
        btnGoToHome = "button#resolve-success-continue"

    def go_to_home(self):
        click(self.ID.btnGoToHome)
        return self