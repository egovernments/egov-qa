import time

from pytest import fixture

from environment import *
from pages import *
from pages.employee.common import *
from pages.employee.complaints import *

# complaint_number = []
# complain = []


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
    time.sleep(2)
    complaint.set_landmark_details(landmark)
    complaint.set_complaint_details(additional_details)
    complaint.upload_images(upload_photo)
    time.sleep(2)

    if flag_complaint_submit:
        complaint.submit()


def complaint_registration_number_recevied():
    acknowledgement = ComplaintSubmittedPage()
    complaint_no = acknowledgement.get_complaint_number()
    acknowledgement.click_continue()
    return complaint_no


def view_my_complaints(complaint_number):
    complain = []
    myComplaint = MyComplaintsPage()
    AddComplaintPage().complaints_icon()
    # myComplaint.click_my_complaint()
    cards = myComplaint.get_all_complaints()

    for i in cards:
        complain.append(i.get_complaint_no())
    complaints = complain.index(complaint_number)
    cards[complaints].track_complaint()
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
    time.sleep(2)
    MyComplaintsPage().open_compalint(complaint_number)
    time.sleep(2)


def complaint_details(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(2)
    MyComplaintsPage().open_compalint(complaint_number)
    time.sleep(2)
    """
    complaint_summary_page = ComplaintSummaryPage()
    print(complaint_summary_page.get_complaint_number())
    print(complaint_summary_page.get_additional_comments())
    print(complaint_summary_page.get_compalint_type())
    print(complaint_summary_page.get_complaint_submission_date())
    print(complaint_summary_page.get_complaint_status())
    print(complaint_summary_page.get_no_of_image())
    print(complaint_summary_page.get_location())
    print("done")
    """


def rate_closed_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(2)
    MyComplaintsPage().open_compalint(complaint_number)
    complaint_summary_page = ComplaintSummaryPage()
    complaint_summary_page.rate_complaint()
    complaint_feedback_page = ComplaintFeedbackPage()
    complaint_feedback_page.star_click(4)
    complaint_feedback_page.check_others()
    complaint_feedback_page.set("done i am happy with work").submit()


def reopen_closed_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(4)
    MyComplaintsPage().open_compalint(complaint_number)
    complaint_summary_page = ComplaintSummaryPage()
    time.sleep(2)
    complaint_summary_page.reopen_complaint()
    ReopenComplaintPage().set("still there is a problem").submit()


def resolve_assigned_complaint(complaint_number, comments):
    pass