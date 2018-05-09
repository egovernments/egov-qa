from pytest import fixture

from environment import *
from pages import *
from framework.selenium_plus import *
from pages.flows.common import *


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


def test_create_complaint(citizen_login):
    # Login as a registered citizen user
    #("7975179334")

    # Create a new complaint
    add_complaint_details(
        "Water Body",
        "Amritsar, Punjab, India ",
        "Street end",
        "Leakage of water",
        "D:/Repositories/rainmaker_automation/egov-qa/assets/images/image1.jpg"
    )
    # Acknowledgement on successful complaint submission
    complaint_successful_page(complaint_number)
    print(complaint_number)

    # Search and view complaint created on My Complaints
    view_my_complaints(complaint_number, "Comments")

    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()


# def test_complaint_workflow():
#     GRO_employee_login(password="murali@1993")
#     logout()
