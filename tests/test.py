from pytest import fixture

from environment import DEFAULT_IMAGELIST_ONE, DEFAULT_IMAGELIST_THREE, DEFAULT_IMAGELIST_TWO
from pages import *
from framework.selenium_plus import *
from pages.flows.common import *

# def pytest_sessionstart(session):
#     # setup_stuff
#
# def pytest_sessionfinish(session, exitstatus):
#     # teardown_stuff
from pages.employee.complains import ComplaintResolvedCommentPage, RequestReassignReasonPage
from pages.flows.common import create_new_complaint


@fixture(autouse=True, scope='session')
def my_fixture():
    # setup_stuff
    yield
    try:
        quit_driver()
        pass
    finally:
        pass
    # teardown_stuff



def test_new_complaint(login_citizen):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)

def test_otp_submission():  # done
    otp = OTPPage()
    otp.navigate()

    otp.set("12345").get_started()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():  # done
    comp = AddComplaintPage()
    comp.navigate()
    comp.set_complaint_type("Overflowing Garbage Bins")
    comp.set_location_by_address("Homigo Ant")
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_citizen_profile():  # error
    cp = CitizenProfilePage()
    cp.navigate().set("ABH", "satishkrgu95@gmail.com").set_city("Amritsar").save()


def test_complain_submitted():  # done
    complaint_subpage = ComplaintSubmittedPage()
    complaint_subpage.navigate()
    complaint_subpage.click_continue()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_my_complaints():  # done
    complaints = MyComplaintsPage()
    complaints.navigate()
    cards = complaints.get_all_complaints()
    card = cards[2]
    card.track_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=rejected"


def test_user_registration():  # done
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_language_selection():  # done
    ls = LanguageSelectionPage()
    ls.navigate()
    ls.language("punjabi").language("hindi").language("english").submit()

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register"


def test_homepage():  # done
    hp = HomePage()

    hp.navigate().new_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"

    hp.navigate().my_complaints()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/my-complaints"


def test_complaintfeedbackpage():  # done
    cf = ComplaintFeedbackPage()
    cf.navigate().star_click(4)
    cf.check_services().check_quality_of_work().check_resolution_time().check_others()
    cf.set("good to go").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/feedback"


def test_login():
    LoginPage().navigate().set("8792101399").submit()
    OTPPage().set("123456").get_started()
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"



    assert get_url() == "http://egov-micro-dev.egovernments.org/app/stv3/citizen/add-complaint"


def test_reopen_complaint():  # added uploading picture method #done
    photo1 = "/home/abh/Pictures/Screenshot from 2018-02-11 13-13-22.png"
    ReopenComplaintPage().navigate().set("Complaint not resolved").upload_images(photo1)
    ReopenComplaintPage().submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-submitted"


def test_navigation():  # DONE
    LoginPage().navigate().set("9999999999").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"
    OTPPage().set("12345").get_started()
    BottomMenuComponent().info().payments().complaints().home()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    TopMenuNavigationComponent().back()
    TopMenuNavigationComponent.ham()

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"

    # this test is for verifying navigation


def test_profile():  # done
    LoginPage().navigate().set("9999999999").submit()
    OTPPage().set("12345").get_started()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    ProfilePage().update("Singh", "def@ulb.in")
    ProfilePage().photo_remove()
    ProfilePage().save()
    TopMenuNavigationComponent().back()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_complaint_resolved_comment():  # done
    resolved = ComplaintResolvedCommentPage()
    resolved.navigate().upload_images("/home/abh/Pictures/Screenshot from 2018-02-11 13-13-22.png")
    resolved.set_comment("GOTTYA").click_mark_resolved()





def test_new_complaint_by_plus_icon(login_citizen):
    create_new_complaint_by_plus_icon("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs",
                                      "landmarkdetail", True)



def test_add_complaint(citizen_login):
    # Create a new complaint
    add_complaint_details(
        "Water Body",
        "Amritsar, Punjab, India ",
        "Street end",
        "Leakage of water",
        "D:/Repositories/rainmaker_automation/egov-qa/assets/images/image1.jpg"
    )
    # Acknowledgement on successful complaint submission
    complaintNo = complaint_successful_page()
    print(complaintNo)

    # Search and view complaint created on My Complaints
    view_my_complaints(complaint_number)

    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()


