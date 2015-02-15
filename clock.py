from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from apscheduler.schedulers.blocking import BlockingScheduler
from page_test.models import Company, Images
import datetime, pytz
import requests

# sched = BlockingScheduler()

def set_cover(user, company, cover):
    fields = {
        'cover':cover.id_photo, 
        'access_token':company.token,
        'no_notification':True,
        'no_feed_story':True,
    }
    base_url = 'https://graph.facebook.com/' + company.id_page
    content = requests.post(base_url, fields)

def get_like(company):
    base_url = 'https://graph.facebook.com/' + company.id_page
    url = '%s?access_token=%s' % (base_url, company.token,)
    content = requests.get(url).json()
    return int(content['likes'])

# @sched.scheduled_job('interval', minutes=1)
def timed_job():
    companys = Company.objects.filter(level=1)
    now = datetime.datetime.now()
    for company in companys:
        if company.end < pytz.utc.localize(now):
            company.level = 2
        else:            
            photo = Images.objects.get(id=company.current_photo_id)
            new_likes = get_like(company)
            photo.likes = photo.likes + new_likes - company.likes
            photo.save()
            company.likes = new_likes
            next_photo = Images.objects.get(company=company, 
                                            number=(photo.number + 1) % company.number_photos)
            set_cover(company.user, company, next_photo)
            company.current_photo_id = next_photo.id
        company.save()

# sched.start()

if __name__ == '__main__':
    timed_job()