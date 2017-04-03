from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Contest

class ContestForm(forms.ModelForm):

	class Meta:
		model = Contest
		fields = ['id','hashtag_1','hashtag_2','start_time','end_time']
		start_date = forms.DateField(widget=AdminDateWidget())
		end_date = forms.DateField(widget=AdminDateWidget())

		