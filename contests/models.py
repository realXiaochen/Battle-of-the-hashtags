from django.db import models
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils import timezone
from django.core.exceptions import ValidationError 
from datetime import datetime, timedelta
import enchant
import json
import oauth2 as oauth
import re
import time


class Contest(models.Model):
	hashtag_1 = models.CharField(max_length=20,default = "")
	hashtag_2 = models.CharField(max_length=20,default = "")
	start_time = models.DateTimeField(default=now)
	end_time = models.DateTimeField(default=now)
	c1 = models.IntegerField(default = 0)
	c2 = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self): 
		h1,h2 = str(self.hashtag_1),str(self.hashtag_2) 
		if not h1.startswith('#'):h1 = "#" + h1
		if not h2.startswith('#'):h2 = "#" + h2
		return str(h1) + " vs " + str(h2)

	def __unicode__(self):  
		h1,h2 = str(self.hashtag_1),str(self.hashtag_2) 
		if not h1.startswith('#'):h1 = "#" + h1
		if not h2.startswith('#'):h2 = "#" + h2
		return str(h1) + " vs " + str(h2)

	def clean(self):
		if (self.end_time -self.start_time).total_seconds()<0:
			msg = u"End time should be greater than start time."
			raise ValidationError(msg)
		if (timezone.now() - self.end_time).total_seconds()>0:
			msg = u"Sorry, can't search history tweets"
			raise ValidationError(msg)

	def add_1(self,n):
		self.c1 += n

	def add_2(self,n):
		self.c2 += n

	def start_counting(self):
		# Twitter REST API
		CONSUMER_KEY = 'CnmZDwmnx9KenyOXJKgNFVZFd'
		CONSUMER_SECRET = 'mk6vx0ikuGnexJOjbRdpMULFzU0qDbBsWJDmTP6qZ35BQrExn6'
		ACCESS_KEY = '4173869540-WJgplWGRwdL4DAXta0FNTxEgYaFJbz1ccsghcEc'
		ACCESS_SECRET = 'DGxljC5DZddQuwbflIZ485fNL4P7MTHWKjYcrf3TDmVAP'

		consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
		access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
		client = oauth.Client(consumer, access_token)

		h = [str(self.hashtag_1),str(self.hashtag_2)]
		for e in h:
			if e.startswith('#'):e = e[1:]
		c = [0,0]
		d = enchant.Dict("en_US")
		d.check('fuckoff')
		for idx,tag in enumerate(h):
			url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23' + tag + '&result_type=recent'
			response, data = client.request(url)
			tweets = json.loads(data)
			for tweet in  tweets['statuses']:
				line = tweet['text']

				#remove url
				new_line = re.sub(r"http\S+", "", line)

				#remove emoji
				emoji_pattern = re.compile(
				u"(\ud83d[\ude00-\ude4f])|"  # emoticons
				u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
				u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
				u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
				u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
				"+", flags=re.UNICODE)

				new_line = re.sub(emoji_pattern, "", new_line)

				#find words
				word_list=re.findall(r'[a-zA-Z]+', new_line)

				#count typo
				for word in word_list: 
					if not d.check(word):c[idx]+=1

		self.add_1(c[0])
		self.add_2(c[1])
		self.save()
		print self.c1
		print self.c2





# @receiver(models.signals.post_save, sender=Contest)
# def execute_after_save(sender, instance, created, *args, **kwargs):
# 	if created:
# 		while((timezone.now() - instance.end_time).total_seconds()<0):
# 			if (timezone.now() - instance.start_time).total_seconds()>0:
# 				start_counting(instance)
# 			print "wait for 15 secs"
# 			time.sleep(15)

# @receiver(models.signals.post_save, sender=Contest)
# def execute_after_save(sender, instance, created, *args, **kwargs):
# 	if created:
# 		return





