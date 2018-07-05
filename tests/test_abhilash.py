from framework.selenium_plus import *
from pages.flows.common import *


def test_homepage_displayed_after_sucessful_login(citizen_login): #done
    if exists(HomePage().ID.btnNewComplaints):
        assert True
    else:
        assert False

    pass


def test_selecting_city_from_dropdown_of_citizen_profile_page(citizen_login):
    drpCity = "span[id='pb.ludhiana']"
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    click(ProfilePage().ID.drpCity)
    click(drpCity)
    ProfilePage().save()


def test_image_no(citizen_login, images=DEFAULT_IMAGELIST_THREE):
    click("div.file-complaint")
    click("button#mycomplaints-add")
    complaint_details = "VAGAO YAAR JALDI"
    landmark_details = "HAIN WAHI HAI"
    location = "amritsar "
    complaint_type_search = "Stray"
    complaint_type_select = "Stray Dogs"

    citizen_create_new_complaint(
        location,
        complaint_details,
        landmark_details,
        complaint_type_search,
        complaint_type_select,
        images)

    complaint_no = ComplaintSubmittedPage().get_complaint_number()
    ComplaintSubmittedPage().click_continue()
    click("div.file-complaint")
    ComplaintCitizenSummaryPage().open_compalint(complaint_no)
    assert complaint_no == ComplaintCitizenSummaryPage().get_complaint_number(), "COMPAINT NO IS WRONG"
    assert ComplaintCitizenSummaryPage().get_no_of_image() == 3, "IMAGE NO IS NOT RIGHT"
    assert complaint_details == ComplaintCitizenSummaryPage.get_additional_details(), "ADDITIONAL DETAILS IS WRONG"
    assert landmark_details == ComplaintCitizenSummaryPage()