# The battle of the hashtags

This application allows an administrator to create ‘contests’ between two hashtags, comparing the number of typos in tweets tagged with them.
A programmatic and automated approach is used to fetch tweets from the hashtags in question, on a periodic basis.
After a predetermined amount of time, the winning hashtag will be the one with the smallest total number of typos.

## Structure

- myproject: setting, celery task, main url
- contest: main class
- api: REST API

## Tools
- Django,
- Celery + Redis
- Twitter Search API  + oauth2
- Django REST framework
- Booststrap

## Setup
#### Start a virutal environment

  $ pip install virtualenv
  $ virtualenv test_env
  $ cd test_env
  $ git clone https://github.com/realXiaochen/The-battle-of-the-hashtags.git src
   
## Start server

  $ cd src
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  $ ./manage.py runserver

## Create battle


## Start battle

## View Result

## REST API
