from selenium.common.exceptions import InvalidElementStateException

from framework.common import Page, PageObject, Component
from framework.selenium_plus import *


class UploadImageComponent(Component):
    class ID:
        prmBtnRemoveImage = "xpath=(//div[contains(@class,'image-remove')])[{}]"
        fileImageUploadPlaceHolder = ".upload-placeholder input,.upload-icon-cont input"
        pass

    def remove_image_1(self):
        click(self.ID.prmBtnRemoveImage.format(1))

    def remove_image_2(self):
        click(self.ID.prmBtnRemoveImage.format(2))

    def remove_image_3(self):
        click(self.ID.prmBtnRemoveImage.format(3))

    def upload_images(self, *images):
        assert 0 <= len(images) <= 3, "Maximum 3 photos can be uploaded"
        if not images:
            return

        for image in images:
            elem = find(self.ID.fileImageUploadPlaceHolder)
            try:
                set(elem, image)
            except InvalidElementStateException:
                execute_script("""
                var elem = arguments[0];
                elem.style.display = ""
                """, elem)
                set(elem, image)



@PageObject
class _AddComplaintPage(Page, UploadImageComponent):
    def __init__(self):
        print("i was called")


    class ID:
        txtLocation = "input#addComplaint-location-details"
        txtComplaintDetails = "input#addComplaint-additional-details"
        txtComplaintType = "input#addComplaint-complaint-type"
        txtLandmarkDetails = "input#addComplaint-landmark-details"
        txtSearchAddress = "input.searchBoxStyles"
        # Todo: The pick button should have an id
        btnPickAddress = "button#map-pick-button"
        lblSearchAddressResults = "div.pac-container > div.pac-item"


    def set_location_by_address(self, address, result_index=0):
        click(self.ID.txtLocation)
        set(self.ID.txtSearchAddress, address)
        elems = finds(self.ID.lblSearchAddressResults, condition=count_non_zero_and_clickable)
        assert len(elems) != 0, "No search results found"
        elems[result_index].click()

        click(self.ID.btnPickAddress)

    def set_complaint_type(self, filter_city, complaint_type):
        click(self.ID.txtComplaintType)
        ComplaintTypePage.set(filter_city).select_complaint_type(complaint_type)

    def set_landmark_details(self, details):
        set(self.ID.txtLandmarkDetails, details)

    def set_complaint_details(self, details):
        set(self.ID.txtComplaintDetails, details)

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint")



@PageObject
class _ComplaintTypePage(Page):
    class ID:
        txtComplaintTypeSearch = "input#complainttype-search"
        prmLblComplaintType = "xpath=//div[.='{}']"

    def set(self, complaint_filter):
        set(self.ID.txtComplaintTypeSearch, complaint_filter)
        return self

    def select_complaint_type(self, complaint_type):
        click(self.ID.prmLblComplaintType.format(complaint_type))
        return self


ComplaintTypePage = _ComplaintTypePage()

AddComplaintPage = _AddComplaintPage()
