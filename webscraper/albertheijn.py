import json
import time
from selenium import webdriver

LOGINPAGE = "https://sam.ahold.com/pingus_jct/idp/startSSO.ping?PartnerSpId=dingprod"
REDIRECTPAGE = "https://sam.ahold.com/wrkbrn_jct/etm/etmMenu.jsp?locale=nl_NL"
SCHEDULEPAGE = "https://sam.ahold.com/etm/time/timesheet/etmTnsMonth.jsp"


class AlbertHeijn:
    def __login(self):
        """
        Logs the user in so he can access the schedule later on.
        :return: 
        """
        # Load the AH credentials.
        with open('credentials.json') as data_file:
            data = json.load(data_file)
        # Create a firefox driver.
        self.driver.get(LOGINPAGE)
        # Set the username and password.
        self.driver.find_element_by_id('uid').send_keys(data['username'])
        self.driver.find_element_by_id('password').send_keys(data['password'])
        # Log in.
        self.driver.find_element_by_id('form').submit()
        time.sleep(1)

    def __load_schedule(self):
        """
        Loads the schedule and returns the content.
        :return: The work schedule in html.
        """
        # Go to the main schedule page.
        self.driver.get(REDIRECTPAGE)
        # Click the 'Start' button.
        self.driver.find_element_by_xpath("(//table[@class='imageButton'])[6]").click()
        time.sleep(1)

    def __init__(self):
        """
        Initializes a web client and logs the user in.
        """
        self.driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
        self.__login()
        self.__load_schedule()

    def get_blocks(self):
        """
        Gets all the blocks from the schedule.
        :return: All blocks in a list.
        """
        all_elements_container = self.driver.find_elements_by_xpath("//td[@height=\"62\"][@valign=\"top\"]")
        return [element.get_attribute('outerHTML') for element in all_elements_container]

    def get_month(self):
        """
        Gets the month the schedule is displaying.
        :return: The month. 
        """
        if self.driver.current_url != SCHEDULEPAGE:
            print("Can't get the month if we're not on the schedule page. Aborting...")
            exit(2)
        return self.driver.find_element_by_class_name('calMonthTitle').get_attribute('innerHTML')

    def get_year(self):
        """
        Gets the year the schedule is displaying.
        :return: The year. 
        """
        if self.driver.current_url != SCHEDULEPAGE:
            print("Can't get the year if we're not on the schedule page. Aborting...")
            exit(3)
        return self.driver.find_element_by_class_name('calYearTitle').get_attribute('innerHTML')

    def dispose(self):
        """
        Closes the browser window and ends the driver process.
        """
        self.driver.quit()
