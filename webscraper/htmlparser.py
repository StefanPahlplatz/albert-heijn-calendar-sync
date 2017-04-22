from bs4 import BeautifulSoup
import yaml
from datetime import datetime
import calendar
import pyrfc3339 as rfc
import pytz
import json


class Parser:

    def block_to_json(self, html, month, year):
        """
        info index information:
        0 = day number      e.g. 19
        1 = start - end     e.g. (18:00 - 21:00) AH 152218:00 ~ 21:00geautoriseerd
        2 = start date      e.g. 18:00
        3 = end date        e.g. 21:00
        
        :param html: Html text that contains the information from ah.get_blocks()
        :param month: as 3 lettered string e.g. 'Apr'
        :param year: as 4 digit int.
        :return: json representation of the html.
        """
        soup = BeautifulSoup(str(html), 'html.parser')
        if 'calendarCellRegularPast' not in html:
            return None

        # Remove spaces
        info = [span.text.replace('\t', '').replace('\n', '') for span in soup.find_all('span')]

        # Convert the dates
        year = int(year)
        month = list(calendar.month_abbr).index(month[:3])
        day = int(info[0])
        # TODO: clean this up if possible
        starthour, startmin = [int(x) for x in info[2].split(":")]
        endhour, endmin = [int(x) for x in info[3].split(":")]

        # Generate RFC-3339 dates
        # TODO: clean this up if possible
        startdate = rfc.generate(self.timezone.localize(datetime(year, month, day, starthour, startmin)), utc=False)
        enddate = rfc.generate(self.timezone.localize(datetime(year, month, day, endhour, endmin)), utc=False)

        return json.loads(self.jsonformat.replace('_start', startdate).replace('_end', enddate))

    def __init__(self):
        """
        Initialized the parser by creaing the json format 
        and initializing the timezone.
        """
        with open('settings.yaml') as s:
            settings = yaml.load(s)

        # Json format for google calendar.
        self.jsonformat = '{"summary":"_summary","location":"_location","description":"Event created by ' +\
                          'Stefan Pahlplatz\'s webscraper.","start":{"dateTime":"_start"},"end":{"dateTime":"_end"}}'

        # Replace default values with user settings.
        self.jsonformat = self.jsonformat.replace('_summary', settings['summary'])\
            .replace('_location', settings['location'])\

        # Set the timezone.
        self.timezone = pytz.timezone(settings['timezone'])
