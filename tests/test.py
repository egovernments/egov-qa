from framework.selenium_plus import *
from pages.flows.common import *
from pages.employee.complains import ComplaintResolvedCommentPage, RequestReassignReasonPage


# def pytest_sessionstart(session):
#     # setup_stuff
#
# def pytest_sessionfinish(session, exitstatus):
#     # teardown_stuff


@fixture(autouse=True, scope='session')
def my_fixture():
    # setup_stuff
    yield
    try:
        # quit_driver()
        pass
    finally:
        pass
    # teardown_stuff


@fixture
def test_citizen_login():
    citizen_login()


@fixture
def test_gro_login():
    gro_employee_login()


@fixture
def test_last_mile_employee_login():
    last_mile_employee_login()


@fixture
def test_logout(login_citizen):
    logout()


def test_profile():
    citizen_login()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    ProfilePage().update("Manjunatha S ", "manju@ulb.in")
    # ProfilePage().photo_remove()
    # ProfilePage().save()
    assert ProfilePage().save() == "Profile is Successfully Updated"
    navigation = TopMenuNavigationComponent()
    navigation.back()
    logout()


def test_homepage():
    citizen_login()
    home_page = HomePage()
    home_page.new_complaint()
    home_page.navigate().click_my_complaint()


def test_citizen_profile():  # error
    cp = CitizenProfilePage()
    cp.navigate().set("ABH", "satishkrgu95@gmail.com").set_city("Amritsar").save()


def test_complain_submitted():  # done
    complaint_subpage = ComplaintSubmittedPage()
    complaint_subpage.navigate()
    complaint_subpage.click_continue()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_my_complaints():  # done
    citizen_login()
    complaints = MyComplaintsPage()
    # complaints.navigate()

    cards = complaints.get_all_complaints()
    card = cards[2]
    card.track_complaint()

def test_user_registration():  # done
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()


def test_language_selection():
    language_selection = LanguageSelectionPage()
    language_selection.navigate()
    language_selection.language("punjabi").language("hindi").language("english").submit()


def test_complaint_feedback():
    complaint_feedback_page = ComplaintFeedbackPage()
    complaint_feedback_page.navigate().star_click(4)
    complaint_feedback_page.check_services().check_quality_of_work().check_resolution_time().check_others()
    complaint_feedback_page.set("Good to go").submit()

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

def test_complaint_resolved_comment():  # done
    resolved = ComplaintResolvedCommentPage()
    resolved.navigate().upload_images("/home/abh/Pictures/Screenshot from 2018-02-11 13-13-22.png")
    resolved.set_comment("GOTTYA").click_mark_resolved()


def test_register_mobile_less10():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set(876543, 'satish', 'Amritsar')
    registration.submit()


def test_register_mobile_greater10():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set(87654398887773333, 'satish', 'Amritsar')
    registration.submit()


def test_register_mobile_with_specialchar():
    LanguageSelectionPage().navigate().language("english").submit()
    registration = RegistrationPage()
    registration.navigate().set("876543Lhkjh", 'satish', 'Amritsar')
    registration.submit()


def test_add_complaint(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE):
    # Create a new complaint
    add_complaint_details("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water", upload_photo)
    # Acknowledgement on successful complaint submission
    complaint_no = complaint_registration_number_recevied()
    print(complaint_no)
    # Search and view complaint created on My Complaints
    view_my_complaints(complaint_no)
    comment_on_complaint("Add comments")
    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()


def test_pgr_workflow(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE):
    # Create a new complaint
    add_complaint_details("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water", upload_photo)
    # Acknowledgement on successful complaint submission
    complaint_no = complaint_registration_number_recevied()
    print(complaint_no)
    # Search and view complaint created on My Complaints
    view_my_complaints(complaint_no)
    comment_on_complaint("Add comments")
    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()
    # Login as GRO
    gro_employee_login("Amardeep", "12345678")
    view_my_complaints(complaint_no)
    assign_open_complaints(complaint_no, "Complaint Assigned", "LastMileEmployee")
    logout()
    quit_driver()
    # Login as Last Mile Employee
    last_mile_employee_login("Antarikshkumar", "12345678")
    view_my_complaints(complaint_no)
    # resolve_assigned_complaint(complaint_o, "Complaint Resolved")
    logout()
    quit_driver()


def test_view_my_complaint():
    gro_employee_login("Amardeep", "12345678")
    view_my_complaints("18/05/2018/000800")
    assign_open_complaints("18/05/2018/000800", "Complaint Assigned", "V Sudheer")


def test_complaint_register_to_resolve(login_citizen):
    add_complaint_details("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)
    complain_number = ComplaintSubmittedPage().get_complaint_number()
    # logout_citizen()
    gro_employee_login("9090909010", "murali@1993")


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


def test_citizen_should_file_complaint_with_one_image(login_citizen, images=DEFAULT_IMAGELIST_ONE):
    complaint_details = "VAGAO YAAR JALDI"
    landmark_details = "HAIN WAHI HAI"
    location = "amritsar "
    complaint_type_search = "Stray"
    complaint_type_select = "Stray Dogs"
    HomePage().new_complaint()
    add_complaint_details(
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