from django import forms
from .models import Forecast
from django.contrib.auth.models import User
from PIL import Image

class ForecastForm(forms.ModelForm):

	class Meta:
		model = Forecast
		fields = ['day', 'date', 'high', 'low', 'average', 'wind']
