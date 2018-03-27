from framework.common import Page, PageObject

from framework.selenium_plus import *


@PageObject
class _BottomMenuPage(Page):
    class ID:
        btnHome = "div.bottom-navigation>button:nth-child(1)"  # todo, this filed required id
        btnInfo = "div.bottom-navigation>button:nth-child(2)"  # todo, this filed required id
        btnPayments = "div.bottom-navigation>button:nth-child(3)"  # todo, this filed required id
        btnComplaints = "div.bottom-navigation>button:nth-child(4)"  # todo, this filed required id

    def home(self):
        click(self.ID.btnHome)
        return self

    def info(self):
        click(self.ID.btnInfo)
        return self

    def payments(self):
        click(self.ID.btnPayments)
        return self

    def complaints(self):
        click(self.ID.btnComplaints)
        return self


@PageObject
class _TopMenuPage(Page):
    class ID:
        btnHam = "div:nth-child(1)>div:nth-child(1)>button"  # todo, this filed required id
        btnBackNavigate = "#back-navigator"

    def ham(self):
        click(self.ID.btnHam)
        return self

    def back(self):
        click(self.ID.btnBackNavigate)
        return self


BottomMenuPage = _BottomMenuPage()
TopMenuPage = _TopMenuPage()
