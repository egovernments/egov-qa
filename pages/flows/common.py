import time

from pytest import fixture

from environment import *
from pages import *
from pages.employee.common import *
from pages.employee.complaints import *

complaint_number = []
complain = []


@fixture
def citizen_login(username=None, otp=None):
    username = username or DEFAULT_CITIZEN_USERNAME
    otp = otp or DEFAULT_FIXED_OTP
    LoginPage().navigate().set(username).submit()
    OTPPage().set(otp).get_started()


@fixture
def gro_employee_login(username=None, password=None):
    username = username or GRO_EMPLOYEE_USERNAME
    password = password or DEFAULT_PASSWORD
    EmployeeLoginPage().navigate().employee_id(username) \
        .password(password).submit()


@fixture
def last_mile_employee_login(username=None, password=None):
    username = username or LAST_MILE_EMPLOYEE_USERNAME
    password = password or DEFAULT_PASSWORD
    EmployeeLoginPage().navigate().employee_id(username)\
        .password(password).submit()


@fixture
def logout():
    TopMenuNavigationComponent().ham()
    LogoutPage().submit()


def add_complaint_details(complaint_type, location, landmark, additional_details, upload_photo,
                          flag_complaint_submit=True):
    complaint = AddComplaintPage()
    complaint.complaints_icon()
    complaint.add_icon()
    complaint.set_complaint_type(complaint_type)
    complaint.set_location_by_address(location)
    time.sleep(3)
    complaint.set_landmark_details(landmark)
    complaint.set_complaint_details(additional_details)
    complaint.upload_images(upload_photo)

    time.sleep(2)

    if flag_complaint_submit:
        complaint.submit()


def complaint_registration_number_recevied():
    acknowledgement = ComplaintSubmittedPage()
    co = acknowledgement.get_complaint_number()
    complaint_number.append(acknowledgement.get_complaint_number())
    acknowledgement.click_continue()
    return co


def view_my_complaints(complaint_number):
    myComplaint = MyComplaintsPage()
    AddComplaintPage().complaints_icon()
    # myComplaint.click_my_complaint()
    cards = myComplaint.get_all_complaints()

    for i in cards:
        complain.append(i.get_complaint_no())
    c = complain.index(complaint_number)
    cards[c].track_complaint()
    # if complaint_number == 0:
    #     print("entered if")
    #     for cn in complain:
    #         print(cn)
    # else:
    #     print("entered else")
    #     a = complain.index(complaint_number)
    #     print(a)
    #     cards[a].track_complaint()


def comment_on_complaint(comment):
    myComplaint = MyComplaintsPage()
    myComplaint.add_comments(comment)
    myComplaint.send_comment()


def complaint_feedback(rating, comment):
    complaint_feedback = ComplaintFeedbackPage()
    complaint_feedback.rate()
    complaint_feedback.star_click(rating)
    complaint_feedback.check_services().check_resolution_time()
    complaint_feedback.set(comment).submit()


def assign_open_complaints(complaint_number, comments, assignee):
    complaints = UnassignedComplaintsPage()
    # cards = complaints.get_all_complaints()
    # for i in cards:
    #     complain.append(i.get_complaint_no())
    # a = complain.index(complaint_number[0])
    # cards[a].track_complaint()
    complaints.add_comments(comments).send_comment()
    complaints.assign_complaint(assignee)


def open_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(4)
    MyComplaintsPage().open_compalint(complaint_number)
    time.sleep(5)


def complaint_details(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(4)
    MyComplaintsPage().open_compalint(complaint_number)
    time.sleep(4)
    csp = ComplaintSummaryPage()
    print(csp.get_complaint_number())
    print(csp.get_additional_comments())
    print(csp.get_compalint_type())
    print(csp.get_complaint_submission_date())
    print(csp.get_complaint_status())
    print(csp.get_no_of_image())
    print(csp.get_location())
    print("done")


def rate_closed_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(4)
    MyComplaintsPage().open_compalint(complaint_number)
    csp = ComplaintSummaryPage()
    csp.rate_complaint()
    cfp = ComplaintFeedbackPage()
    cfp.star_click(4)
    cfp.check_others()
    cfp.set("done i am happy with work").submit()


def reopen_closed_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(4)
    MyComplaintsPage().open_compalint(complaint_number)
    csp = ComplaintSummaryPage()
    time.sleep(2)
    csp.reopen_complaint()
    ReopenComplaintPage().set("still there is a problem").submit()


def resolve_assigned_complaint(complaint_number, comments):
    pass