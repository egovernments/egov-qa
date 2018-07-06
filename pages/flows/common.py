import time

from pytest import fixture

from environment import *
from framework.selenium_plus import *
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
def csr_employee_login(username=None, password=None, city=None):
    username = username or CSR_EMPLOYEE_USERNAME
    password = password or DEFAULT_PASSWORD
    city = city or DEFAULT_CITY
    EmployeeLoginPage().navigate().employee_id(username) \
        .password(password).city(city).submit()


@fixture
def gro_employee_login(username=None, password=None, city=None):
    username = username or GRO_EMPLOYEE_USERNAME
    password = password or DEFAULT_PASSWORD
    city = city or DEFAULT_CITY
    EmployeeLoginPage().navigate().employee_id(username) \
        .password(password).city(city).submit()


@fixture
def last_mile_employee_login(username=None, password=None, city=None):
    username = username or LAST_MILE_EMPLOYEE_USERNAME
    password = password or DEFAULT_PASSWORD
    city = city or DEFAULT_CITY
    EmployeeLoginPage().navigate().employee_id(username) \
        .password(password).city(city).submit()


@fixture
def logout():
    TopMenuNavigationComponent().user_profile()
    LogoutPage().submit()


def citizen_create_new_complaint(complaint_type, location, landmark, additional_details, upload_photos=None,
                                 flag_complaint_submit=True, open_complaints=True):
    complaint = AddComplaintPage()
    complaint.complaints_icon()
    complaint.set_complaint_type(complaint_type)
    # TODO: improve this
    # waiting for the current location to load
    time.sleep(2)
    print("Location select - " + complaint.set_location_by_address(location))
    time.sleep(2)
    complaint.set_landmark_details(landmark)
    complaint.set_complaint_details(additional_details)

    if upload_photos:
        complaint.upload_images(upload_photos)
        time.sleep(2)

    if flag_complaint_submit:
        complaint.submit()

    complaint_number = complaint_registration_number_recevied()
    print(complaint_number)

    if open_complaints:
        open_complaint(complaint_number)
        comment_on_complaint("Complaint registered")

    status = get_current_status()
    print(status)

    return {
        "complaint_number": complaint_number,
        "status": status
    }


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
    AddComplaintPage().complaints_icon()
    # MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    # image = ComplaintSummaryPage().get_no_of_image()
    # assert image == len(upload_photo) , "Number of image uploaded while creating complaint"


def comment_on_complaint(comment):
    myComplaint = MyComplaintsPage()
    myComplaint.add_comments(comment)
    myComplaint.send_comment()


def assign_open_complaint(complaint_number, assignee):
    complaints = UnassignedComplaintsPage()
    # cards = complaints.get_all_complaints()
    # for i in cards:
    #     complain.append(i.get_complaint_no())
    # a = complain.index(complaint_number[0])
    # cards[a].track_complaint()
    complaints.assign_complaint(assignee)
    complaints.go_to_homepage()


def open_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(2)
    MyComplaintsPage().open_complaint(complaint_number)
    time.sleep(2)


def complaint_details(complaint_number):
    MyComplaintsPage().select_my_complaint()
    time.sleep(2)
    MyComplaintsPage().open_complaint(complaint_number)
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


def resolve_assigned_complaint(complaint_number):
    MyComplaintsPage().open_complaint(complaint_number)
    comment_on_complaint("Complaint Resolved")
    ComplaintResolvedCommentPage().click_mark_resolved()
    pass


def get_current_status():
    complaint_summary_page = ComplaintCitizenSummaryPage()
    return complaint_summary_page.get_complaint_status()


def gro_verification(complaint_number):
    GroHomePage().click_unassigned_complaint_list().open_complaint(complaint_number)
    assign_open_complaint(complaint_number, "Antriksh Kumar")
    EmployeeComplaintAcknowledgementPage().go_to_home()
    GroHomePage().click_assigned_complaint_list().open_complaint(complaint_number)
    comment_on_complaint("Complaint Under verification")
    current_status = get_current_status()

    return {
        "current_status": current_status
    }


def last_mile_employee_verification(complaint_number, complaint_action):
    if complaint_action == "Mark as Resolve":
        resolve_assigned_complaint(complaint_number)
    elif complaint_action == "Request for Re-Assign":
        request_for_reassign_complaint(complaint_number)
    EmployeeComplaintAcknowledgementPage().go_to_home()
    logout()
    quit_driver()


def rate_closed_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    status_before = get_current_status()
    complaint_summary_page = ComplaintCitizenSummaryPage()
    complaint_summary_page.rate_complaint()
    complaint_feedback_page = ComplaintFeedbackPage()
    complaint_feedback_page.star_click(4)
    complaint_feedback_page.reason_for_feedback(complaint_feedback_page.Feedback.SERVICES)
    complaint_feedback_page.set("done i am happy with work").submit()
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    status_after = get_current_status()

    return {
        "Status_before_rate": status_before,
        "Status_after_rate": status_after
    }


def reassign_open_complaint(assignee):
    complaint_reassign_page = ComplaintReassignPage()
    complaint_reassign_page.reassign(assignee)