def test_complaint_register_to_resolve(login_citizen):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)
    complain_number = ComplaintSubmittedPage().get_complaint_number()
    #logout_citizen()
    login_gro("9090909010", "murali@1993")


def test_request_reassign_reason():  # done
    reassign_reason = RequestReassignReasonPage()
    reassign_reason.navigate().option(reassign_reason.REASONS.NOT_MY_DEPARTMENT) \
        .option("Not my Jurisdiction") \
        .option("Absent or Leave") \
        .option("Not a valid Complaint") \
        .set_comment("YO") \
        .click_request_assign()


def test_registering_with_already_registered_mobile_no():  # error
    LanguageSelectionPage().navigate().language("hindi").submit()
    rp = RegistrationPage()
    rp.navigate().set("9999999999", "ABH", "patiala").submit()
    rp.navigate().set("9999999999", "ABH", "patiala").submit()


def test_add_more_than_three_image():  # suscess
    photo1 = "/home/abh/Pictures/Screenshot from 2018-02-11 13-13-22.png"
    photo2 = "/home/abh/Pictures/Screenshot from 2018-03-29 14-51-09.png"
    photo3 = "/home/abh/Pictures/Screenshot from 2018-03-29 14-51-20.png"
    AddComplaintPage().navigate().upload_images(photo1, photo2, photo3)
    AddComplaintPage().upload_images(photo1)


def test_upload_other_than_image_format():  # error, Should give an error becasuse we are uploading pdf file
    pdf1 = "/home/abh/Documents/HDFC Bank Credit Card.pdf"
    photo1 = "/home/abh/Pictures/Screenshot from 2018-02-11 13-13-22.png"
    photo2 = "/home/abh/Pictures/Screenshot from 2018-03-29 14-51-09.png"
    AddComplaintPage().navigate().upload_images(photo1, photo2, pdf1)


def test_upload_a_large_size_file():  # field , it is uploading the file, it shuld give error mesaage
    large_file = "/home/abh/Desktop/shong's party/IMG_8844.JPG"
    AddComplaintPage().navigate().upload_images(large_file)


def test_select_location_by_typing_address():
    AddComplaintPage().navigate().set_location_by_address("HSR Layout, Bengaluru, Karnataka, India")


def test_flow_check_1():
    RegistrationPage().navigate().login()
    LoginPage().set(9337682030).submit()
    OTPPage().set(123456).get_started()
    HomePage().new_complaint()
    AddComplaintPage().set_location_by_address("amritsar ")
    AddComplaintPage().set_complaint_type("Stray Dogs", "Stray")
    photo1 = "/home/abh/Pictures/Screenshot from 2018-02-11 13-13-22.png"
    photo2 = "/home/abh/Pictures/Screenshot from 2018-03-29 14-51-09.png"
    photo3 = "/home/abh/Pictures/Screenshot from 2018-03-29 14-51-20.png"
    AddComplaintPage().upload_images(photo1, photo2, photo3)
    AddComplaintPage().set_complaint_details("VAGAO YAAR JALDI")
    AddComplaintPage().set_landmark_details("HAIN WAHI HAI")
    # AddComplaintPage().click_submit()
    # print(ComplaintSubmittedPage().get_complaint_number())
    # ComplaintSubmittedPage().click_continue()


def test_citizen_should_file_complaint_with_one_image(login_citizen, images=DEFAULT_IMAGELIST_ONE):
    complaint_details = "VAGAO YAAR JALDI"
    landmark_details = "HAIN WAHI HAI"
    location = "amritsar "
    complaint_type_search = "Stray"
    complaint_type_select = "Stray Dogs"
    HomePage().new_complaint()
    create_new_complaint(
        location,
        complaint_details,
        landmark_details,
        complaint_type_search,
        complaint_type_select,
        images)


def test_citizen_should_file_complaint_with_two_image(login_citizen):
    test_citizen_should_file_complaint_with_one_image(login_citizen, DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(login_citizen):
    test_citizen_should_file_complaint_with_one_image(login_citizen, DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_images(login_citizen):
    test_citizen_should_file_complaint_with_one_image(login_citizen, [])
    #assign_to_last_mile_employee()
    # gro_reject_complaint()

    # reassign_request_last_mile_employee()

    # Read complaint #
    # assert complaint is not blank




