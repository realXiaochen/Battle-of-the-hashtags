This program will periodically get recent tweets about the competing hashtags, parse and count the typo within.


Back-End

	Periodic task running in background of Django: 
		Celery
		Redis

	Geting tweets: 
		Twitter REST API (my account has rate limit)
		oauth2

	Parsing and Counting typo: 
		re
		enchant

Front-End

	Bootstrap



Environment Setup


How to use it

	start django server: './manage.py runserver'
	
	CRUD of Battle
		http://127.0.0.1:8000/admin  (localhost/admin)
		user name: admin
		password: 12345678a
	

	Starting of battle
		start redis: 'redis-server'
		start celery:  'celery -A myproject worker -l debug'

	Battle results: 
		http://127.0.0.1:8000/ (localhost)
		Period is set at 15s because of rate limit.
		No ajax :(, please refreash.

	REST API






