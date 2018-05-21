from framework.selenium_plus import *
from pages.flows.common import *


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


def test_pgr_workflow():
    # Create a new complaint
    citizen_login("7975179334", "123456")
    upload_photo = DEFAULT_IMAGELIST_THREE
    add_complaint_details("Garbage", "Amritsar, Punjab, India ", "Street end", "Leakage of water", upload_photo)
    # Acknowledgement on successful complaint submission
    complaint_no = complaint_registration_number_recevied()
    print(complaint_no)
    # Search and view complaint created on My Complaints
    view_my_complaints(complaint_number)
    comment_on_complaint("Add comments")

    # Navigate to the home page and logout
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    # Login as GRO
    gro_employee_login("AMRGRO001", "12345678")
    # Assign the complaint to Last mile employee
    assign_open_complaints(complaint_no, "Manjunath")