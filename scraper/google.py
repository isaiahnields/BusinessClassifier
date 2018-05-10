import os
import platform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Google:
    def __init__(self):

        # determines the operating system that the program is running on
        self.operating_system = platform.system()

        # get the directory of the current file
        root_dir = os.path.dirname(os.path.abspath(__file__))[:50]

        # loads chromedriver for the appropriate operating system
        if self.operating_system == 'Windows':
            self.driver = webdriver.Chrome(root_dir + '/drivers/chromedriver.exe')
        elif self.operating_system == 'Darwin':
            self.driver = webdriver.Chrome(root_dir + '/drivers/chromedriver_mac')
        elif self.operating_system == 'Linux':
            self.driver = webdriver.Chrome(root_dir + '/drivers/chromedriver_linux')
        else:
            raise OSError('Operating system must be either Windows, Mac OS, or Linux.')

    def class_wait(self, class_, time):
        """
        Wait until a specified class element loads in HTML.

        :param class_: The name of the class element in the HTML that needs to be loaded before continuing.
        :param time: The maximum amount of time to wait until an element is loaded.
        :return element: The element at the specified by the class name
        """
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located((By.CLASS_NAME, class_))
        )

    def xpath_wait(self, xpath, time):
        """
        Wait until a specified element loads in HTML.

        :param xpath: The xpath to the specified element that needs to be loaded before continuing.
        :param time: The maximum amount of time to wait until an element is loaded.
        :return element: A list of elements at the specified xpath
        """
        try:
            return WebDriverWait(self.driver, time).until(
                    ec.presence_of_all_elements_located((By.XPATH, xpath))
            )
        except TimeoutException:
            return None

    def get_category(self, term, location):
        """
        Returns the category of the business being queried.

        :param term: The name of the business.
        :param location: The location of the business.
        :return element: The element at the specified position for the business category
        """
        term.replace(' ', '+')
        location.replace(' ', '+')
        self.driver.get('https://www.google.com/maps/search/' + term + ' ' + location)
        try:
            self.class_wait('section-result-content', 5).click()
        finally:
            try:
                try:
                    return [self.xpath_wait("//h1[@class='section-hero-header-title']", 5)[0].text,
                            self.xpath_wait("//button[@class='widget-pane-link']", 5)[2].text]
                except TypeError:
                    return ['None', 'None']
            except IndexError:
                return ['None', 'None']
