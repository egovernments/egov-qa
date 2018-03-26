from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _CitizenProfilePage(Page):
    class ID:
        txtName = "input#profile-form-name"
        txtEmailId = "input#profile-form-email"
        drpCity = "input#person-city"
        btnSave = "button#profile-save-action"
        txtSearch = "div.search-field-container input"
        prmLblCity = "xpath=//div[.='{}']"

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile")
        return self

    def set(self, name, email):
        set(self.ID.txtName, name)
        set(self.ID.txtEmailId, email)
        return self

    def set_city(self, city):
        click(self.ID.drpCity)
        set(self.ID.txtSearch, city)
        click(self.ID.prmLblCity.format(city))
        return self

    def save(self):
        click(self.ID.btnSave)
        return self


CitizenProfilePage = _CitizenProfilePage()
