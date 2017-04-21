import json
import requests


class AlbertHeijn:

    def __init__(self):
        with open('credentials.json') as data_file:
            data = json.load(data_file)

        payload = {
            'action': 'login',
            'username': data['username'],
            'password': data['password']
        }

        self.session = requests.session()
        self.session.post('https://sam.ahold.com/pingus_jct/idp/startSSO.ping?PartnerSpId=dingprod', data=payload)
        response = self.session.get('https://sam.ahold.com/wrkbrn_jct/etm/etmMenu.jsp?locale=nl_NL')

        print(response.text)
