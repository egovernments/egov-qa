from typing import List

from framework.common import PageObject, Page
from framework.selenium_plus import *
from ..components import *

__all__ = ['UnassignedComplaintsPage', 'ComplaintResolvedCommentPage', 'ComplaintResolvedPageSucessPage',
           'RequestReassignReasonPage',
           'ReAssignComplaintSuccessPage', 'GroHomePage', 'ComplaintSummaryPage']


class UnassignedComplaintsPage(Page):
    class ID:
        rowComplaintCards = "xpath=//div[contains(@class,'complaint-card-wrapper')]"
        txtComment = "textarea#citizen-comment"
        btnSendComment = "svg[class='comment-send']"
        btnAssign = "button#actionTwo"
        txtEmployeeSearch = "input#employee-search"
        lblAssignee = "id#23289"
        btnAssignLastMile = "//div[contains(text(), 'ASSIGN')]"

    def get_all_complaints(self) -> List[ComplainCardComponent]:
        cards = []
        for card in finds(self.ID.rowComplaintCards):
            cards.append(ComplainCardComponent(card))

        return cards

    def add_comments(self, employee_comment):
        set(self.ID.txtComment, employee_comment)
        return self

    def send_comment(self):
        click(self.ID.btnSendComment)
        return self

    def assign_complaint(self, assignee):
        click(self.ID.btnAssign)
        set(self.ID.txtEmployeeSearch, assignee)
        click(self.ID.lblAssignee)
        click(self.ID.btnAssignLastMile)


@PageObject
class ComplaintReassignPage(Page):
    class ID:
        # todo satish: add id for call,commenet box,send button
        btnReject = "button#actionOne"
        btnAssign = "button#actionTwo"
        txtComments = "textarea[id]"

    def reject(self):
        click(self.ID.btnReject)
        return self

    def assign(self):
        click(self.ID.btnReject)
        return self

    def set(self, comments):
        scroll_into_view(self.ID.txtComments)
        set(self.ID.txtComments, comments)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/employee/complaint-details?status=unassigned&reassign")
        return self


class ComplaintResolvedCommentPage(Page, UploadImageComponent):
    class ID:
        txtComment = "textarea#reopencomplaint-comment-field"
        btnMarkResolved = "button#complaint-resolved-submit"

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/employee/complaint-resolved")
        return self

    def set_comment(self, comment):
        set(self.ID.txtComment, comment)
        return self

    def click_mark_resolved(self):
        click(self.ID.btnMarkResolved)


@PageObject
class ComplaintResolvedPageSucessPage(Page):
    class ID:
        btncontinue = "button#resolvesuccess-continue"

    def click_continue(self):
        click(self.ID.btncontinue)


@PageObject
class RequestReassignReasonPage(Page):
    class REASONS:
        NOT_MY_DEPARTMENT = "Not my Department"
        NotMyJurisdiction = "Not my Jurisdiction"
        AbsentOrLeave = "Absent or Leave"
        NotAValidComplaint = "Not a valid Complaint"

    class ID:
        txtComment = "textarea#reopencomplaint-comment-field"
        clickRequestAssign = "button#reassigncomplaint-submit-action"
        radNotMyDepartment = "input#reopencomplaint-radio-button-0"
        radNotMyJurisdiction = "input#reopencomplaint-radio-button-1"
        radAbsentOrLeave = "input#reopencomplaint-radio-button-2"
        radNotAValidComplaint = "input#reopencomplaint-radio-button-3"

    radOption = {
        REASONS.NOT_MY_DEPARTMENT: ID.radNotMyDepartment,
        REASONS.NotMyJurisdiction: ID.radNotMyJurisdiction,
        REASONS.AbsentOrLeave: ID.radAbsentOrLeave,
        REASONS.NotAValidComplaint: ID.radNotAValidComplaint
    }

    def option(self, option):
        click(self.radOption[option], condition=EC.presence_of_element_located)
        return self

    def set_comment(self, comment):
        set(self.ID.txtComment, comment)
        return self

    def click_request_assign(self):
        click(self.ID.clickRequestAssign)
        return self


@PageObject
class ReAssignComplaintSuccessPage(Page):
    class ID:
        btnContinue = "button#reassignsuccess-continue"
        lblStatus = "span.thankyou-text"

    def get_status(self):
        return find(self.ID.lblStatus).text

    def click_continue(self):
        click(self.ID.btnContinue)


@PageObject
class GroHomePage(Page):
    class ID:
        btnUnassigned = ".unassigned-label-text"
        btnAssigned = ".assigned-label-text"
        lblComplaintNumber = "xpath=//div[contains(@class,'complaint-complaint-number')]/*[text()='{}']"

    def click_unassigned_complaint_list(self):
        click(self.ID.btnUnassigned)
        return self

    def click_assigned_complaint_list(self):
        click(self.ID.btnAssigned)
        return self

    def open_compalint(self, complaint_number):
        elem = find(self.ID.lblComplaintNumber.format(complaint_number))
        scroll_into_view(elem)
        click(elem)
        return self


@PageObject
class ComplaintSummaryPage(Page):
    class ID:
        lblComplainNumber = "#complaint-details-complaint-number .label-text"
        lblcomplaintStatus = "#complaint-details-current-status .label-text"
        lblSubmissionDate = "#complaint-details-submission-date .label-text"
        lblComplaintType = ".rainmaker-big-font"
        lblLocation = "#complaint-details-complaint-location .label-text"
        lblAdditionalComment = "#complaint-details-complaint-description .label-text"
        lblImageCount = ".complaint-detail-full-width img.img-responsive"
        btnRequestReAssign = "//div[text()='REQUEST RE-ASSIGN']"
        btnMarkResolved = "//div[text()='MARK RESOLVED']"
        btnReject = "//div[text()='REJECT']"
        btnAssign = "//div[text()='ASSIGN']"



    def get_compalint_type(self):
        return get(self.ID.lblComplaintType)

    def get_complaint_number(self):
        return get(self.ID.lblComplainNumber)

    def get_complaint_status(self):
        return get(self.ID.lblcomplaintStatus)

    def get_complaint_submission_date(self):
        return get(self.ID.lblSubmissionDate)

    def get_no_of_image(self):
        return len(finds(self.ID.lblImageCount))

    def get_location(self):
        return get(self.ID.lblLocation)

    def get_additional_comments(self):
        return get(self.ID.lblAdditionalComment)

    def click_reject(self):
        click(self.ID.btnReject)
        return self

    def click_assign(self):
        click(self.ID.btnAssign)
        return self

    def click_mark_resolved(self):
        click(self.ID.btnMarkResolved)
        return self

    def click_request_reassign(self):
        click(self.ID.btnRequestReAssign)
        return self




