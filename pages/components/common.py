from selenium.common.exceptions import InvalidElementStateException

from framework.common import Component, PageObject
from framework.selenium_plus import *
from framework.selenium_plus import click, set, finds, get

__all__ = ['ComplaintTypeComponent',
           'LocationComponent',
           'UploadImageComponent',
           'SelectCityComponent',
           'ComplainCardComponent',
           'TopMenuNavigationComponent',
           'BottomMenuComponent'
           ]


class ComplaintTypeComponent(Component):
    class ID:
        txtComplaintTypeSearch = "input#complainttype-search"
        prmLblComplaintType = "xpath=//div[.='{}']"

    def select_complaint_type(self, complaint_type, complaint_filter=None):
        if complaint_filter is None:
            complaint_filter = complaint_type

        set(self.ID.txtComplaintTypeSearch, complaint_filter)
        click(self.ID.prmLblComplaintType.format(complaint_type))
        return self


class LocationComponent(Component):
    class ID:
        txtSearchAddress = "input.searchBoxStyles"
        btnPickAddress = "button#map-pick-button"
        lblSearchAddressResults = "div.pac-container > div.pac-item"

    def set_location_by_address(self, address, result_index=0):
        set(self.ID.txtSearchAddress, address)
        elems = finds(self.ID.lblSearchAddressResults, condition=count_non_zero_and_clickable)
        assert len(elems) != 0, "No search results found"
        elems[result_index].click()
        text = get(self.ID.txtSearchAddress)
        click(self.ID.btnPickAddress)
        return text


class UploadImageComponent(Component):
    class ID:
        prmBtnRemoveImage = "xpath=(//div[contains(@class,'image-remove')])[{}]"
        fileImageUploadPlaceHolder = ".upload-placeholder input,.upload-photo-overlay input"
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
                unhide(elem)
                set(elem, image)


class SelectCityComponent(Component):
    class ID:
        prmLblCity = "xpath=//div[contains(@class, 'search-field-container')]/following-sibling::div[1]//div[contains(text(), '{}')]"
        txtSearch = "div.search-field-container input"

    def set_city(self, city):
        set(self.ID.txtSearch, city)
        click(self.ID.prmLblCity.format(city))
        return self


class ComplainCardComponent(Component):
    class ID:
        lblComplaintHeader = "span.complaint-header"
        lblComplaintStatus = ".complaint-status-text"
        lblComplaintDate = ".complaint-date"
        lblComplaintNo = ".complaint-complaint-number .label-text"
        btnTrack = ".complaint-track-btn button"
        colComplaintImages = ".complaint-image"


    def __init__(self, container=None):
        self.container = container

    def complain_images(self):
        return finds(self.ID.colComplaintImages)

    def get_complaint_header(self):
        return get(self.ID.lblComplaintHeader, context=self.container)

    def get_complaint_status(self):
        return get(self.ID.lblComplaintStatus, context=self.container)

    def get_complaint_date(self):
        return get(self.ID.lblComplaintDate, context=self.container)

    def get_complaint_no(self):
        return get(self.ID.lblComplaintNo, context=self.container)

    def track_complaint(self):
        click(self.container)





class BottomMenuComponent(Component):
    class ID:
        btnHome = ".bottom-navigation #home-button"
        btnInfo = "#information-button"
        btnPayments = "#payments-button"
        btnComplaints = "#complaints-button"

    def home(self):
        click(self.ID.btnHome)
        return self

    def info(self):
        click(self.ID.btnInfo)
        return self

    def payments(self):
        click(self.ID.btnPayments)
        return self

    def complaints(self):
        click(self.ID.btnComplaints)
        return self


class TopMenuNavigationComponent(Component):
    class ID:
        btnHam = "#icon-hamburger"
        btnBackNavigate = "#back-navigator"

    def ham(self):
        click(self.ID.btnHam)
        return self

    def back(self):
        click(self.ID.btnBackNavigate)
        return self


class SideBarComponent(Component):
    class ID:
        pass

    pass
