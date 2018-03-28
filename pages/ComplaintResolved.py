from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _ComplaintResolved(Page):
    class ID:
        btnReOpen = "#complaint-details-timline-button"

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=resolved")
        return self

    def reOpen(self):
        click(self.ID.btnReOpen)
        return self

ComplaintResolved = _ComplaintResolved()