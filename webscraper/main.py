from googlecalendar import Calendar
from albertheijn import AlbertHeijn

ah = AlbertHeijn()
schedule = ah.load_schedule()
print(schedule)
