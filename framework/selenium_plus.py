import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, \
    TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

__author__ = 'Tarun'

default_timeout = 10
driver = None


class count_zero_or_invisible(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elems = driver.find_elements(*self.locator)
            if len(elems) == 0:
                return True
            else:
                for elem in elems:
                    if elem.is_displayed():
                        return False
                return True
        except StaleElementReferenceException:
            return False


class count_non_zero_and_visible(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elems = driver.find_elements(*self.locator)
            if not elems or len(elems) == 0:
                return False
            else:
                for elem in elems:
                    if elem.is_displayed():
                        return elems
                return False
        except StaleElementReferenceException:
            return False


class count_non_zero_and_clickable(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elems = driver.find_elements(*self.locator)
            if not elems or len(elems) == 0:
                return False
            else:
                for elem in elems:
                    if elem.is_displayed() and elem.is_enabled():
                        return elems
                return False
        except StaleElementReferenceException:
            return False


def get_context():
    return get_driver()


def goto(url):
    get_context().get(url)


map_locator_to_by = {
    "id": By.ID,
    "class": By.CLASS_NAME,
    "css": By.CSS_SELECTOR,
    "xpath": By.XPATH,
    "linktext": By.LINK_TEXT,
    "text": By.LINK_TEXT,
    "partialtext": By.PARTIAL_LINK_TEXT,
    "partiallinktext": By.PARTIAL_LINK_TEXT,
    "name": By.NAME,
    "tag": By.TAG_NAME,
    "tagname": By.TAG_NAME
}


def get_identifier(identifier):
    locator = "css"
    locator_value = ""

    if isinstance(identifier, dict):
        if 'locator' not in identifier:
            raise ValueError(
                "The identifier has no specified locator - {}".format(
                    identifier))
        identifier = identifier['locator']

    if isinstance(identifier, str):
        identify = identifier.split('=', 1)
        if len(identify) == 1:
            locator_value = identify[0]
        else:
            locator = identify[0]
            locator_value = identify[1]

    if not locator.lower() in map_locator_to_by:
        locator = "css"
        locator_value = identifier

    return (map_locator_to_by[locator], locator_value)


def click(identifier, context=None, timeout=-1, scroll_in_view=False):
    if scroll_in_view:
        elem = scroll_into_view(identifier, context=context, timeout=timeout)
    else:
        elem = find(identifier, context, timeout, EC.element_to_be_clickable)

    elem.click()


def exists(identifier, context=None, timeout=-1, condition=EC.presence_of_element_located):
    return find(identifier, context, timeout, condition)


def set(identifier, text, context=None, timeout=-1):
    elem = find(identifier, context, timeout)
    elem.clear()
    elem.send_keys(text)


def finds(identifier, context=None, timeout=-1, condition=None):
    """
        @return: Returns the web element found by identifier
        @rtype: selenium.webdriver.remote.webelement.WebElement
    """
    if timeout == -1:
        timeout = default_timeout

    if isinstance(identifier, WebElement):
        return identifier

    if context is None:
        context = driver

    locator = get_identifier(identifier)

    if condition is None:
        condition = count_non_zero_and_visible(locator)
    else:
        condition = condition(locator)

    wdw = WebDriverWait(driver, timeout)

    try:
        elems = wdw.until(condition)
        return elems if isinstance(elems, list) else []

    except TimeoutException:
        return []


def wait_any(identifiers, **kwargs):
    timeout = kwargs.get('timeout', default_timeout)
    if 'timeout' in kwargs:
        del kwargs['timeout']

    time_start = time.time()

    while True:
        for identifier in identifiers:
            try:
                find(identifier, timeout=0, **kwargs)
                return True
            except Exception as ex:
                pass
        if time.time() - time_start > timeout:
            return False
    return False


def find(identifier, context=None, timeout=-1,
         condition=EC.presence_of_element_located):
    """
        @return: Returns the web element found by identifier
        @rtype: selenium.webdriver.remote.webelement.WebElement
    """
    if timeout == -1:
        timeout = default_timeout

    if isinstance(identifier, WebElement):
        return identifier

    if context is None:
        context = driver
    elif context is str:
        context = find(context)

    locator = get_identifier(identifier)
    wdw = WebDriverWait(driver=context, timeout=timeout)
    try:
        element = wdw.until(condition(locator))
    except Exception as ex:
        element = context.find_element(*locator)
        return element
        raise
    return element


def refresh_page():
    get_context().refresh()


def init_driver(param_driver):
    """
        @type driver: RemoteWebDriver
    """
    global driver
    driver = param_driver
    driver.implicitly_wait(0)


def get_driver():
    """
        @rtype: selenium.webdriver.remote.WebDriver
    """
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        init_driver(driver)
    return driver


def scroll_into_view(elem_or_identifier, **kwargs):
    elem = find(elem_or_identifier, **kwargs)
    execute_script(
        "arguments[0].scrollIntoView()",
        elem
    )
    return elem


def quit_driver():
    global driver
    if driver:
        driver.quit()
        driver = None


def execute_script(text, args=None):
    if args is None:
        args = []
    return get_driver().execute_script(text, args)


def take_screen_shot(path):
    return get_driver().save_screenshot(path)


def get_page_source():
    return get_driver().page_source


def get_url():
    return get_driver().current_url


def get(elem, **kwargs):
    return find(elem, **kwargs).text


def unhide(identifier, **kwargs):
    elem = find(identifier, **kwargs)
    execute_script("""
        var elem = arguments[0];
        elem.style.display = "";
        elem.style.visibility = "";
    """, elem)
    return elem


def get_html(identifier, context=None, timeout=-1):
    return execute_script("return arguments[0].outerHTML", find(identifier, context=context, timeout=timeout))
