from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _HomePage(Page):
    class ID:
        divNewComplain = "div#home-new-complaint"
        divOldComplain = "div#home-old-complaint"

    def new_complaint(self):
        click(self.ID.divNewComplain)
        return self

    def my_complaints(self):
        click(self.ID.divOldComplain)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen")
        return self


HomePage = _HomePage()
