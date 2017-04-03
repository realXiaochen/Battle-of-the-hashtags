from django.conf.urls import url
from .views import contest_list,contest_detail

urlpatterns = [
	# api.views,
	url(r'^contests/$', contest_list, name='contest_list'),
	url(r'^contests/(?P<pk>[0-9]+)$', contest_detail, name='contest_detail'),
]