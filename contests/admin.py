from django.contrib import admin
from .models import Contest
from .forms import ContestForm

# Register your models here.

class ContestAdmin(admin.ModelAdmin):
	list_display = ['id',"__unicode__","timestamp"]
	form = ContestForm

admin.site.register(Contest,ContestAdmin)
