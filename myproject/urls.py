"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from contests.views import ContestListView
from django.conf.urls import url,include
from django.contrib import admin
from django.http import HttpResponseRedirect
from .tasks import simple_task
from api import urls as api_urls

urlpatterns = [
	# url(r'api/',lambda r: HttpResponseRedirect('api/')),
	url(r'api/',include(api_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^$',ContestListView.as_view(), name = "contests"),
]

# hello_world.delay()
simple_task.delay()

