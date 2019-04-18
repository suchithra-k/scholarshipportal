from __future__ import absolute_import, unicode_literals
from celery import shared_task, task

from .sites import studyportal
from .models import SchedulerAudit

@shared_task
def crawl_data():
    status = False
    remarks = None
    try:
        total = studyportal.crawl_data()
        status = True
        remarks =  '{} data crawled succesfully'.format(total)
    except:
        status = False
        remarks = 'Failed to crawl data'

    SchedulerAudit(task='crawl_data', status=status, remarks=remarks).save()
    return remarks
