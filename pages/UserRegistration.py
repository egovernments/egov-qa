from time import sleep

from framework.common import Page, PageObject
from framework.selenium_plus import *
from logging import *


@PageObject
class _RegistrationPage(Page):
    class ID:
        txtPhoneNumber = "input#person-phone-number"
        txtName = "input#person-name"
        txtCity = "input#person-city"
        # todo: fix this identified
        btnSubmit = "button#login-submit-action"
        # todo: fix this identifed by UI team-
        txtSearchCity = "input[id*='Search']"
        prmLblSearchResultCity = "xpath=//div[contains(text(), '{}')]"

    def set(self, phoneNumber, name, city):
        set(self.ID.txtPhoneNumber, phoneNumber)
        set(self.ID.txtName, name)
        self.set_city(city)
        return self

    def set_city(self, city):
        click(self.ID.txtCity)
        set(self.ID.txtSearchCity, city)
        click(self.ID.prmLblSearchResultCity.format(city))

    def submit(self):
        sleep(1)
        click(self.ID.btnSubmit)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register")
        return self

RegistrationPage = _RegistrationPage()