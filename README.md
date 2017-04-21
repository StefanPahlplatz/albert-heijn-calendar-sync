# albert-heijn-calendar-sync

# How to use

Change your settings in `webscraper/settings.yaml`

Make sure you have [geckodriver](https://github.com/mozilla/geckodriver/releases), 
[Firefox](https://www.mozilla.org/nl/firefox/new/)
and the required [dependencies](#Depencencies) installed.

[Request](https://console.developers.google.com/flows/enableapi?apiid=calendar)
a google calendar api key and store the `client_secret.json` in `webscraper/`. ([Guide on how to request a key](https://developers.google.com/google-apps/calendar/quickstart/python))


# Depencencies

Google Client Library: `pip install --upgrade google-api-python-client`

Requests: `pip install requests`

Httplib2: `pip install httplib2`

Six: `pip install six`

Uritemplate: `pip install uritemplate`

pyRFC3339: `pip install pyrfc3339`