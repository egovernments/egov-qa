import time

from pytest import fixture

from environment import *
from pages import *
from pages.employee.common import EmployeeLoginPage
from pages.employee.complaints import UnassignedComplaintsPage

complaint_number = []
complain = []


@fixture
def citizen_login(username=None, otp=None):
    username = username or DEFAULT_CITIZEN_USERNAME
    otp = otp or DEFAULT_FIXED_OTP
    LoginPage().navigate().set(username).submit()
    OTPPage().set(otp).get_started()
    yield


@fixture
def GRO_employee_login(username=None, password=None):
    username = username or GRO_EMPLOYEE_USERNAME
    password = password or DEFAULT_PASSWORD
    EmployeeLoginPage().navigate(APP_EMPLOYEE_URL).employee_id(username) \
        .password(password).submit()
    yield


@fixture
def last_mile_employee_login(username=None, otp=None):
    username = username or LAST_MILE_EMPLOYEE_USERNAME
    otp = otp or DEFAULT_FIXED_OTP
    LoginPage().navigate(APP_EMPLOYEE_URL).set(username).submit()
    OTPPage().set(otp).get_started()
    yield


def logout():
    TopMenuNavigationComponent().ham()
    LogoutPage().submit()


def add_complaint_details(
        complaint_type,
        location,
        landmark,
        additional_details,
        upload_photo,
        flag_complaint_submit=True
):
    complaint = AddComplaintPage()
    complaint.file_complaint()
    complaint.set_complaint_type(complaint_type)
    complaint.set_location_by_address(location)
    time.sleep(3)
    complaint.set_landmark_details(landmark)
    complaint.set_complaint_details(additional_details)
    complaint.upload_images(upload_photo)
    time.sleep(2)

    if flag_complaint_submit:
        complaint.submit()


def complaint_successful_page():
    acknowledgement = ComplaintSubmittedPage()
    co = acknowledgement.get_complaint_number()
    complaint_number.append(acknowledgement.get_complaint_number())
    acknowledgement.click_continue()
    return co


def view_my_complaints(complaint_number = 0):
    myComplaint = MyComplaintsPage()
    myComplaint.select_my_complaint()
    cards = myComplaint.get_all_complaints()

    print(len(cards))
    for i in cards:
        complain.append(i.get_complaint_no())
    if complaint_number == 0:
        for cn in complain:
            print(cn)
    else:
        a = complain.index(complaint_number[0])
        cards[a].track_complaint()


def assign_open_complaints(complaint_number, comments, assignee):
    complaints = UnassignedComplaintsPage()
    cards = complaints.get_all_complaints()
    for i in cards:
        complain.append(i.get_complaint_no())
    a = complain.index(complaint_number[0])
    cards[a].track_complaint()
    complaints.add_comments(comments).send_comment()
    complaints.assign_complaint(assignee)