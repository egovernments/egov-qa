from framework.common import PageObject, Page
from framework.selenium_plus import *


@PageObject
class _ReopenComplaintPage(Page):
    class ID:
        radReopenReason = "input#reopencomplaint-radio-button-0"
        txtTypeComplaint = "#reopencomplaint-comment-field"
        btnSubmit = "#reopencomplaint-submit-action"

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/reopen-complaint")
        return self

    def set(self, type_complaint):
        set(self.ID.txtTypeComplaint, type_complaint)
        return self

    def submit(self):
        click(self.ID.btnSubmit)
        return self


ReopenComplaintPage = _ReopenComplaintPage()
