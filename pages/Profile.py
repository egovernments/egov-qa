from framework.common import PageObject, Page
from framework.selenium_plus import *


@PageObject
class _ProfilePage(Page):
    class ID:
        txtProfileName = "#profile-form-name"
        txtProfileEmailId = "#profile-form-email"
        btnProfileSave = "#profile-save-action"
        btnProfilePhoto = "#profile-upload-icon"
        btnPhotoRemove = "#uploadDrawerRemoveIcon"

    def update(self, name, emailid):
        set(self.ID.txtProfileName, name)
        set(self.ID.txtProfileEmailId, emailid)

    def photo_remove(self):
        click(self.ID.btnProfilePhoto)
        click(self.ID.btnPhotoRemove)

    def save(self):
        click(self.ID.btnProfileSave)
        return self


ProfilePage = _ProfilePage()
