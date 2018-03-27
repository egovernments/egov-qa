from framework.common import Page, PageObject
from framework.selenium_plus import *


@PageObject
class _ComplaintFeedbackPage(Page):
    class ID:
        prmStarRating = "span#feedback-ratings{}"
        chkServices = "input#feedback-checkbox0"
        chkResolutionTime = "input#feedback-checkbox1"
        chkQualityOfWork = "input#feedback-checkbox2"
        chkOthers = "input#feedback-checkbox3"
        txtFeedbackComment = "textarea#feedback-comments"
        btnFeedbackSubmit = "button#feedback-submit"

    def set(self, feedback_comment):
        set(self.ID.txtFeedbackComment, feedback_comment)
        return self

    def star_click(self, a):
        print(a)
        click(self.ID.prmStarRating.format(int(a) - 1))
        return self

    def check_services(self):
        click(self.ID.chkServices)
        return self

    def check_resolution_time(self):
        click(self.ID.chkResolutionTime)
        return self

    def check_quality_of_work(self):
        click(self.ID.chkQualityOfWork)
        return self

    def check_others(self):
        click(self.ID.chkOthers)
        return self

    def submit(self):
        click(self.ID.btnFeedbackSubmit)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/feedback")
        return self


ComplaintFeedbackPage = _ComplaintFeedbackPage()
