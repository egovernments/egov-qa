from pytest import fixture

from environment import *
import time
from pages import *
from pages.employee.Login import *


@fixture
def login_citizen(username=None, otp=None):
    username = username or DEFAULT_CITIZEN_USERNAME
    otp = otp or DEFAULT_FIXED_OTP
    loginpage=LoginPage()
    loginpage.navigate()

    loginpage.set(username)
    loginpage.submit()
    otppage=OTPPage()
    otppage.set(otp)
    otppage.get_started()







   # yield
   # logout


def create_new_complaint(location,additional_details,complaint_type_search,complaint_type_select,landmark,flag_submit_complaint=True):
    addcomplaintpage=AddComplaintPage()

    HomePage().new_complaint()
    addcomplaintpage.set_location_by_address(location)
    addcomplaintpage.set_complaint_details(additional_details)
    addcomplaintpage.set_landmark_details(landmark)
    addcomplaintpage.set_complaint_type(complaint_type_search, complaint_type_select)
    image1="/home/satish/Pictures/bank1.png"
    image2="/home/satish/Pictures/bank1.png"
    image3="/home/satish/Pictures/bank1.png"
    addcomplaintpage.upload_images(image1,image2,image3)

    time.sleep(3)
    addcomplaintpage.submit()



def create_new_complaint_by_plus_icon(location,additional_details,complaint_type_search,complaint_type_select,landmark,flag_submit_complaint=True):
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


def comment_on_given_complaint(my_complaint_number):
    HomePage().my_complaints()
    all_complaint = MyComplaintsPage().get_all_complaints()
    print(all_complaint)
    complaint_number=[]

    for i in all_complaint:
        complaint_number.append(i.get_complaint_no())
    complaint_index = complaint_number.index(my_complaint_number)
    all_complaint[complaint_index].track_complaint()
    MyComplaintsPage().comment("hey you are done with complaint")
    MyComplaintsPage().sendcomment()



@fixture
def logout_citizen():
    yield
    LogoutPage().navigate()
    TopMenuNavigationComponent().ham()
    LogoutPage().submit()



def login_gro(username=None,password=None):
    username1 = username
    password1=password
    print(username1)
    print(password1)
    le=LoginEmployeePage()
    le.navigate()
    print("in function")
