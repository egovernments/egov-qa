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


def test_rate_closed_compalint():
    # Create complaint from citizen to last mile employee verification
    pgr_details = complaint_workflow_from_citizen_to_employee(complaint_action="Mark as Resolve")

    # Complaint Details (Test Data)
    complaint_number = pgr_details["complaint_number"]
    status = pgr_details["status"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))
    current_status = pgr_details["current_status"]

    # Verification
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, current_status))

    # rate the closed complaint
    citizen_login()
    rate_complaint = rate_closed_complaint(complaint_number)
    status_before = rate_complaint["status_before_rate"]
    status_after = rate_complaint["status_after_rate"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status_before))
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status_after))


def test_reopen_closed_complaint():
    # Create complaint from citizen to last mile employee verification
    pgr_details = complaint_workflow_from_citizen_to_employee(complaint_action="Mark as Resolve")

    # Complaint Details (Test Data)
    complaint_number = pgr_details["complaint_number"]
    status = pgr_details["status"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))
    current_status = pgr_details["current_status"]

    # Verification
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))

    # Reopen the closed complaint
    citizen_login()
    reopen_complaint = reopen_closed_complaint(complaint_number)
    status_before = reopen_complaint["status_before_reopen"]
    status_after = reopen_complaint["status_after_reopen"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status_before))
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status_after))


def test_reassign_complaint():
    # Create complaint from citizen to last mile employee verification
    pgr_details = complaint_workflow_from_citizen_to_employee(complaint_action="Request for Re-Assign")

    # Complaint Details (Test Data)
    complaint_number = pgr_details["complaint_number"]
    status = pgr_details["status"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))
    current_status = pgr_details["current_status"]

    # Verification
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, current_status))

    # Re-Assign complaint
    gro_employee_login(GRO_EMPLOYEE_USERNAME, DEFAULT_PASSWORD)
    reassign = complaint_reassign(complaint_number)
    current_status = reassign["status"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, current_status))
    # last_mile_employee_login("MamataDevi", "12345678")
    # last_mile_employee_verification(complaint_number, "Mark as Resolve")


def test_reject_complaint():
    # Create complaint from citizen
    citizen_login()
    upload_photo = DEFAULT_IMAGELIST_TWO
    complaint_info = create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ",
                                          "Street end",
                                          "Leakage of water", upload_photo)
    complaint_number = complaint_info["complaint_number"]
    status = complaint_info["status"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()

    # GRO verification (Reject Complaint)
    gro_employee_login(GRO_EMPLOYEE_USERNAME, DEFAULT_PASSWORD)
    complaint_reject(complaint_number)
    logout()
    quit_driver()

    # Citizen Login
    citizen_login()
    open_complaint(complaint_number)
    status = get_current_status()
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))
    navigation.back().back()
    logout()
    quit_driver()


def test_reopen_rejected_complaint():
    # Create complaint from citizen
    citizen_login()
    upload_photo = DEFAULT_IMAGELIST_TWO
    complaint_info = create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ",
                                          "Street end",
                                          "Leakage of water", upload_photo)
    complaint_number = complaint_info["complaint_number"]
    status = complaint_info["status"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status))
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()

    # GRO verification (Reject Complaint)
    gro_employee_login(GRO_EMPLOYEE_USERNAME, DEFAULT_PASSWORD)
    complaint_reject(complaint_number)
    logout()
    quit_driver()

    # Citizen Login: Reopen Rejected Complaint
    citizen_login()
    reopen_complaint = reopen_closed_complaint(complaint_number)
    status_before = reopen_complaint["status_before_reopen"]
    status_after = reopen_complaint["status_after_reopen"]
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status_before))
    print("Complaint Number:{0}, Complaint Status:{1}".format(complaint_number, status_after))
    navigation.back().back()
    logout()
    quit_driver()
