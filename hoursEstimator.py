print('Thank you for using Hour Estimator.')
inputHoursWorked = input('Enter the number of hours you\'ve worked so far this month(down to the quarter hour):\n')
inputWorkdaysInMonth = input('Input the number of workdays this month:')
# inputMonth = input('Enter the month:\n')
inputHoursIntended = input('Enter the number of hours you intend to work this month(down to the quarter hour):\n')
# inputHoursPerDay = input('Enter the fewest number of hours you want to work per day(down to the quarter hour):\n')

hoursWorked = float(inputHoursWorked)
workdaysInMonth = int(inputWorkdaysInMonth)
# month = str(inputMonth)
hoursIntended = float(inputHoursIntended)
# hoursPerDay = float(inputHoursPerDay)

# monthInHours = 0
# month.lower()
# if month == 'january' or 'march' or 'may' or 'july' or 'august' or 'october' or 'december':
#   monthInHours = 31 * 8
# elif month == 'february'
hoursLeftToWork = hoursIntended - hoursWorked
daysLeftToWork = 0
if hoursLeftToWork % 8 == 0:
  daysLeftToWork = hoursLeftToWork / 8
else:
  daysLeftToWork = hoursLeftToWork // 8 + 1

workdaysLeftInMonth = (workdaysInMonth - (hoursWorked / 8))
averageHoursPerDay = hoursLeftToWork / workdaysLeftInMonth

daysLeftToWork = str(daysLeftToWork)
averageHoursPerDay = str(averageHoursPerDay)
workdaysLeftInMonth = str(workdaysLeftInMonth)
print('You should work at least' + daysLeftToWork + 'more day(s) to hit your monthly goal' )

print('Over the next' + workdaysLeftInMonth + 'work days, you should work an average of' + averageHoursPerDay + 'hours per day to hit your monthly goal')
