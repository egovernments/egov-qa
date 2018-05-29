from framework.selenium_plus import *
from pages.employee.common import EmployeeComplaintAcknowledgementPage
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


def test_citizen_login():
    citizen_login('8792101399', "123456")


def test_new_complaint(citizen_login):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)


def test_open_complaint_and_comment(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO):
    create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ", "Street end", "Leakage of water", upload_photo)
    complain_number = complaint_registration_number_recevied()
    view_my_complaints(complain_number)
    comment_on_complaint("Comments")


def test_logout(citizen_login):
    logout()


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):
    # Create a new complaint
    complaint_type = "Water Body"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Leakage of water"

    create_new_complaint(complaint_type, location, landmark, additional_details, upload_photo)


def test_citizen_should_file_complaint_with_two_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])


def test_add_three_image_then_remove_one(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_open_compalint(citizen_login):
    create_new_complaint("Illegal Cutting of Trees", "Amritsar, Punjab, India ", "Street end", "Useful trees")
    complaint_number = complaint_registration_number_recevied()
    open_complaint(complaint_number)


def test_complaint_detail(citizen_login):
    create_new_complaint("Potholes on the Road", "Amritsar, Punjab, India ", "Street end", "Difficult to travel")
    complaint_number = complaint_registration_number_recevied()
    complaint_details(complaint_number)


def test_rate_closed_compalint():
    citizen_login()
    create_new_complaint("Blocked Drain", "Amritsar, Punjab, India ", "Main roads", "Drainage water is flooding")
    complaint_number = complaint_registration_number_recevied()
    print(complaint_number)
    open_complaint(complaint_number)
    status = get_current_status()
    print(status) # Submitted
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()

    gro_employee_login("Amardeep", "12345678")
    GroHomePage().click_unassigned_complaint_list().open_compalint(complaint_number)
    assign_open_complaints(complaint_number, "Antriksh Kumar")
    EmployeeComplaintAcknowledgementPage().go_to_home()
    GroHomePage().click_assigned_complaint_list().open_compalint(complaint_number)
    status = get_current_status()
    print(status) # Assigned
    navigation.back()
    logout()
    quit_driver()

    last_mile_employee_login("AntrikshKumar", "12345678")
    resolve_assigned_complaint(complaint_number)
    EmployeeComplaintAcknowledgementPage().go_to_home()
    # open_complaint(complaint_number)
    # status = get_current_status()
    # print(status) # Resolved
    # navigation.back()
    logout()
    quit_driver()
"""
    citizen_login()
    # open_complaint(complaint_number)
    # status = get_current_status()
    # print(status)
    rate_closed_complaint(complaint_number)


def test_reopen_closed_complaint(citizen_login):
    reopen_closed_complaint("28/05/2018/000869")


def test_timeline_details(citizen_login):
    complaint_timeline_details('23/05/2018/000835')


def test_view_my_complaint(citizen_login):
    view_my_complaint('25/05/2018/000860')


def test_get_all_comaplint(citizen_login):
    get_all_comments("25/05/2018/000861")
"""