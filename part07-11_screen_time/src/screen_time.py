#this could should be refactored into smaller chunks of functionality.

from datetime import datetime, timedelta

filename = input('Filename:')
start_date = input('Starting date:')
day_count = int(input('How many days:'))

print('Please type in screen time in minutes on each day (TV computer mobile):')

screen_time_list = []
start_date = datetime.strptime(start_date, "%d.%m.%Y")
end_date = start_date + timedelta(days=day_count)
loop_change = timedelta(days=1)


for i in range(int(day_count)):
    daily_input = input('Screen time ' + str(start_date.strftime("%d.%m.%Y")) + ':')
    parts = daily_input.split(' ')
    screen_time_list.append((start_date.strftime("%d.%m.%Y"),parts[0],parts[1],parts[2]))
    start_date = start_date + timedelta(days=1)
    
total_minutes = 0
for item in screen_time_list:
    total_minutes += int(item[1]) + int(item[2]) + int(item[3])

average_minutes = float(total_minutes) / len(screen_time_list)

with open(filename,'w') as new_file:
    new_file.write('Time period: ' + screen_time_list[0][0] + '-' + screen_time_list[-1][0] + '\n')
    new_file.write('Total minutes: ' + str(total_minutes) + '\n')
    new_file.write('Average minutes: ' + str(average_minutes) + '\n')
    for item in screen_time_list:
        new_file.write(item[0] + ': ' + item[1] + '/' + item[2] + '/' + item[3] + '\n')
    new_file.close()

