from typing import List

from framework.common import PageObject, Page
from framework.selenium_plus import *
from ..components import *

__all__ = ['AddComplaintPage', 'ComplaintFeedbackPage', 'ComplaintSubmittedPage', 'MyComplaintsPage',
           'ReopenComplaintPage', 'ComplaintSummaryPage']


@PageObject
class AddComplaintPage(Page, UploadImageComponent, LocationComponent, ComplaintTypeComponent):
    class ID:
        btnFileComplaint = "div#home-new-complaint"
        txtLocation = "input#address"
        txtComplaintDetails = "textarea[id='additional details']"
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
        return self

    def set_landmark_details(self, details):
        set(self.ID.txtLandmarkDetails, details)
        return self

    def set_complaint_details(self, details):
        set(self.ID.txtComplaintDetails, details)
        return self

    def click_submit(self):
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
        btnFeedbackSubmit = "button#feedback-submit-action"

    def set(self, feedback_comment):
        set(self.ID.txtFeedbackComment, feedback_comment)
        return self

    def star_click(self, a):
        click(self.ID.prmStarRating.format(int(a) - 1), condition=EC.presence_of_element_located)
        return self

    def check_services(self):
        click(self.ID.chkServices, condition=EC.presence_of_element_located)
        return self

    def check_resolution_time(self):
        click(self.ID.chkResolutionTime, condition=EC.presence_of_element_located)
        return self

    def check_quality_of_work(self):
        click(self.ID.chkQualityOfWork, condition=EC.presence_of_element_located)
        return self

    def check_others(self):
        click(self.ID.chkOthers, condition=EC.presence_of_element_located)
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
        btnMyComplaints = ".file-complaint"
        rowComplaintCards = "xpath=//div[contains(@class,'complaint-card-wrapper')]"
        btnAddComplaintPlus = "button#mycomplaints-add"
        txtComment = "div#citizen-comment"
        btnSend = "svg[class='comment-send']"
        lblComplaintNumber = "xpath=//div[contains(@class,'complaint-complaint-number')]/*[text()='{}']"

    def open_compalint(self, complaint_number):
        elem = find(self.ID.lblComplaintNumber.format(complaint_number))
        scroll_into_view(elem)
        click(elem)
        return self

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
class ReopenComplaintPage(Page, UploadImageComponent):
    class ID:
        radReopenReason = "input#reopencomplaint-radio-button-0"
        txtTypeComplaint = "#reopencomplaint-comment-field"
        btnSubmit = "button#reopencomplaint-submit-action"

    def set(self, type_complaint):
        set(self.ID.txtTypeComplaint, type_complaint)
        return self

    def submit(self):
        click(self.ID.btnSubmit)
        return self


@PageObject
class ComplaintSummaryPage(Page):
    class ID:
        lblComplainNumber = "#complaint-details-complaint-number .label-text"
        lblComplaintStatus = "#complaint-details-current-status .label-text"
        lblSubmissionDate = "#complaint-details-submission-date .label-text"
        lblComplaintType = ".rainmaker-big-font"
        lblLocation = "#complaint-details-complaint-location .label-text"
        lblAdditionalComment = "#complaint-details-complaint-description .label-text"
        lblImageCount = ".complaint-detail-full-width img.img-responsive"

        btnRate = "xpath=// div[contains( @class ,'label-container ')]/*[text()='RATE']"
        btnReopen = "xpath=// div[contains( @class ,'label-container ')]/*[text()='RE-OPEN']"

    def get_compalint_type(self):
        return get(self.ID.lblComplaintType)

    def get_complaint_number(self):
        return get(self.ID.lblComplainNumber)

    def get_complaint_status(self):
        return get(self.ID.lblComplaintStatus)

    def get_complaint_submission_date(self):
        return get(self.ID.lblSubmissionDate)

    def get_no_of_image(self):
        return len(finds(self.ID.lblImageCount))

    def get_location(self):
        return get(self.ID.lblLocation)

    def get_additional_comments(self):
        return get(self.ID.lblAdditionalComment)

    def reopen_complaint(self):
        click(self.ID.btnReopen)
        return self

    def rate_complaint(self):
        click(self.ID.btnRate)
        return self
