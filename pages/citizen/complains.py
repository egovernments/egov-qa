from typing import List

from framework.common import PageObject, Page
from framework.selenium_plus import *
from ..components import *

__all__ = ['AddComplaintPage', 'ComplaintFeedbackPage', 'ComplaintSubmittedPage', 'MyComplaintsPage',
           'ReopenComplaintPage']


@PageObject
class AddComplaintPage(Page, UploadImageComponent, LocationComponent, ComplaintTypeComponent):
    class ID:
        btnFileComplaint = "div#home-new-complaint"
        txtLocation = "input#address"
        txtComplaintDetails = "[id='additional details']"
        txtComplaintType = "input#complaint-type"
        txtLandmarkDetails = "input#landmark"
        btnSubmit = "button#addComplaint-submit-complaint"

    def file_complaint(self):
        click(self.ID.btnFileComplaint)
        return self

    def set_location_by_address(self, address, result_index=0):
        click(self.ID.txtLocation)
        time.sleep(2)
        return super(AddComplaintPage, self).set_location_by_address(address, result_index)

    def set_complaint_type(self, complaint_type, complaint_filter=None):
        click(self.ID.txtComplaintType)
        self.select_complaint_type(complaint_type, complaint_filter)

    def set_landmark_details(self, details):
        set(self.ID.txtLandmarkDetails, details)

    def set_complaint_details(self, details):
        set(self.ID.txtComplaintDetails, details)

    def submit(self):
        click(self.ID.btnSubmit)
        return self


@PageObject
class ComplaintFeedbackPage(Page):
    class ID:
        prmStarRating = "span#feedback-ratings{}"
        chkServices = "input#feedback-checkbox0"
        chkResolutionTime = "input#feedback-checkbox1"
        chkQualityOfWork = "input#feedback-checkbox2"
        chkOthers = "input#feedback-checkbox3"
        txtFeedbackComment = "textarea#feedback-comments"
        btnFeedbackSubmit = "button#feedback-submit"

    def set(self, feedback_comment):
        set(self.ID.txtFeedbackComment, feedback_comment)
        return self

    def star_click(self, a):
        click(self.ID.prmStarRating.format(int(a) - 1))
        return self

    def check_services(self):
        click(self.ID.chkServices)
        return self

    def check_resolution_time(self):
        click(self.ID.chkResolutionTime)
        return self

    def check_quality_of_work(self):
        click(self.ID.chkQualityOfWork)
        return self

    def check_others(self):
        click(self.ID.chkOthers)
        return self

    def submit(self):
        click(self.ID.btnFeedbackSubmit)
        return self


@PageObject
class ComplaintSubmittedPage(Page):
    class ID:
        btnContinue = "#complaint-submitted-continue"
        lblComplainNumber = ".complaint-number-value .label-text"
        lblComplaintSuccessfulMessage = "xpath=//div[contains(text(),'Complaint registered successfully')]"

    def get_complaint_number(self):
        return get(self.ID.lblComplainNumber)

    def click_continue(self):
        click(self.ID.btnContinue)


@PageObject
class MyComplaintsPage(Page):
    class ID:
        btnMyComplaints = "div#home-old-complaint"
        rowComplaintCards = "xpath=//div[contains(@class,'complaint-card-wrapper')]"
        btnAddComplaintPlus = "button#mycomplaints-add"
        txtComment = "div#citizen-comment"
        btnSend = "svg[class='comment-send']"

    def get_all_complaints(self) -> List[ComplainCardComponent]:
        cards = []
        for card in finds(self.ID.rowComplaintCards):
            cards.append(ComplainCardComponent(card))

        return cards

    def select_my_complaint(self):
        click(self.ID.btnMyComplaints)
        return self

    def add_complaint_plus_button(self):
        click(self.ID.btnAddComplaintPlus)
        return self

    def add_comments(self, citizen_comment):
        set(self.ID.txtComment, citizen_comment)
        return self

    def send_comment(self):
        click(self.ID.btnSend)
        return self


@PageObject
class ReopenComplaintPage(Page):
    class ID:
        radReopenReason = "input#reopencomplaint-radio-button-0"
        txtTypeComplaint = "div#reopencomplaint-comment-field"
        btnSubmit = "button#reopencomplaint-submit-action"

    def set(self, type_complaint):
        set(self.ID.txtTypeComplaint, type_complaint)
        return self

    def submit(self):
        click(self.ID.btnSubmit)
        return self
