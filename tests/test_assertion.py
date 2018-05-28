from environment import APP_EMPLOYEE_URL
import time
from pages import *
from pages.employee.common import EmployeeLoginPage


def test_employee_login_assertion():
    emp = EmployeeLoginPage()

    # Test for both the field blank
    emp.navigate().submit()
    assert emp.get_user_name_error_message() == emp.ERROR_MESSAGE.errMsgRequired, "error at username error message for both field blank"
    assert emp.get_password_error_message() == emp.ERROR_MESSAGE.errMsgRequired, "error at password error message for both field blank"

    # Test for password field blank
    emp.employee_id("Amardeep").submit()
    assert emp.get_password_error_message() == emp.ERROR_MESSAGE.errMsgRequired, "error at password error message for password field blank"
    assert emp.get_user_name_error_message() == "", "error at username error message for password field blank"

    #test for username blank
    emp.employee_id(" ").password("12345678").submit()
    assert emp.get_user_name_error_message() == emp.ERROR_MESSAGE.errMsgRequired, "error at username error message for user name blank"
    assert emp.get_password_error_message() == "", "error at password error message for user name blank"

    # Test for Wrong user name  and password
    emp.employee_id("wrongUserName").password("WrongPassword").submit()
    assert emp.get_error_pop_up_message() == emp.ERROR_MESSAGE.errPop, "No pop up message for wrong usename and password"
    assert emp.get_user_name_error_message() == "", "error at username error message for wrong usename and password"
    assert emp.get_password_error_message() == "", "error at password error message for wrong usename and password"

    #test for special case character
    emp.employee_id("enterSpecialCharacter@").password("enterSpecialCharacter!")
    assert emp.get_user_name_error_message() == emp.ERROR_MESSAGE.errMsgEnterValidName, "error at username error message for special character"
    assert emp.get_password_error_message() == emp.ERROR_MESSAGE.errMsgEnterValidPassword, "error at password error message for special character"

def test_open_unassigned_complaint_gro_login():
    EmployeeLoginPage().navigate().employee_id("Amardeep").password("12345678").submit()
    GroHomePage()\
        .click_unassigned_complaint_list()\
        .open_compalint("18/05/2018/000793")

def test_open_assigned_complaint_gro_login():
    EmployeeLoginPage().navigate().employee_id("Amardeep").password("12345678").submit()
    GroHomePage() \
        .click_assigned_complaint_list() \
        .open_compalint("18/05/2018/000809")


def test_get_count_of_assigned_and_unassigned_complaint():
    EmployeeLoginPage().navigate().employee_id("Amardeep").password("12345678").submit()
    time.sleep(2) #TODO
    Gro = GroHomePage()
    print(Gro.get_unassigned_complaint_count())
    print(Gro.get_assigned_complaint_count())
    print(Gro.get_total_complaints())


def test_get_details_from_complaint_list():
    EmployeeLoginPage().navigate().employee_id("Amardeep").password("12345678").submit()
    card = MyComplaintsPage().get_complaint_card("24/05/2018/000851") #TODO
    print(len(card.complain_images()))
    print(card.get_complaint_date())
    print(card.get_complaint_header())
    print(card.get_complaint_no())
    print(card.get_complaint_status())










