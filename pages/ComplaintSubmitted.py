from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _ComplaintSubmittedPage(Page):
    class ID:
        btnContinue = "button#complaint-submitted-continue"
        # todo:  fixed it
        lblComplain = "div.complaint-submitted-boldlabel"

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-submitted")
        return self

    def get_complaint_number(self):
        return find(self.ID.lblComplain).text

    def click_continue(self):
        click(self.ID.btnContinue)


ComplaintSubmittedPage = _ComplaintSubmittedPage()
