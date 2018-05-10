from framework.selenium_plus import *
from pages.flows.common import *


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
        quit_driver()
        pass
    finally:
        pass
    # teardown_stuff


def test_otp_submission():
    otp = OTPPage()
    otp.navigate()

    otp.set("12345").get_started()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():
    comp = AddComplaintPage()
    comp.navigate()
    comp.set_complaint_type("Overflowing Garbage Bins")
    comp.set_location_by_address("Homigo Ant")
    photo1 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    photo2 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    photo3 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"

    comp.upload_images(photo1, photo2, photo3)
    comp.remove_image_2()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_citizen_profile():
    cp = CitizenProfilePage()
    cp.navigate().set("ABH", "satishkrgu95@gmail.com").set_city("Amritsar").save()


def test_complain_submitted():
    complaint_subpage = ComplaintSubmittedPage()
    complaint_subpage.navigate()
    complaint_subpage.click_continue()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_my_complaints():
    complaints = MyComplaintsPage()
    complaints.navigate()
    cards = complaints.get_all_complaints()
    card = cards[2]
    card.track_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=rejected"


def test_user_registration():
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_language_selection():
    ls = LanguageSelectionPage()
    ls.navigate()
    ls.language("punjabi").language("hindi").language("english").submit()

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register"


def test_homepage():
    hp = HomePage()

    hp.navigate().new_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"

    hp.navigate().select_my_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/my-complaints"


def test_complaint_feedback():
    cf = ComplaintFeedbackPage()
    cf.navigate().star_click(4)
    cf.check_services().check_quality_of_work().check_resolution_time().check_others()
    cf.set("good to go").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/feedback"


def test_login():
    LoginPage().navigate().set("8792101399").submit()
    OTPPage().set("123456").get_started()
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_reopen_complaint():
    ReopenComplaintPage().navigate().set("Complaint not resolved").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-submitted"


def test_navigation():
    LoginPage.navigate().set("9999999999").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    BottomMenuComponent().info().payments().complaints().home()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    TopMenuNavigationComponent().back()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"

    # this test is for verifying navigation


def test_profile():
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


def test_register_mobile_less10():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set(876543, 'satish', 'Amritsar')
    reg.submit()
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_register_mobile_greater10():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set(87654398887773333, 'satish', 'Amritsar')
    reg.submit()
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_register_mobile_with_specialchar():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set("876543Lhkjh", 'satish', 'Amritsar')
    reg.submit()

    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_duplicate_mobile_number():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set("8792101399", 'satish', 'Amritsar').submit()
    reg.navigate().set("8792101399", 'satish', 'Amritsar').submit()


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


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):
    # Create a new complaint
    complaint_type = "Water Body"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Leakage of water"

    add_complaint_details(
        complaint_type,
        location,
        landmark,
        additional_details,
        upload_photo
    )


def test_citizen_should_file_complaint_with_two_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])