def reopen_closed_complaint(complaint_number):
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    status_before = get_current_status()
    complaint_summary_page = ComplaintCitizenSummaryPage()
    complaint_summary_page.reopen_complaint()
    reopen = ReopenComplaintPage()
    reopen.reason_for_reopen(reopen.Reason.NO_WORK_WAS_DONE)
    reopen.set("Still pending work")
    reopen.submit()
    acknowledgement = ComplaintReopenedPage().get_successful_message()
    assert "Re-opened" in acknowledgement, "acknowledgement should contain the Re-Opened"
    ComplaintReopenedPage().go_to_home()
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    status_after = get_current_status()
    assert ComplaintCitizenSummaryPage().get_complaint_status() == "Re-opened", "status is not Re-Opened"
    return {
        "Status_before_reopen": status_before,
        "Status_after_reopen": status_after
    }


def complaint_reassign(complaint_number):
    GroHomePage().click_unassigned_complaint_list().open_complaint(complaint_number)
    reassign_open_complaint("Mamata Devi")
    EmployeeComplaintAcknowledgementPage().go_to_home()
    GroHomePage().click_assigned_complaint_list().open_complaint(complaint_number)
    current_status = get_current_status()
    TopMenuNavigationComponent().back()
    logout()
    quit_driver()
    return {
        "status": current_status
    }


def complaint_reject(complaint_number):
    GroHomePage().click_unassigned_complaint_list().open_complaint(complaint_number)
    reject = ComplaintRejectPage()
    reject.click_reject()
    reject.option(reject.REASONS.OPERATION_ALREADY_UNDERWAY)
    reject.send_comment("Complaint is already taken up")
    reject.submit_reject()
    EmployeeComplaintAcknowledgementPage().go_to_home()
    # GroHomePage().click_assigned_complaint_list().open_compalint(complaint_number)
    # status = get_current_status()

    # return {
    #     "status": status
    # }


def request_for_reassign_complaint(complaint_number):
    MyComplaintsPage().open_complaint(complaint_number)
    comment_on_complaint("Requested for re-assign")
    reassign = RequestReassignReasonPage()
    reassign.click_request_assign()
    reassign.option(reassign.REASONS.NOT_MY_DEPARTMENT)
    reassign.click_reassign()
    pass


def complaint_workflow_from_citizen_to_employee(complaint_action):
    # Add Registration
    citizen_login()
    complaint_info = citizen_create_new_complaint("Blocked Drain", "Amritsar, Punjab, India ", "Main roads",
                                                  "Drainage water is flooding")
    complaint_number = complaint_info["complaint_number"]
    status = complaint_info["status"]
    navigation = TopMenuNavigationComponent()
    navigation.back().back()
    logout()
    quit_driver()

    # GRO Complaint Verification: Assigning complaints
    gro_employee_login(GRO_EMPLOYEE_USERNAME, DEFAULT_PASSWORD)
    workflow_status = gro_verification(complaint_number)
    gro_status = workflow_status["current_status"]
    navigation.back()
    logout()
    quit_driver()

    # Last Mile Employee Complaint Verification: Resolving Assigned complaints
    last_mile_employee_login(LAST_MILE_EMPLOYEE_USERNAME, DEFAULT_PASSWORD)
    last_mile_employee_verification(complaint_number, complaint_action)

    return {
        "complaint_number": complaint_number,
        "status": status,
        "current_status": gro_status,
    }


def get_all_comments(complaint_number):
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    ccc = ComplaintCommentCard()
    comments = ccc.get_all_comments()
    comment_number = 0
    list_of_all_comment = []
    for i in range(0, len(comments) // 3):
        commentsdict = dict()
        commentsdict['name'] = comments[comment_number]
        comment_number += 1
        commentsdict['comment'] = comments[comment_number]
        comment_number += 1
        commentsdict['date'] = comments[comment_number]
        comment_number += 1
        # TO-DO TYPE SHOULD NOT BE BLANK
        commentsdict['type'] = ""
        list_of_all_comment.append(commentsdict)

    print(list_of_all_comment)


def complaint_timeline_details(complaint_number):
    MyComplaintsPage().select_my_complaint()
    MyComplaintsPage().open_complaint(complaint_number)
    ctp = ComplaintTimelinePage()
    timelines = ctp.get_all_timeline_card()
    for i in timelines:
        print(i.get_timeline_details())


def csr_search_complaint(mobile_no='', complaint_no=''):
    csr_home_page = CsrHomePage()
    if mobile_no != '':
        csr_home_page.set_citizen_mobile_no(mobile_no)

    if complaint_no != '':
        csr_home_page.set_complaint_no(complaint_no)

    csr_home_page.search()


def csr_create_complaint(citizen_name, citien_mobile_no, complaint_type, complaint_details, address, city,
                         landmark,
                         mohalla):
    CsrHomePage().wait_for_busy()
    CsrHomePage().add_complaint()
    ccp = CsrCreateComplaintPage()
    ccp.set_name(citizen_name)
    ccp.set_mobile_no(citien_mobile_no)
    ccp.set_complaint_details(complaint_details)
    ccp.set_address(address)
    ccp.set_landmark(landmark)
    ccp.set_mohalla(mohalla)
    time.sleep(1)

    ccp.set_complaint_type(complaint_type)
    time.sleep(1)

    ccp.set_city(city)
    time.sleep(1)

    ccp.submit()
    complaint_number = ccp.get_complaint_number()
    return {
        "citizen_name": citizen_name,
        "mobile_number": citien_mobile_no,
        "complaint_type": complaint_type,
        "complaint_details": complaint_details,
        "address": address,
        "city": city,
        "landmark": landmark,
        "mohalla": mohalla,
        "complaint_number": complaint_number
    }
