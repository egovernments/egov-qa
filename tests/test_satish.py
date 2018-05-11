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


def test_citizen_login():
    citizen_login('8792101399', "123456")


def test_new_complaint(citizen_login):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)


def test_new_complaint_by_plus_icon(citizen_login):
    create_new_complaint_by_plus_icon("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs",
                                      "landmarkdetail", True)


def test_open_complaint_and_comment(citizen_login, logout_citizen):
    complain_number = "09/05/2018/000652"
    comment_on_given_complaint(complain_number)


def test_logout(citizen_login):
    logout_citizen()


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

    add_complaint_details(complaint_type, location, landmark, additional_details, upload_photo)


def test_citizen_should_file_complaint_with_two_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])


def test_add_three_image_then_remove_one(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_open_compalint(citizen_login):
    open_complaint("10/05/2018/000676")


def test_complaint_detail(citizen_login):
    complaint_details("09/05/2018/000666")


def test_rate_closed_compalint(citizen_login):
    rate_closed_complaint("07/05/2018/000607")


def test_reopen_closed_complaint(citizen_login):
    reopen_closed_complaint("10/05/2018/000676")
