from __future__ import absolute_import

from datetime import timedelta
from myproject.celery import app
from contests.models import Contest

from celery.task import PeriodicTask
import time


@app.task
def simple_task():
	while True:
		for c in Contest.objects.all():
			c.start_counting()
		time.sleep(15)