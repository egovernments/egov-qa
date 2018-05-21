from framework.common import PageObject, Page
from framework.selenium_plus import *
from ..components import *

__all__ = ['ComplaintResolvedCommentPage', 'ComplaintResolvedPageSucessPage', 'RequestReassignReasonPage',
           'ReAssignComplaintSuccessPage']


@PageObject
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
    #
    # def navigate(self):
    #     goto("http://egov-micro-dev.egovernments.org/app/v3/employee/resolve-success")


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

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/employee/reassign-complaint")
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

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/employee/reassign-success")

    def get_status(self):
        return find(self.ID.lblStatus).text

    def click_continue(self):
        click(self.ID.btnContinue)
