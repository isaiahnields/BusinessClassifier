import os
import platform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# determines the operating system that the program is running on
OPERATING_SYSTEM = platform.system()

# get the directory of the current file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))[:50]

# loads chromedriver for the appropriate operating system
if OPERATING_SYSTEM == 'Windows':
    driver = webdriver.Chrome(ROOT_DIR + '/drivers/chromedriver.exe')
elif OPERATING_SYSTEM == 'Darwin':
    driver = webdriver.Chrome(ROOT_DIR + '/drivers/chromedriver_mac')
elif OPERATING_SYSTEM == 'Linux':
    driver = webdriver.Chrome(ROOT_DIR + '/drivers/chromedriver_linux')
else:
    raise OSError('Operating system must be either Windows, Mac OS, or Linux.')


def class_wait(class_, time):
    """
    Wait until a specified class element loads in HTML.

    :param class: The name of the class element in the HTML that needs to be loaded before continuing.
    :param time: The maximum amount of time to wait until an element is loaded.
    :return element: The element at the specified by the class name
    """
    return WebDriverWait(driver, time).until(
        ec.presence_of_element_located((By.CLASS_NAME, class_))
    )


def xpath_wait(xpath, time):
    """
    Wait until a specified element loads in HTML.

    :param xpath: The xpath to the specified element that needs to be loaded before continuing.
    :param time: The maximum amount of time to wait until an element is loaded.
    :return element: A list of elements at the specified xpath
    """
    try:
        return WebDriverWait(driver, time).until(
                ec.presence_of_all_elements_located((By.XPATH, xpath))
        )
    except TimeoutException:
        return None


def get_category(term, location):
    """
    Returns the category of the business being queried.

    :param term: The name of the business.
    :param location: The location of the business.
    :return element: The element at the specified position for the business category
    """
    term.replace(' ', '+')
    location.replace(' ', '+')
    driver.get('https://www.google.com/maps/search/' + term + ' ' + location)
    try:
        class_wait('section-result-content', 5).click()
    finally:
        try:
            try:
                return [xpath_wait("//h1[@class='section-hero-header-title']", 5)[0].text,
                        xpath_wait("//button[@class='widget-pane-link']", 5)[2].text]
            except TypeError:
                return ['None', 'None']
        except IndexError:
            return ['None', 'None']
