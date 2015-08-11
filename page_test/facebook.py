import json
from datetime import datetime
import requests
import logging

logger = logging.getLogger('page_test')

def strToDate(date):
    dat, t = date.strip().split()
    y, mon, d = dat.split('/')
    h, m = t.split(':')
    return datetime(int(y), int(mon), int(d), int(h), int(m))

def get_like(token, id_page):
    base_url = 'https://graph.facebook.com/' + id_page
    url = '%s?access_token=%s' % (base_url, token,)
    logger.info(url)
    content = requests.get(url).json()
    logger.info(content)
    return int(content['likes'])

def get_album_cover(token, id_page):
    base_url = 'https://graph.facebook.com/' + id_page + "/albums"
    url = '%s?access_token=%s' % (base_url, token,)
    logger.info(url)
    content = requests.get(url).json()
    for d in content['data']:
        if d["name"] == "Cover Photos":
            return d["id"]
    logger.info(content)
    return ''

def set_cover(user, company, cover):
    fields = {
        'cover':cover.id_photo,
        'access_token':company.token,
        'no_notification':True,
        'no_feed_story':True,
    }
    base_url = 'https://graph.facebook.com/v2.4/' + company.id_page
    logger.info(base_url)
    logger.info(fields)
    content = requests.post(base_url, fields)
    logger.info(content.json())