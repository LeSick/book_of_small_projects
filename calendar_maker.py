import datetime


# Setup the constants
DAYS = (
    'Sunday', 'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday'
)
MONTHS = (
    'January', 'February', 'March',
    'April', 'May', 'June', 'July',
    'August', 'September', 'October',
    'November', 'December'
)
print('Calendar Maker by Al Sweigart')

while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def get_calendar_for(year: int, month: str) -> str:
    # Variable contains the string of our calendar to be printed.
    cal_text: str = ''
    # Put the month and year at the top of the calendar:
    cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    # Add days of the week labels to the calendar
    cal_text += (
        '...Monday....Tuesday...Wednesday'
        '...Thursday....Friday....Saturday....Sunday...\n'
    )
    week_separartor: str = ('+----------' * 7) + '+\n'
    blank_row: str = ('|          ' * 7) + '|\n'
    # Get the first date of the month
    current_date: datetime = datetime.date(year, month, 1)

    # Roll back current_date unitl it is Sunday
    while current_date.weekday() != 0:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_separartor

        # day_number_row is the row with the day number labels
        day_number_row: str = ''
        for i in range(7):
            day_number_label: str = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += '|\n'  # Add vertical after Saturday

        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        if current_date.month != month:
            break
    # Add horizontal line at very bottom of the calendar
    cal_text += week_separartor

    return cal_text


cal_text = get_calendar_for(year, month)
print(cal_text)

# Save the calendar
calendar_filename = f'calendar_{year}_{month}.txt'
with open(calendar_filename, 'w') as file_obj:
    file_obj.write(cal_text)

print('Saved to ' + calendar_filename)
