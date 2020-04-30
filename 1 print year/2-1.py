#打印指定年月日
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
endings = ['st','nd','rd']+17*['th']\
    + ['st','nd','rd'] + 7*['th']\
    + ['st']
year = input('Year: ')
month = input('Month: ')
day = input('Day: ')
month_int = int(month)
month_nam = months[month_int-1]
day_int = int(day)
day_nam = day+endings[day_int-1]
print(month_nam + ' ' + day_nam + ' ' + year)