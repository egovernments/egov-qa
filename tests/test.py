from pytest import fixture

from pages import *

from framework.selenium_plus import *
from pages.employee.Login import *

from pages.flows.common import *
import time


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
    print(get_url())
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


def test_create_complaint():
    comp = AddComplaintPage()
    comp.navigate()
    comp.set_complaint_type("Overflowing Garbage Bins")
    comp.set_location_by_address("Homigo Ant")
    photo1 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    photo2 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    photo3 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"

    comp.upload_images(photo1, photo2, photo3)
    comp.remove_image_2()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_citizen_profile():
    cp = CitizenProfilePage()
    cp.navigate().set("ABH", "satishkrgu95@gmail.com").set_city("Amritsar").save()


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
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/my-complaints"


def test_complaintfeedbackpage():
    cf = ComplaintFeedbackPage()
    cf.navigate().star_click(4)
    cf.check_services().check_quality_of_work().check_resolution_time().check_others()
    cf.set("good to go").submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/feedback"


def test_login():
    LoginPage().navigate().set("8792101399").submit()
    OTPPage().set("123456").get_started()
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen"


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


def test_complaintunassignedpage():
    cap = ComplaintUnassignPage()
    cap.navigate().assign().reject()


def test_complaintreassignpage():
    crp = ComplaintReassignPage()
    crp.navigate().reject().assign().set("ok")


def test_register_mobile_less10():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set(876543, 'satish', 'Amritsar')
    reg.submit()
    print(get_url())
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_register_mobile_greater10():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set(87654398887773333, 'satish', 'Amritsar')
    reg.submit()
    print(get_url())
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_register_mobile_withspecialchar():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set("876543Lhkjh", 'satish', 'Amritsar')
    reg.submit()
    print(get_url())
    # assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/user/otp"


def test_duplicate_mobilenumber():
    LanguageSelectionPage().navigate().language("english").submit()
    reg = RegistrationPage()
    reg.navigate().set("8792101399", 'satish', 'Amritsar').submit()
    reg.navigate().set("8792101399", 'satish', 'Amritsar').submit()


def test_create_complaint():
    comp = AddComplaintPage()
    comp.navigate()
    comp.set_complaint_type("Overflowing Garbage Bins")
    comp.set_location_by_address("Homigo Ant")
    photo1 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    photo2 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    photo3 = "/home/satish/UDEMY/UdemyProject/Book/static/Book/back1.jpg"
    UploadImageComponent().upload_images(photo1, photo2, photo3)
    comp.set_landmark_details("landmark details")
    comp.set_complaint_details("complain details")
    comp.submit()
    assert get_url() == "http://egov-micro-dev.egovernments.org/app/v3/citizen/add-complaint"


def test_create_complaintsatish():
    com = AddComplaintPage()
    LoginPage().navigate().set("8792101399").submit()
    OTPPage().set("123456").get_started()
    CreateComplaintSatish().new_complaint()
    com.set_complaint_type("Stray Dogs", "StrayDogs")
    com.set_location_by_address("Amritsar, Punjab, India")
    time.sleep(3)  # TO-DO Remove the time delay
    com.set_landmark_details("landmark details")
    com.set_complaint_details("complain details")
    com.submit()
    print(ComplaintSubmittedPage().get_complaint_number())

    ComplaintSubmittedPage().click_continue()


def test_citizen_login():
    login_citizen('8792101399', "123456")


def test_new_complaint(login_citizen):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail",True)

def test_new_complaint_by_plus_icon(login_citizen):
    create_new_complaint_by_plus_icon( "Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs","landmarkdetail", True)


def test_open_complaint_and_comment(login_citizen, logout_citizen):
    complain_number="09/05/2018/000652"
    comment_on_given_complaint(complain_number)


def test_logout(login_citizen):
    logout_citizen()



def test_complaint_register_to_resolve(login_citizen):

    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)
    complain_number=ComplaintSubmittedPage().get_complaint_number()
    print(complain_number)
    logout_citizen()
    print("done")
    login_gro("9090909010","murali@1993")








