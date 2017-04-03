# The battle of the hashtags

This application allows an administrator to create ‘contests’ between two hashtags, comparing the number of typos in tweets tagged with them.

A programmatic and automated approach is used to fetch tweets from the hashtags in question, on a periodic basis.

After a predetermined amount of time, the winning hashtag will be the one with the smallest total number of typos.

Tested only in Mac OS.

## Structure

/myproject

    Project setting, Celery task, Main url
    
/contest

    Main class, Twitter stuff

/api

    REST API

## Tools
- Django
- Celery + Redis
- Twitter Search API  + oauth2 (rate limit)
- Django REST framework
- Booststrap

## Setup

    $ pip install virtualenv
    $ virtualenv test_env (or anywhere you want)
    $ cd test_env
    $ source bin/activate
    $ git clone https://github.com/realXiaochen/The-battle-of-the-hashtags.git src
   
## Start the server

    $ cd src
    $ pip install -r requirements.txt
    
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    
    $ ./manage.py runserver

## Create a battle

    http://127.0.0.1:8000/admin    (your_localhost/admin)
    
    
- username: admin
- password: 12345678a
- To start a battle, create a 'contest' object, or use the existing '#android vs #google'.
- This app only searches recent/future tweets.


## Start a battle
Open two seperate command line window, enter virtualenv, go to /src

Start Redis in one window, as a task pool

    $ redis-server

Start Celery in another, it runs periodical tasks.

Because of rate limit, only one battle/contest will do the counting every 15s.

    $ celery -A myproject worker -l debug
    
## Battle results
Go to localhost, no ajax, please refreash.

    http://127.0.0.1:8000/
    
## REST API

Get all results

    http://127.0.0.1:8000/api/contests
    
Get result by id(visible in admin)

    http://127.0.0.1:8000/api/contests/22

 Authentication & Permissions
 
    Not enough time.
