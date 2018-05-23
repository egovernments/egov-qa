from environment import APP_EMPLOYEE_URL
from pages import GroHomePage
from pages.employee.common import EmployeeLoginPage


def test_employee_login_assertion():
    emp = EmployeeLoginPage()

    # Test for both the field blank
    emp.navigate(APP_EMPLOYEE_URL).submit()
    assert emp.get_user_name_error_message() == emp.ERRORMESSAGE.errMsgRequired, "error at username error message for both field blank"
    assert emp.get_password_error_message() == emp.ERRORMESSAGE.errMsgRequired,  "error at password error message for both field blank"

    # Test for password field blank
    emp.employee_id("Amardeep").submit()
    assert emp.get_password_error_message() == emp.ERRORMESSAGE.errMsgRequired, "error at password error message for password field blank"
    assert emp.get_user_name_error_message() == "", "error at username error message for password field blank"

    #test for username blank
    emp.employee_id(" ").password("12345678").submit()
    assert emp.get_user_name_error_message() == emp.ERRORMESSAGE.errMsgRequired, "error at username error message for user name blank"
    assert emp.get_password_error_message() == "", "error at password error message for user name blank"

    # Test for Wrong user name  and password
    emp.employee_id("wrongUserName").password("WrongPassword").submit()
    assert emp.get_error_pop_up_message() == emp.ERRORMESSAGE.errPop, "No pop up message for wrong usename and password"
    assert emp.get_user_name_error_message() == "", "error at username error message for wrong usename and password"
    assert emp.get_password_error_message() == "", "error at password error message for wrong usename and password"

    #test for special case character
    emp.employee_id("enterSpecialCharacter@").password("enterSpecialCharacter!")
    assert emp.get_user_name_error_message() == emp.ERRORMESSAGE.errMsgEnterValidName, "error at username error message for special character"
    assert emp.get_password_error_message() == emp.ERRORMESSAGE.errMsgEnterValidPassword, "error at password error message for special character"

def test_yo():
    EmployeeLoginPage().navigate(APP_EMPLOYEE_URL).employee_id("Amardeep").password("12345678").submit()
    GroHomePage()\
        .click_unassigned_complaint_list()\
        .open_compalint("18/05/2018/000793")










