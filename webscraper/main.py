from googlecalendar import Calendar
from albertheijn import AlbertHeijn
from htmlparser import Parser

# Create scraper objects.
ah = AlbertHeijn()
parser = Parser()

# Convert all blocks to json format.
json = filter(None, [parser.block_to_json(element, ah.get_month(), ah.get_year()) for element in ah.get_blocks()])

calendar = Calendar()
print('Updating calendar...')
for event in json:
    calendar.insert_event(event)

print('Done')

ah.dispose()
