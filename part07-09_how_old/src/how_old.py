from datetime import datetime, timedelta


day = int(input('Day:'))
month = int(input('Month:'))
year = int(input('Year:'))

millenium = datetime(1999,12,31)

days_old = (millenium - datetime(year, month, day))

if days_old.days > 0:
    print(f'You were {days_old.days} days old on the eve of the new millennium.')
else:
    print("You weren't born yet on the eve of the new millennium.")