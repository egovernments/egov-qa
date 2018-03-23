from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _AddComplaintPage(Page):
    class ID:
        txtComplaintType = ".addComplaint-complaint-type"

    def set_complaint_type(self, filter, complaint_type):
        click(self.ID.txtComplaintType)
        ComplaintTypePage.set(filter).select_complaint_type(complaint_type)



@PageObject
class _ComplaintTypePage(Page):
    class ID:
        txtComplaintTypeSearch = "input#complainttype-search"
        prmLblComplaintType = "xpath=//div[.='{}']"

    def set(self, complaint_filter):
        set(self.ID.txtComplaintTypeSearch, complaint_filter)
        return self

    def select_complaint_type(self, complaint_type):
        click(self.ID.prmLblComplaintType.format("complaint_type"))
        return self


ComplaintTypePage = _ComplaintTypePage()

AddComplaintPage = _AddComplaintPage()