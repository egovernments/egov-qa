from pytest import fixture

from pages import RegistrationPage
from pages import OTPPage
from pages import HomePage
from pages import LanguageSelectionPage
from pages import AddComplaintPage
from pages import ComplaintFeedbackPage
from pages import LoginPage
from pages import ComplaintUnassignPage
from pages import ComplaintReassignPage
from framework.selenium_plus import *
from pages.CitizenProfile import CitizenProfilePage
from pages.ComplaintSubmitted import ComplaintSubmittedPage
from pages.MyComplaints import MyComplaintsPage


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


def test_otp_submission():
    otp = OTPPage
    otp.navigate()

    otp.set("1234").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():
    comp = AddComplaintPage
    comp.navigate()
    photo1 = "/Users/tarun.lalwani/Documents/screenshots/CapturFiles_1.png"
    photo2 = "/Users/tarun.lalwani/Documents/screenshots/CapturFiles-20180126_012014.png"
    photo3 = "/Users/tarun.lalwani/Documents/screenshots/CapturFiles-20180310_095257.png"
    comp.upload_images(photo1, photo2, photo3)
    comp.remove_image_2()
    # comp.set_complaint_type("garbage", "Overflowing Garbage Bins")
    # comp.set_location_by_address("Homigo Ant")
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_citizen_profile():
    CitizenProfilePage.navigate().set("ABH", "ab.se@gmail.com").set_city("Amritsar").click_continue()


def test_complain_submitted():
    ComplaintSubmittedPage.navigate()
    print(ComplaintSubmittedPage.get_complaint_number())
    ComplaintSubmittedPage.click_continue()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_my_complaints():
    complaints = MyComplaintsPage
    complaints.navigate()
    cards = complaints.get_all_complaints()
    card = cards[2]

    print(card.get_complaint_header())
    print(card.get_complaint_status())
    print(card.get_complaint_no())
    print(card.get_complaint_date())
    card.track_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-details?status=rejected"


def test_user_registration():
    userRegistration = RegistrationPage
    userRegistration.navigate()
    userRegistration.set("9988776655", "FirstName", "Bathi").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_language_selection():
    ls = LanguageSelectionPage
    ls.navigate()
    ls.language("punjabi").language("hindi").language("english").submit()

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register"


def test_homepage():
    hp = HomePage

    hp.navigate().new_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"

    hp.navigate().my_complaints()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/my-complaints"


def test_complaintfeedbackpage():
    cf = ComplaintFeedbackPage
    cf.navigate().star_click(1)
    cf.check_services().check_quality_of_work()
    cf.set("good to go").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/feedback"


def test_complaintunassignedpage():
    cap=ComplaintUnassignPage
    cap.navigate().assign().reject()

def test_complaintreassignpage():
    crp=ComplaintReassignPage
    crp.navigate().reject().assign()
