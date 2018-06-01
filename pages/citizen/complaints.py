from typing import List

from framework.common import PageObject, Page
from framework.selenium_plus import *
from pages.components.common import TimelineCardComponent
from ..components import *

__all__ = ['AddComplaintPage', 'ComplaintFeedbackPage', 'ComplaintSubmittedPage', 'MyComplaintsPage',
           'ReopenComplaintPage', 'ComplaintCitizenSummaryPage', 'ComplaintReopenedPage', 'FeedbackSubmittedPage',
           'ComplaintTimelinePage', 'ComplaintCommentCard']


@PageObject
class AddComplaintPage(Page, UploadImageComponent, LocationComponent, ComplaintTypeComponent):
    class ID:
        btnComplaints = "button#complaints-button"
        txtLocation = "input#address"
        txtComplaintDetails = "textarea[id='additional details']"
        txtComplaintType = "input#complaint-type"
        txtLandmarkDetails = "input#landmark"
        btnSubmit = "button#addComplaint-submit-complaint"
        btnPlusIcon = "button#mycomplaints-add"

    def complaints_icon(self):
        click(self.ID.btnComplaints)
        return self

    def set_location_by_address(self, address, result_index=0):
        click(self.ID.txtLocation)
        time.sleep(3)
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

    def click_on_plus_icon(self):
        click(self.ID.btnPlusIcon)
        return self

    def submit(self):
        click(self.ID.btnSubmit)
        return self


@PageObject
class ComplaintFeedbackPage(Page):
    class Feedback:
        SERVICES = "Services"
        RESOLUTION_TIME = "Resolution Time"
        QUALITY_OF_WORK = "Quality of Work"
        OTHERS = "Others"

    class ID:
        prmStarRating = "span#feedback-ratings{}"
        chkServices = "input#feedback-checkbox0"
        chkResolutionTime = "input#feedback-checkbox1"
        chkQualityOfWork = "input#feedback-checkbox2"
        chkOthers = "input#feedback-checkbox3"
        txtFeedbackComment = "textarea#feedback-comments"
        btnFeedbackSubmit = "button#feedback-submit-action"
        btnGoToHome = "button#feedback-acknowledgement"

    FEEDBACK_REASON = {
        Feedback.SERVICES: ID.chkServices.format("Services"),
        Feedback.QUALITY_OF_WORK: ID.chkQualityOfWork.format("Resolution Time"),
        Feedback.RESOLUTION_TIME: ID.chkResolutionTime.format("Quality of Work"),
        Feedback.OTHERS: ID.chkOthers.format("Others")
    }

    def set(self, feedback_comment):
        set(self.ID.txtFeedbackComment, feedback_comment)
        return self

    def star_click(self, a):
        click(self.ID.prmStarRating.format(int(a) - 1), condition=EC.presence_of_element_located)
        return self

    def reason_for_feedback(self, choice):
        click(self.FEEDBACK_REASON[choice], condition=EC.presence_of_element_located)
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
        btnMyComplaints = "button#complaints-button"
        rowComplaintCards = "xpath=//div[contains(@class,'complaint-card-wrapper')]"
        btnAddComplaintPlus = "button#mycomplaints-add"
        txtComment = "textarea#citizen-comment"
        btnSend = "svg[class='comment-send']"
        lblComplaintNumber = "xpath=//div[contains(@class,'complaint-complaint-number')]/*[text()='{}']"
        prmComplaintCard = "xpath=//div[contains(@class,'complaints-card-main-cont')][.//div[contains(@class,'complaint-complaint-number')]/div[text()='{}']]"

    def open_compalint(self, complaint_number):
        elem = find(self.ID.lblComplaintNumber.format(complaint_number))
        scroll_into_view(elem)
        click(elem)
        return self

    def get_complaint_card(self, complaint_number) -> ComplainCardComponent:
        return ComplainCardComponent(find(self.ID.prmComplaintCard.format(complaint_number)))

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
    class Reason:
        NO_WORK_WAS_DONE = "No work was done"
        ONLY_PARTIAL_WORK_WAS_DONE = "Only partial work was done"
        EMPLOYEE_DID_NOT_TURN_UP = "Employee did not turn up"
        NO_PERMANENT_SOLUTION = "No permanent solution"

    class ID:
        prmRadReopenReason = "input[type='radio'][value='{}']"
        txtTypeComplaint = "#reopencomplaint-comment-field"
        btnSubmit = "button#reopencomplaint-submit-action"
        btnGoToHome = "button#success-message-acknowledgement"

    REOPEN_REASON = {
        Reason.NO_WORK_WAS_DONE: ID.prmRadReopenReason.format("No work was done"),
        Reason.ONLY_PARTIAL_WORK_WAS_DONE: ID.prmRadReopenReason.format("Only partial work was done"),
        Reason.EMPLOYEE_DID_NOT_TURN_UP: ID.prmRadReopenReason.format("Employee did not turn up"),
        Reason.NO_PERMANENT_SOLUTION: ID.prmRadReopenReason.format("No permanent solution"),
    }

    def reason_for_reopen(self, choice):
        click(self.REOPEN_REASON[choice])

    def set(self, type_complaint):
        set(self.ID.txtTypeComplaint, type_complaint)
        return self

    def submit(self):
        click(self.ID.btnSubmit)
        return self


@PageObject
class ComplaintCitizenSummaryPage(Page):
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


@PageObject
class ComplaintReopenedPage(Page):
    class ID:
        lblAcknowledgement = ".thankyou-text .label-text"
        btnGoToHome = "#success-message-acknowledgement"

    def get_successful_message(self):
        return get(self.ID.lblAcknowledgement)

    def go_to_home(self):
        click(self.ID.btnGoToHome)


@PageObject
class ComplaintTimelinePage(Page):
    class ID:
        timelineCard = ".complaint-timeline-content-section"

    def get_all_timeline_card(self) -> List[TimelineCardComponent]:
        timeline = []
        for timeline1 in finds(self.ID.timelineCard):
            timeline.append(TimelineCardComponent(timeline1))
        return timeline


@PageObject
class FeedbackSubmittedPage(Page):
    class ID:
        btnContinue = "#feedback-acknowledgement"

    def click_continue(self):
        click(self.ID.btnContinue)
        return self

@PageObject
class ComplaintCommentCard(Page):
    class ID:
        lblComments = ".complaint-details-comments-section .label-text"

    def get_all_comments(self):
        comments = finds(self.ID.lblComments)
        all_comments = list(map(lambda e: e.text, comments))
        return all_comments
