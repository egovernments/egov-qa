from framework.common import PageObject, Page
from framework.selenium_plus import *

__all__ = ['ComplaintUnassignPage', 'ComplaintReassignPage']


@PageObject
class ComplaintUnassignPage(Page):
    class ID:
        # todo satish: add id for call,commenet box,send button
        btnReject = "button#actionOne"
        btnAssign = "button#actionTwo"

    def reject(self):
        click(self.ID.btnReject)
        return self

    def assign(self):
        click(self.ID.btnReject)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/employee/complaint-details?status=unassigned")
        return self


@PageObject
class ComplaintReassignPage(Page):
    class ID:
        # todo satish: add id for call,commenet box,send button
        btnReject = "button#actionOne"
        btnAssign = "button#actionTwo"
        txtComments = "textarea"

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
