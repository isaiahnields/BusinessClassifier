import platform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

OPERATING_SYSTEM = platform.system()

if OPERATING_SYSTEM == 'Windows':
    driver = webdriver.Chrome('C:/Users/imnie/PycharmProjects/BusinessClassifier/drivers/chromedriver.exe')
elif OPERATING_SYSTEM == 'Darwin':
    driver = webdriver.Chrome('C:/Users/imnie/PycharmProjects/BusinessClassifier/drivers/chromedriver_mac')
elif OPERATING_SYSTEM == 'Linux':
    driver = webdriver.Chrome('C:/Users/imnie/PycharmProjects/BusinessClassifier/drivers/chromedriver_linux')
else:
    raise OSError('Operating system must be either Windows, Mac OS, or Linux.')


def class_wait(class_, time):
    """Wait until a specified class element loads in HTML.
    Args:
        class_ (str): The name of the class element in the HTML that needs to be loaded before continuing.
        time (int): The maximum amount of time to wait until an element is loaded.
    Returns:
        element: The element at the specified by the class name
    """
    return WebDriverWait(driver, time).until(
        ec.presence_of_element_located((By.CLASS_NAME, class_))
    )


def xpath_wait(xpath, time):
    """Wait until a specified element loads in HTML.
    Args:
        xpath (str): The xpath to the specified element that needs to be loaded before continuing.
        time (int): The maximum amount of time to wait until an element is loaded.
    Returns:
        element: A list of elements at the specified xpath
    """
    try:
        return WebDriverWait(driver, time).until(
                ec.presence_of_all_elements_located((By.XPATH, xpath))
        )
    except TimeoutException:
        return None


def get_category(term, location):
    """Returns the category of the business being queried.
    Args:
        term (str): The name of the business.
        location (str): The location of the business.
    Returns:
        element: The element at the specified position for the business category
    """
    term.replace(' ', '+')
    location.replace(' ', '+')
    driver.get('https://www.google.com/maps/search/' + term + ' ' + location)
    try:
        class_wait('section-result-content', 5).click()
    finally:
        try:
            try:
                return xpath_wait("//button[@class='widget-pane-link']", 5)[2].text
            except TypeError:
                return 'None'
        except IndexError:
            return 'None'
