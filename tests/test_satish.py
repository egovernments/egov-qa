from framework.selenium_plus import *
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


def test_citizen_login():
    citizen_login('8792101399', "123456")


def test_new_complaint(citizen_login):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):
    # Create a new complaint
    complaint_type = "Water Body"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Leakage of water"

    add_complaint_details(complaint_type, location, landmark, additional_details, upload_photo)


def test_citizen_should_file_complaint_with_two_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO)


def test_citizen_should_file_complaint_with_three_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_citizen_should_file_complaint_without_image(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, [])


def test_add_three_image_then_remove_one(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)


def test_open_compalint(citizen_login):
    open_complaint("25/05/2018/000863")


def test_complaint_detail(citizen_login):
    complaint_details("28/05/2018/000867")


def test_rate_closed_compalint(citizen_login):
    rate_closed_complaint("28/05/2018/000868")


def test_reopen_closed_complaint(citizen_login):
    reopen_closed_complaint("28/05/2018/000869")


def test_timeline_details(citizen_login):
    complaint_timeline_details('23/05/2018/000835')


def test_view_my_complaint(citizen_login):
    view_my_complaint('25/05/2018/000860')


def test_get_all_comaplint(citizen_login):
    get_all_comments("25/05/2018/000861")
