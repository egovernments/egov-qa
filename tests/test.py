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
    goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/language-selection")
    language_selection = LanguageSelectionPage()
    language_selection.language("punjabi").language("hindi").language("english").submit()


def test_user_registration():
    goto("https://egov-micro-dev.egovernments.org/app/v3/citizen/user/register")
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()


def test_homepage():
    citizen_login()
    home_page = HomePage()
    home_page.new_complaint()
    home_page.click_my_complaint()


def test_profile_update(upload_photo=PROFILE_IMAGELIST):
    citizen_login()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    update = ProfilePage().update("Manjunatha S", "manju@ulb.in")
    ProfilePage().change_profile_picture(upload_photo)
    ProfilePage().save()
    name = get(ProfilePage().ID.txtProfileName)
    emailId = get(ProfilePage().ID.txtProfileEmailId)
    city = get(ProfilePage().ID.drpCity)
    assert ProfilePage().toaster_message() == "Profile is Successfully Updated"
    assert name == get(ProfilePage().ID.txtProfileName), "Verify name in applcation is correct"
    assert emailId == get(ProfilePage().ID.txtProfileEmailId), "Verify email in application is correct"
    assert city == get(ProfilePage().ID.drpCity), "Verfy city in application is correct"
    navigation = TopMenuNavigationComponent()
    navigation.back()
    logout()


def test_discard_changes_in_profile():
    citizen_login()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    ProfilePage().update("Sathish", "sathish@ulb.in")


def test_add_complaint(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE):
    # Create a new complaint
    create_new_complaint("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water", upload_photo)
    # Acknowledgement on successful complaint submission
    complaint_no = complaint_registration_number_recevied()
    print(complaint_no)
    # Search and view complaint created on My Complaints
    open_complaint(complaint_no)
    comment_on_complaint("Add comments")
    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()


def test_pgr_workflow(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE):
    # Create a new complaint
    create_new_complaint("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water", upload_photo)
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
    assign_open_complaint(complaint_no, "AntrikshKumar")
    logout()
    quit_driver()
    # Login as Last Mile Employee
    last_mile_employee_login("Antarikshkumar", "12345678")
    view_my_complaints(complaint_no)
    resolve_assigned_complaint(complaint_no)
    logout()
    quit_driver()


def test_view_my_complaint():
    gro_employee_login("Amardeep", "12345678")
    view_my_complaints("18/05/2018/000800")
    assign_open_complaint("18/05/2018/000800", "V Sudheer")


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):
    # Create a new complaint
    complaint_type = "Garbage"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Uneven"

    create_new_complaint(complaint_type, location, landmark, additional_details, upload_photo)


def test_citizen_should_file_complaint_with_two_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])


def test_add_more_than_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_FOUR)


def test_upload_other_than_image_format(citizen_login):  # error, Should give an error becasuse we are uploading pdf file
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=PDF_FILELIST)


def test_upload_a_large_size_file(citizen_login):  # it is uploading the file, it shuld give error mesaage
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=LARGE_IMAGELIST)
