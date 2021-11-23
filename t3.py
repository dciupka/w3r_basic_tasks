'''. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''
import datetime
now = datetime.datetime.now()
print(f'Current date and time :\n{now.strftime("%Y-%m-%d %H:%M:%S")}')


print(f'Current date and time :\n{datetime.datetime(2014,7,5,14,34,14)}')


date_today = datetime.date.today()
print(f'Today is: {date_today.strftime("%d %m %Y")}')
print(f'Day is: {date_today.day}')
print(f'Month is: {date_today.month}')
print(f'Year is: {date_today.year}')
print(f'Day of week: {date_today.isoweekday()}')

