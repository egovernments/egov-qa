import time

from pytest import fixture

from environment import *
from pages import *
from pages.employee.common import *
from pages.employee.complaints import *


@fixture
def citizen_login(username=None, otp=None):
    username = username or DEFAULT_CITIZEN_USERNAME
    otp = otp or DEFAULT_FIXED_OTP
    navigate = LoginPage().navigate()
    navigate.set(username).submit()
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
    EmployeeLoginPage().navigate().employee_id(username) \
        .password(password).submit()


@fixture
def logout():
    TopMenuNavigationComponent().ham()
    LogoutPage().submit()


def add_complaint_details(complaint_type, location, landmark, additional_details, upload_photo,
                          flag_complaint_submit=True):
    complaint = AddComplaintPage()
    complaint.complaints_icon()
    complaint.click_on_plus_icon()
    complaint.set_complaint_type(complaint_type)
    complaint.set_location_by_address(location)
    time.sleep(2)
    complaint.set_landmark_details(landmark)
    complaint.set_complaint_details(additional_details)
    complaint.upload_images(upload_photo)
    time.sleep(2)

    if flag_complaint_submit:
        complaint.submit()


def complaint_registration_number_recevied(flag_is_continue=True):
    acknowledgement = ComplaintSubmittedPage()
    complaint_no = acknowledgement.get_complaint_number()

    if flag_is_continue:
        acknowledgement.click_continue()
    return complaint_no


def create_new_complaint_by_plus_icon(location, additional_details, complaint_type_search, complaint_type_select,
                                      landmark, flag_submit_complaint=True):
    HomePage().my_complaints()
    addcomplaintpage = AddComplaintPage()
    MyComplaintsPage().add_complaint_plus_button()
    addcomplaintpage.set_location_by_address(location)
    addcomplaintpage.set_complaint_details(additional_details)
    addcomplaintpage.set_landmark_details(landmark)
    addcomplaintpage.set_complaint_type(complaint_type_search, complaint_type_select)
    image1 = "/home/satish/Pictures/bank1.png"
    image2 = "/home/satish/Pictures/bank1.png"
    image3 = "/home/satish/Pictures/bank1.png"
    addcomplaintpage.upload_images(image1, image2, image3)

    time.sleep(3)
    addcomplaintpage.submit()


def complaint_successful_page():
    acknowledgement = ComplaintSubmittedPage()
    co = acknowledgement.get_complaint_number()
    acknowledgement.click_continue()
    return co


def view_my_complaints(complaint_number):
    complain = []
    AddComplaintPage().complaints_icon()
    myComplaint = MyComplaintsPage()


def comment_on_complaint(comment):
    myComplaint = MyComplaintsPage()
    myComplaint.add_comments(comment)
    myComplaint.send_comment()


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
    MyComplaintsPage().open_compalint(complaint_number)
    complaint_summary_page = ComplaintSummaryPage()
    time.sleep(2)
    complaint_summary_page.reopen_complaint()
    ReopenComplaintPage().set("still there is a problem").submit()
    rcp = ReopenComplaintPage()
    rcp.reason_for_reopen(rcp.Reason.NO_WORK_WAS_DONE)
    rcp.set("work should be done")
    rcp.submit()
    acknowledgement = ComplaintReopenedPage().get_successful_message()
    assert "Re-opened" in acknowledgement, "acknowledgement should contain the Re-Opened"
    ComplaintReopenedPage().go_to_home()
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_compalint(complaint_number)
    assert ComplaintSummaryPage().get_complaint_status() == "Re-opened", "status is not Re-Opened"


def login_gro(username=None, password=None):
    LoginPage().navigate().set(username).submit()
    OTPPage().set(DEFAULT_FIXED_OTP).get_started()
    yield
    HomePage().navigate()


def create_new_complaint(
        location,
        additional_details,
        landmark_details,
        complaint_type_search,
        complaint_type_select,
        images,
        flag_submit_complaint=True):
    acp = AddComplaintPage()

    acp.navigate() \
        .set_landmark_details(landmark_details) \
        .set_complaint_details(additional_details) \
        .set_complaint_type(complaint_type_select, complaint_type_search) \
        .set_location_by_address(location)
    acp.upload_images(images)

    if flag_submit_complaint:
        acp.click_submit()


def resolve_assigned_complaint(complaint_number, comments):
    pass
