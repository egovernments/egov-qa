from framework.common import PageObject, Page
from framework.selenium_plus import *
from ..components import *

__all__ = ['CitizenProfilePage', 'ProfilePage']


@PageObject
class CitizenProfilePage(Page, SelectCityComponent):
    class ID:
        txtName = "input#profile-form-name"
        txtEmailId = "input#profile-form-email"
        btnSave = "button#profile-save-action"
        drpCity = "input#person-city"

    def set_city(self, city):
        click(self.ID.drpCity)
        super(CitizenProfilePage, self).set_city(city)
        return self

    def set(self, name, email):
        set(self.ID.txtName, name)
        set(self.ID.txtEmailId, email)
        return self

    def save(self):
        click(self.ID.btnSave)
        return self


@PageObject
class ProfilePage(Page):
    class ID:
        txtProfileName = "#profile-form-name"
        txtProfileEmailId = "#profile-form-email"
        btnProfileSave = "#profile-save-action"
        btnProfilePhoto = "#profile-upload-icon"
        btnPhotoRemove = "#uploadDrawerRemoveIcon"
        lblToaster = "#toast-message span"

    def update(self, name, email_id):
        clear(self.ID.txtProfileName)
        set(self.ID.txtProfileName, name)
        clear(self.ID.txtProfileEmailId)
        set(self.ID.txtProfileEmailId, email_id)

    def photo_remove(self):
        click(self.ID.btnProfilePhoto)
        click(self.ID.btnPhotoRemove)

    def save(self):
        click(self.ID.btnProfileSave)
        return wait_for_appear_then_disappear(self.ID.lblToaster)