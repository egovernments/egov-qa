from framework.selenium_plus import *
from pages.flows.common import *


def test_homepage_displayed_after_sucessful_login(login_citizen):
    if exists(HomePage().ID.btnNewComplain):
        assert True
    else:
        assert False

    pass

def test_upadate_profile(login_citizen):
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    ProfilePage().change_profile_picture()
    ProfilePage().profile_upload_image(DEFAULT_IMAGELIST_ONE)
    ProfilePage().set_email_id("abhilash.seth@gmail.com").set_name("Abhilash Seth").set_city("Am")
    ProfilePage().save()

def test_discard_changes_in_profile(login_citizen):
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    name = get(ProfilePage().ID.txtProfileName)
    emailId = get(ProfilePage().ID.txtProfileEmailId)
    city = get(ProfilePage().ID.drpCity)
    ProfilePage().change_profile_picture()
    ProfilePage().profile_upload_image(DEFAULT_IMAGELIST_ONE)
    ProfilePage().set_email_id("YO.YO@gmail.com").set_name("YO YO").set_city("Pa").click_back()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    assert name == get(ProfilePage().ID.txtProfileName), "Verify name in applcation is correct"
    assert emailId == get(ProfilePage().ID.txtProfileEmailId), "Verify email in application is correct"
    assert city == get(ProfilePage().ID.drpCity), "Verfy city in application is correct"


def test_uploading_large_size_image_for_profile_picture(login_citizen):
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    ProfilePage().change_profile_picture()
    ProfilePage().profile_upload_image(LARGE_SIZE_IMAGE)

def test_selecting_city_from_dropdown_of_citizen_profile_page(login_citizen):
    drpCity = "span[id='pb.ludhiana']"
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    click(ProfilePage().ID.drpCity)
    click(drpCity)
    ProfilePage().save()

def test_image_no(login_citizen, images=DEFAULT_IMAGELIST_THREE):
    click("div.file-complaint")
    click("button#mycomplaints-add")
    complaint_details = "VAGAO YAAR JALDI"
    landmark_details = "HAIN WAHI HAI"
    location = "amritsar "
    complaint_type_search = "Stray"
    complaint_type_select = "Stray Dogs"

    create_new_complaint(
        location,
        complaint_details,
        landmark_details,
        complaint_type_search,
        complaint_type_select,
        images)

    complaint_no = ComplaintSubmittedPage().get_complaint_number()
    ComplaintSubmittedPage().click_continue()
    click("div.file-complaint")
    ComplaintSummaryPage().open_compalint(complaint_no)
    assert complaint_no == ComplaintSummaryPage().get_complaint_number(), "COMPAINT NO IS WRONG"
    assert ComplaintSummaryPage().get_no_of_image() == 3, "IMAGE NO IS NOT RIGHT"
    assert complaint_details == ComplaintSummaryPage.get_additional_details(), "ADDITIONAL DETAILS IS WRONG"
    assert landmark_details == ComplaintSummaryPage().





