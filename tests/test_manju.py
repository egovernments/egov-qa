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


def test_my_complaints():
    citizen_login()
    complaints = MyComplaintsPage()
    # complaints.navigate()

    cards = complaints.get_all_complaints()
    card = cards[2]
    card.track_complaint()


def test_language_selection():
    language_selection = LanguageSelectionPage()
    language_selection.navigate()
    language_selection.language("punjabi").language("hindi").language("english").submit()


def test_user_registration():
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()


def test_profile_update():
    citizen_login()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    ProfilePage().update("Manjunatha S", "manju@ulb.in")
    ProfilePage().change_photo()
    # ProfilePage().save()
    assert ProfilePage().save() == "Profile is Successfully Updated"
    navigation = TopMenuNavigationComponent()
    navigation.back()
    logout()


def test_discard_changes_in_profile():
    citizen_login()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    ProfilePage().update("Sathish", "sathish@ulb.in")


def test_homepage():
    citizen_login()
    home_page = HomePage()
    home_page.new_complaint()
    home_page.navigate().click_my_complaint()


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
    resolve_assigned_complaint(complaint_no, "Complaint Resolved")
    logout()
    quit_driver()


def test_view_my_complaint():
    gro_employee_login("Amardeep", "12345678")
    view_my_complaints("18/05/2018/000800")
    assign_open_complaints("18/05/2018/000800", "Complaint Assigned", "V Sudheer")


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):
    # Create a new complaint
    complaint_type = "Water Body"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Leakage of water"

    add_complaint_details(complaint_type, location, landmark, additional_details, upload_photo)


def test_citizen_should_file_complaint_with_two_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])