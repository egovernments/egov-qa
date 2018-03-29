from pytest import fixture

from pages import *
from framework.selenium_plus import *


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
    otp = OTPPage()
    otp.navigate()

    otp.set("12345").get_started()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():
    comp = AddComplaintPage()
    comp.navigate()
    comp.set_complaint_type("Overflowing Garbage Bins")
    comp.set_location_by_address("Homigo Ant")
    photo1 = "/Users/tarun.lalwani/Documents/screenshots/CapturFiles_1.png"
    photo2 = "/Users/tarun.lalwani/Documents/screenshots/CapturFiles-20180126_012014.png"
    photo3 = "/Users/tarun.lalwani/Documents/screenshots/CapturFiles-20180310_095257.png"
    comp.upload_images(photo1, photo2, photo3)
    comp.remove_image_2()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_citizen_profile():
    cp = CitizenProfilePage()

    cp.navigate().set("ABH", "ab.se@gmail.com").set_city("Amritsar").save()


def test_complain_submitted():
    complaint_subpage = ComplaintSubmittedPage()
    complaint_subpage.navigate()
    print(complaint_subpage.get_complaint_number())
    complaint_subpage.click_continue()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_my_complaints():
    complaints = MyComplaintsPage()
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
    user_reg = RegistrationPage()
    user_reg.navigate()
    user_reg.set("9988776655", "FirstName", "Bathinda").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_language_selection():
    ls = LanguageSelectionPage()
    ls.navigate()
    ls.language("punjabi").language("hindi").language("english").submit()

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/register"


def test_homepage():
    hp = HomePage()

    hp.navigate().new_complaint()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"

    hp.navigate().my_complaints()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/my-complaints.py"


def test_complaintfeedbackpage():
    cf = ComplaintFeedbackPage()
    cf.navigate().star_click(1)
    cf.check_services().check_quality_of_work()
    cf.set("good to go").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/feedback"


def test_complaintunassignedpage():
    cap = ComplaintUnassignPage()
    cap.navigate().assign().reject()

    assert get_url() == "http://egov-micro-dev.egovernments.org/app/stv3/citizen/add-complaint"


def test_login():
    LoginPage().navigate().set("1234567890").submit()
    OTPPage().set("12345").get_started()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_reopen_complaint():
    ReopenComplaintPage().navigate().set("Complaint not resolved").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/complaint-submitted"


def test_navigation():
    LoginPage.navigate().set("9999999999").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    BottomMenuComponent().info().payments().complaints().home()
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    TopMenuNavigationComponent().back()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"

    # this test is for verifying navigation


def test_profile():
    LoginPage().navigate().set("9999999999").submit()
    OTPPage().set("12345").get_started()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"
    TopMenuNavigationComponent().ham()
    LoginPage().profile()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/profile"
    ProfilePage().update("Singh", "def@ulb.in")
    ProfilePage().photo_remove()
    ProfilePage().save()
    TopMenuNavigationComponent().back()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


# def test_complaintreassignpage():
#     crp = ComplaintReassignPage()
#     crp.navigate().reject().assign()


def test_complaintunassignedpage():
    cap = ComplaintUnassignPage()
    cap.navigate().assign().reject()


def test_complaintreassignpage():
    crp = ComplaintReassignPage()
    crp.navigate().reject().assign()
