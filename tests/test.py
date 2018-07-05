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


def test_my_complaints():  # TODO
    citizen_login()
    complaints = MyComplaintsPage()
    # complaints.navigate()

    cards = complaints.get_all_complaints()
    card = cards[2]
    card.track_complaint()


# TODO: as of now below test case is hardcoded for dev, need to implement for other env
"""

def test_language_selection():
    goto("http://egov-micro-dev.egovernments.org/app/v3/citizen/user/language-selection")
    language_selection = LanguageSelectionPage()
    language_selection.language("punjabi").language("hindi").language("english").submit()


def test_user_registration():
    goto("https://egov-micro-dev.egovernments.org/app/v3/citizen/user/register")
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()
"""


def test_homepage():  # done
    citizen_login()
    home_page = HomePage()
    home_page.new_complaint()
    home_page.navigate()
    home_page.my_complaints()


def test_profile_update(upload_photo=PROFILE_IMAGELIST):  # done
    citizen_login()
    TopMenuNavigationComponent().user_profile()
    LoginPage().profile()
    profile = ProfilePage()
    profile.update("Manjunatha S", "manju@ulb.in")
    profile.change_profile_picture(upload_photo)
    profile.save()
    name = get(profile.ID.txtProfileName)
    emailId = get(profile.ID.txtProfileEmailId)
    city = get(profile.ID.drpCity)
    assert profile.toaster_message() == "Profile is Successfully Updated"
    assert name == get(profile.ID.txtProfileName), "Verify name in applcation is correct"
    assert emailId == get(profile.ID.txtProfileEmailId), "Verify email in application is correct"
    assert city == get(profile.ID.drpCity), "Verfy city in application is correct"
    logout()


def test_discard_changes_in_profile():  # done
    citizen_login()
    navigate = TopMenuNavigationComponent()
    loginpage = LoginPage()
    profile = ProfilePage()

    navigate.user_profile()
    loginpage.profile()
    profile.update("Sathish", "sathish@ulb.in")
    HomePage().navigate()
    navigate.user_profile()
    loginpage.profile()
    assert "Sathish" != get(profile.ID.txtProfileName), "Verify name in application is correct"
    assert "sathish@ulb.in" != get(profile.ID.txtProfileEmailId), "Verify email in application is correct"


def test_add_complaint(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE):  # done
    # Create a new complaint
    complaint = citizen_create_new_complaint("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water",
                                             upload_photo, True,
                                             True)

    # Acknowledgement on successful complaint submission

    print("COMPLAINT NO : " + complaint["complaint_number"])
    print("STATUS : " + complaint["status"])
    HomePage().navigate()
    logout()


def test_pgr_workflow(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE):  # done
    # Create a new complaint
    complaint = citizen_create_new_complaint("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water",
                                             upload_photo)
    # Navigate to the home page and logout
    HomePage().navigate()
    logout()
    quit_driver()

    # Login as GRO
    gro_employee_login("ShivaG", "12345678", "Amritsar")
    MyComplaintsPage().open_complaint(complaint["complaint_number"])
    assign_open_complaint(complaint["complaint_number"], "Palash")
    logout()
    quit_driver()

    # Login as Last Mile Employee
    last_mile_employee_login("PalashS", "12345678", "Amritsar")
    resolve_assigned_complaint(complaint["complaint_number"])
    logout()
    quit_driver()


def test_view_my_complaint():  # done
    gro_employee_login("ShivaG", "12345678", "Amritsar")
    MyComplaintsPage().open_complaint("02/07/2018/001119")
    assign_open_complaint("02/07/2018/001119", "Palash")


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):  # done
    # Create a new complaint
    complaint_type = "Garbage"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Uneven"

    citizen_create_new_complaint(complaint_type, location, landmark, additional_details, upload_photo, True, True)


def test_citizen_should_file_complaint_with_two_image(citizen_login):  # done
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):  # done
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):  # done
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])


def test_add_more_than_three_image(citizen_login):  # done
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_FOUR)


def test_upload_a_large_size_file(citizen_login):  # it is uploading the file, it shuld give error mesaage #TODO : ERROR
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=LARGE_IMAGELIST)


def test_csr_search_complaint(csr_employee_login):
    csr_home_page = CsrHomePage()
    mobile_no = "9337682030"
    complaint_no = "03/07/2018/001142"

    # Search with Mobile No
    csr_search_complaint(mobile_no)
    time.sleep(10)
    csr_home_page.clear_search()

    # Search with Complaint No
    csr_search_complaint('', complaint_no)
    time.sleep(2)
    csr_home_page.clear_search()

    # Search with Mobile  No and Complaint No
    csr_search_complaint(mobile_no, complaint_no)
    time.sleep(2)
    csr_home_page.clear_search()


def test_csr_create_complaint(csr_employee_login):
    complaint = csr_create_complaint("Spandan Raj Seth",
                         "9439576138",
                         "Garbage",
                         "Clean it as soon as possible",
                         "House No : 106, near CCD",
                         "Amritsar",
                         "Land mark ABC",
                         "Malind Nagar")
    print(complaint["complaint_number"])

    MyComplaintsPage().open_complaint(complaint["complaint_number"])

def test_csr_workflow(csr_employee_login):
    complaint = csr_create_complaint("Spandan Raj Seth",
                                            "9439576138",
                                            "Garbage",
                                            "Clean it as soon as possible",
                                            "House No : 106, near CCD",
                                            "Amritsar",
                                            "Land mark ABC",
                                            "Malind Nagar")
    csr_search_complaint(complaint["complaint_number"])




