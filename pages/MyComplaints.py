from framework.common import Page, PageObject
from framework.selenium_plus import *
from typing import List


@PageObject
class _ComplainCardPage(Page):
    class ID:
        lblComplaintHeader = "span.complaint-header"

        # todo:  fixed it in Status we are getting "OPEN" and "Complaint Re-assigned to Dharmendra Pal" ,but we should get "OPEN"
        lblComplaintStatus = "span.complaint-status-text"
        lblComplaintDate = "div.complaint-date-cont"
        lblComplaintNo = "div.complaint-number-cont"
        # todo :put id for the button track
        btnTrack = "div.complaint-track-button-cont button"
        btnMycomplaintAdd = "button#mycomplaints-add"

    def __init__(self, container=None):
        self.container = container

    def get_complaint_header(self):
        return find(self.ID.lblComplaintHeader, context=self.container).text

    def get_complaint_status(self):
        return find(self.ID.lblComplaintStatus, context=self.container).text

    def get_complaint_date(self):
        return find(self.ID.lblComplaintDate, context=self.container).text

    def get_complaint_no(self):
        return find(self.ID.lblComplaintNo, context=self.container).text

    def track_complaint(self):
        elem = find(self.ID.btnTrack, context=self.container)
        execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

@PageObject
class _MyComplaintsPage(Page):
    class ID:
        rowComplaintCards = "xpath=//div[contains(@class,'complaint-card-wrapper')]"
        btnAddComplaint = "button#mycomplaints-add"

    def get_all_complaints(self) -> List[_ComplainCardPage]:
        cards = []
        for card in finds(self.ID.rowComplaintCards):
            cards.append(_ComplainCardPage(card))

        return cards

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/my-complaints")

    def add_complaint(self):
        click(self.ID.btnAddComplaint)


MyComplaintsPage = _MyComplaintsPage()
