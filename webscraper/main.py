from googlecalendar import Calendar
from albertheijn import AlbertHeijn
from htmlparser import Parser

ah = AlbertHeijn()
parser = Parser()

json = [Parser.block_to_json(element, ah.get_month(), ah.get_year()) for element in ah.get_blocks()]
json = filter(None, json)

print('\n'.join(json))

ah.dispose()
