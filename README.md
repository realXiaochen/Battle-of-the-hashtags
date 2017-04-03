# The battle of the hashtags

This application allows an administrator to create ‘contests’ between two hashtags, comparing the number of typos in tweets tagged with them.
A programmatic and automated approach is used to fetch tweets from the hashtags in question, on a periodic basis.
After a predetermined amount of time, the winning hashtag will be the one with the smallest total number of typos.

## Structure

- myproject: setting, celery task, main url
- contest: main class
- api: REST API

## Tools
- Django
- Celery + Redis
- Twitter Search API  + oauth2
- Django REST framework
- Booststrap

## Setup
#### Start a virutal environment

    $ pip install virtualenv
    $ virtualenv test_env (or anywhere you want)
    $ cd test_env
    $ source bin/activate
    $ git clone https://github.com/realXiaochen/The-battle-of-the-hashtags.git src
   
## Start server

    $ cd src
    
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    
    $ ./manage.py runserver

## Create a battle

    http://127.0.0.1:8000/admin

- username: admin
- password: 12345678a
- To start a battle, create a 'contest' object, or use the existing '#android vs #google'.
- This app only searches recent/future tweets.


## Start a battle
Open two seperate command line window, enter virtualenv, go to /src

#### Start Redis in one window, as a task pool
    redis-server

#### Start Celery in another, it runs periodical task outside the normal Django cycle
    celery -A myproject worker -l debug
    
## View Result at front-end
    http://127.0.0.1:8000/ (your local host)
    
## REST API

#### Get all battle/contests
    http://127.0.0.1:8000/api/contests
    
#### Get battle/contests by id
Id is visible in admin, I created a object with id 22.

    http://127.0.0.1:8000/api/contests/22
