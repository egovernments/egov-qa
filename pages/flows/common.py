import time

from pytest import fixture
from environment import *
from pages import *
from pages.employee.common import EmployeeLoginPage
from pages.employee.complaints import UnassignedComplaintsPage

complaint_number = []
complain = []

from environment import *
from pages import LoginPage, OTPPage, AddComplaintPage, HomePage


@fixture
def citizen_login(username=None, otp=None):
    username = username or DEFAULT_CITIZEN_USERNAME
    otp = otp or DEFAULT_FIXED_OTP
    loginpage = LoginPage()
    loginpage.navigate()

    loginpage.set(username)
    loginpage.submit()
    otppage = OTPPage()
    otppage.set(otp)
    otppage.get_started()


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


def complaint_successful_page():
    acknowledgement = ComplaintSubmittedPage()
    co = acknowledgement.get_complaint_number()
    complaint_number.append(acknowledgement.get_complaint_number())
    acknowledgement.click_continue()
    return co


def view_my_complaints(complaint_number=0):
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
    MyComplaintsPage().open_compalint(complaint_number)
    csp = ComplaintSummaryPage()
    csp.reopen_complaint()
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
        .set_complaint_type(complaint_type_select, comp
    laint_type_search) \
        .set_location_by_address(location)
    acp.upload_images(images)

    if flag_submit_complaint:
        acp.click_submit()
