from googlecalendar import Calendar
from albertheijn import AlbertHeijn
from htmlparser import Parser

# Create scraper objects.
ah = AlbertHeijn()
parser = Parser()

# Convert all blocks to json format.
json = filter(None, [parser.block_to_json(element, ah.get_month(), ah.get_year()) for element in ah.get_blocks()])

print('\n'.join(json))

ah.dispose()
