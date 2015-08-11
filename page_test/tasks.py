#!/usr/bin/python
#coding=utf-8

from page_test.models import Company, Images
import datetime, pytz
import requests
from page_test.facebook import set_cover, get_like
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger('page_test')

@periodic_task(run_every=datetime.timedelta(minutes=5))
def timed_job():
    companys = Company.objects.filter(level=1)
    now = datetime.datetime.now()
    for company in companys:
        if company.end < pytz.utc.localize(now):
            company.level = 2
        else:
            photo = Images.objects.get(id=company.current_photo_id)
            new_likes = get_like(company.token, company.id_page)
            photo.likes = photo.likes + new_likes - company.likes
            photo.save()
            company.likes = new_likes
            next_photo = Images.objects.get(company=company,
                                            number=(photo.number + 1) % company.number_photos)
            set_cover(company.user, company, next_photo)
            company.current_photo_id = next_photo.id
        company.save()

if __name__ == '__main__':
    timed_job()