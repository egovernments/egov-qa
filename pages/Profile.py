from framework.common import PageObject, Page
from framework.selenium_plus import *


@PageObject
class _ProfilePage(Page):
    class ID:
        txtProfileName = "#profile-form-name"
        txtPersonCity = "#person-city"
        txtProfileEmailId = "#profile-form-email"
        txtSearchCity = "#undefined-Search--1135"  # todo, id is dynamic
        btnCity = "div:nth-child(1)>div>div>div>div:nth-child(3)"  # todo, required id
        btnProfileSave = "#profile-save-action"
        btnProfilePhoto = "#profile-upload-icon"
        btnPhotoRemover = "#uploadDrawerRemoveIcon"

    def update(self, name, emailid):
        set(self.ID.txtProfileName, name)
        set(self.ID.txtProfileEmailId, emailid)

    def photo_remover(self):
        click(self.ID.btnProfilePhoto)
        click(self.ID.btnPhotoRemover)

    def save(self):
        click(self.ID.btnProfileSave)
        return self


ProfilePage = _ProfilePage()
