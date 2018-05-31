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


def test_logout(citizen_login):
    logout()


def test_open_complaint_and_comment(citizen_login, upload_photo=DEFAULT_IMAGELIST_TWO):
    citizen_login()
    create_new_complaint("No water or electricity in Public Toilet", "Amritsar, Punjab, India ", "Street end",
                         "Leakage of water", upload_photo)
    complain_number = complaint_registration_number_recevied()
    view_my_complaints(complain_number)
    comment_on_complaint("Comments")


def test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_ONE):
    # Create a new complaint
    complaint_type = "Water Body"
    location = "Amritsar, Punjab, India "
    landmark = "Street end"
    additional_details = "Leakage of water"

    create_new_complaint(complaint_type, location, landmark, additional_details, upload_photo)


def test_add_three_image_then_remove_one(citizen_login):
    test_citizen_should_file_complaint_with_one_image(citizen_login, upload_photo=DEFAULT_IMAGELIST_THREE)

# Below tests were commented out, leaving for tests need to be retain or not ?

"""
def test_open_compalint(citizen_login):
    create_new_complaint("Illegal Cutting of Trees", "Amritsar, Punjab, India ", "Street end", "Useful trees")
    complaint_number = complaint_registration_number_recevied()
    open_complaint(complaint_number)


def test_complaint_detail(citizen_login):
    create_new_complaint("Potholes on the Road", "Amritsar, Punjab, India ", "Street end", "Difficult to travel")
    complaint_number = complaint_registration_number_recevied()
    complaint_details(complaint_number)


def test_timeline_details(citizen_login):
    complaint_timeline_details('23/05/2018/000835')

def test_get_all_comaplint(citizen_login):
    get_all_comments("25/05/2018/000861")
    
def test_new_complaint(citizen_login):
    create_new_complaint("Amritsar punjab", "additional details", "Stray Dogs", "StrayDogs", "landmarkdetail", True)

"""
