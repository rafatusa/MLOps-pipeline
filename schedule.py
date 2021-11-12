from crontab import CronTab

duration = 6 # here 6 is for 6 min this will be changed as required
cron = CronTab(user='root')
job = cron.new(command='python /models/model.py')
job.minute.every(duration)

cron.write()