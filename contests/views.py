import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Contest

# def home(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


class ContestListView(ListView):
	model = Contest
	queryset = Contest.objects.all()
