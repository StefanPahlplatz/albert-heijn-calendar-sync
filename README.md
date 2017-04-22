# albert-heijn-calendar-sync

# How to use

- Change your settings in `webscraper/settings.yaml`
    - Change the albert-heijn credentials.
    - Change the path to [PhantomJS](http://phantomjs.org/download.html).
    
- [Request](https://console.developers.google.com/flows/enableapi?apiid=calendar)
a google calendar api key and store the `client_secret.json` in `webscraper/`. ([Guide on how to request a key](https://developers.google.com/google-apps/calendar/quickstart/python))
- Install the required depencencies.


# Depencencies

Google Client Library: `pip install --upgrade google-api-python-client`

Selenium: `pip install selenium`

Beautifulsoup4: `pip install beautifulsoup4`

PyYAML `pip install pyyaml`

Requests: `pip install requests`

Httplib2: `pip install httplib2`

Six: `pip install six`

Uritemplate: `pip install uritemplate`

pyRFC3339: `pip install pyrfc3339`

pytz: `pip install pytz`

# View the browser

- Change the `showbrowser` setting in `webscraper/settings.yaml` to true
- Change `geckopath` to your [geckodriver](https://github.com/mozilla/geckodriver/releases) path.
- Make sure you have [Firefox](https://www.mozilla.org/nl/firefox/new/) installed.