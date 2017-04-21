import json
from selenium import webdriver


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
        self.driver.get("https://sam.ahold.com/pingus_jct/idp/startSSO.ping?PartnerSpId=dingprod")
        # Set the username and password.
        self.driver.find_element_by_id('uid').send_keys(data['username'])
        self.driver.find_element_by_id('password').send_keys(data['password'])
        # Log in.
        self.driver.find_element_by_id('form').submit()

    def load_schedule(self):
        """
        Loads the schedule and returns the content.
        :return: The work schedule in html.
        """
        # Go to the main schedule page.
        self.driver.get("https://sam.ahold.com/wrkbrn_jct/etm/etmMenu.jsp?locale=nl_NL")
        # Click the 'Start' button.
        self.driver.find_element_by_xpath("(//table[@class='imageButton'])[6]").click()
        # Return the schedule html.
        return self.driver.page_source

    def __init__(self):
        """
        Initializes a web client and logs the user in.
        """
        self.driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
        self.__login()
