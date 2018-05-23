from functools import partial
from framework.common import PageObject, Page
from framework.selenium_plus import click, goto

__all__ = ['HomePage', 'LanguageSelectionPage']


@PageObject
class HomePage(Page):
    class ID:
        btnNewComplain = "div#home-new-complaint"
        btnOldComplain = "div#home-old-complaint"

    def new_complaint(self):
        click(self.ID.btnNewComplain)
        return self

    def my_complaints(self):
        click(self.ID.btnOldComplain)
        return self


@PageObject
class LanguageSelectionPage(Page):
    class LANGUAGES:
        ENGLISH = "english"
        HINDI = "hindi"
        PUNJABI = "punjabi"

    class ID:
        # TO-DO  add ID for language
        btnContinue = "button#continue-action"
        btnLanguageHindi = ".language-selection-card  div.button-toggle-container > button:nth-child(2)"
        btnLanguageEnglish = ".language-selection-card  div.button-toggle-container > button:nth-child(1)"
        btnLanguagePunjabi = ".language-selection-card  div.button-toggle-container > button:nth-child(3)"

    btnLanguage = {
        LANGUAGES.HINDI: ID.btnLanguageHindi,
        LANGUAGES.ENGLISH: ID.btnLanguageEnglish,
        LANGUAGES.PUNJABI: ID.btnLanguagePunjabi,
    }

    def language(self, language):
        click(self.btnLanguage[language])
        return self

    hindi = partial(language, language=LANGUAGES.HINDI)
    english = partial(language, language=LANGUAGES.ENGLISH)
    punjabi = partial(language, language=LANGUAGES.PUNJABI)

    def submit(self):
        click(self.ID.btnContinue)
        return self

    def navigate(self):
        goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/language-selection")
        return self
