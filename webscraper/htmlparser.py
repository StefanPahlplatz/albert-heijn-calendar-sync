from bs4 import BeautifulSoup
import yaml
from datetime import datetime
import calendar
import pyrfc3339 as rfc
import pytz


class Parser:

    def block_to_json(self, html, month, year):
        """
        0 = day number      e.g. 19
        1 = start - end     e.g. (18:00 - 21:00) AH 152218:00 ~ 21:00geautoriseerd
        2 = start date      e.g. 18:00
        3 = end date        e.g. 21:00
        
        :param html:
        :param month: 
        :param year: 
        :return: 
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
        timezone = pytz.timezone('Europe/Amsterdam')
        # TODO: clean this up if possible
        startdate = rfc.generate(timezone.localize(datetime(year, month, day, starthour, startmin)), utc=False)
        enddate = rfc.generate(timezone.localize(datetime(year, month, day, endhour, endmin)), utc=False)

        return self.jsonformat.replace('_start', startdate).replace('_end', enddate)

    def __init__(self):
        with open('settings.yaml') as s:
            settings = yaml.load(s)

        self.jsonformat = '{"summary":"_summary","location":"_location","description":"_description",' +\
                          '"start":{"dateTime":"_start"},"end":{"dateTime":"_end"}}'

        self.jsonformat = self.jsonformat.replace('_summary', settings['summary'])\
            .replace('_location', settings['location']).replace('_description', settings['description'])
