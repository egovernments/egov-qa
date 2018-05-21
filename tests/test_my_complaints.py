from pytest import fixture

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


def test_update_my_complaints(citizen_login):
    # Add Complaint with details
    upload_photo = DEFAULT_IMAGELIST_ONE
    add_complaint_details(
        "Water Body",
        "Amritsar, Punjab, India ",
        "Street end",
        "Leakage of water",
        upload_photo
    )
    # Acknowledgement on successful complaint submission
    complaint_no = complaint_registration_number_recevied()
    print('complaint number is: ', complaint_no)

    view_my_complaints(complaint_number)
    comment_on_complaint("Add comment")


def test_track_my_complaint(citizen_login):
    # Add Complaint with details
    upload_photo = DEFAULT_IMAGELIST_ONE
    add_complaint_details(
        "Water Body",
        "Amritsar, Punjab, India ",
        "Street end",
        "Leakage of water",
        upload_photo
    )
    # Acknowledgement on successful complaint submission
    complaint_no = complaint_registration_number_recevied()
    print(complaint_no)

    # Search complaint
    view_my_complaints(complaint_number)
    # complaint_tracking(complaint_number)  # assert complaint status to be "Submitted"

    # Complaint Workflow: GRO login, and assign complaint to Last mile employee
    # Track complaint with status: "Assigned"
    # Complaint Workflow: Last mile employee, Mark compliant as Resolved
    # Track complaint with status: "Resolved"


def test_complaint_feedback(citizen_login):
    # Add complaint
    add_complaint_details()
    complaint_registration_number_recevied()
    # Search and view complaint created on My Complaints
    complaint_number = ["10/05/2018/000705"]
    view_my_complaints(complaint_number) # assert complaint status to be Submitted
    comment_on_complaint("Add comments")
    # Employee workflow
    # feedback
    view_my_complaints() # assert complaint status to be Resolved
    complaint_feedback(4, "On time resolved")

    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()


def test_complaint_reopen(citizen_login):
    # Add complaint
    add_complaint_details()
    complaint_registration_number_recevied()
    # view complaint
    view_my_complaints() # assert complaint status to be Submitted
    # Employee workflow
    # complaint_tracking() # track complaint unitl status become Resolved
    # reopen complaint
    view_my_complaints() # assert complaint status to be Resolved
    reopen_closed_complaint()