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
    create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ", "Street end",
                         "Leakage of water", upload_photo)
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

    # From create complaint to resolve
    pgr_details = complaint_workflow_from_citizen_to_employee("Mark as Resolve")

    # Complaint Details (Test Data)
    complaint_number = pgr_details["complaint_number"]
    status = pgr_details["status"]
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(status))
    current_status = pgr_details["current_status"]

    # Verification
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(current_status))

    # rate the closed complaint
    citizen_login()
    rate_complaint = rate_closed_complaint(complaint_number)
    status_before = rate_complaint["Status_before_rate"]
    status_after = rate_complaint["Status_after_rate"]
    print("Complaint Number: {}".format(complaint_number), "Current Status: {}".format(status_before))
    print("Complaint Number: {}".format(complaint_number), "Current Status: {}".format(status_after))


def test_reopen_closed_complaint():

    # From create complaint to resolve
    pgr_details = complaint_workflow_from_citizen_to_employee("Mark as Resolve")

    # Complaint Details (Test Data)
    complaint_number = pgr_details["complaint_number"]
    status = pgr_details["status"]
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(status))
    current_status = pgr_details["current_status"]

    # Verification
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(current_status))

    # Reopen the closed complaint
    citizen_login()
    reopen_complaint = reopen_closed_complaint(complaint_number)
    status_before = reopen_complaint["Status_before_reopen"]
    status_after = reopen_complaint["Status_after_reopen"]
    print("Complaint Number: {}".format(complaint_number), "Current Status: {}".format(status_before))
    print("Complaint Number: {}".format(complaint_number), "Current Status: {}".format(status_after))


def test_reassign_complaint():
    # Create complaint from citizen to last mile employee verification
    pgr_details = complaint_workflow_from_citizen_to_employee("Request for Re-Assign")

    # Complaint Details (Test Data)
    complaint_number = pgr_details["complaint_number"]
    status = pgr_details["status"]
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(status))
    current_status = pgr_details["current_status"]

    # Verification
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(current_status))

    # Re-Assign complaint
    gro_employee_login("Amardeep", "12345678")
    reassign = complaint_reassign(complaint_number)
    current_status = reassign["status"]
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(current_status))
    # last_mile_employee_login("MamataDevi", "12345678")
    # last_mile_employee_verification(complaint_number, "Mark as Resolve")


def test_reject_complaint():
    # Create complaint from citizen
    citizen_login()
    upload_photo = DEFAULT_IMAGELIST_TWO
    complaint_info = create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ", "Street end",
                         "Leakage of water", upload_photo)
    complaint_number = complaint_info["complaint_number"]
    status = complaint_info["status"]
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(status))
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()

    # GRO verification (Reject Complaint)
    gro_employee_login("Amardeep", "12345678")
    complaint_reject(complaint_number)
    logout()
    quit_driver()

    # Citizen Login
    citizen_login()
    open_complaint(complaint_number)
    status = get_current_status()
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(status))
    navigation.back().back()
    logout()
    quit_driver()


def test_reopen_rejected_complaint():
    # Create complaint from citizen
    citizen_login()
    upload_photo = DEFAULT_IMAGELIST_TWO
    complaint_info = create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ", "Street end",
                         "Leakage of water", upload_photo)
    complaint_number = complaint_info["complaint_number"]
    status = complaint_info["status"]
    print("Complaint Number: {}".format(complaint_number), "Complaint Status: {}".format(status))
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()

    # GRO verification (Reject Complaint)
    gro_employee_login("Amardeep", "12345678")
    complaint_reject(complaint_number)
    logout()
    quit_driver()

    # Citizen Login: Reopen Rejected Complaint
    citizen_login()
    reopen_complaint = reopen_closed_complaint(complaint_number)
    status_before = reopen_complaint["Status_before_reopen"]
    status_after = reopen_complaint["Status_after_reopen"]
    print("Complaint Number: {}".format(complaint_number), "Current Status: {}".format(status_before))
    print("Complaint Number: {}".format(complaint_number), "Current Status: {}".format(status_after))
    navigation.back().back()
    logout()
    quit_driver()

"""
def test_timeline_details(citizen_login):
    complaint_timeline_details('23/05/2018/000835')

def test_get_all_comaplint(citizen_login):
    get_all_comments("25/05/2018/000861")
"""
