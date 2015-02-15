from apscheduler.schedulers.blocking import BlockingScheduler
from page_test.models import Company, Images
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    companys = Company.objects.filter(level=1)
    now = datetime.datetime.now()
    for company in companys:
        if company.end < now:
            company.level = 2
            company.save()
        else:
            Images.objects.filter(company)

    print('This job is run every three minutes.')

sched.start()