from django.shortcuts import render
from django.views.generic import *
from data.models import Forecast
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models import Q
from .forms import ForecastForm
import json

def index(request):
	return render(request, "data/index.html")

def submit(request):

	form = ForecastForm(request.POST or None)

	data = serializers.serialize('json', Forecast.objects.all())

	if form.is_valid():
		form.save()
		
		context = {
			"data": data,	
		}
		return render(request, 'data/forecast_data.html', context)

	context = {
		"form": form,
	}
	
	return render(request, 'data/submit.html', context)


class forecast_data(ListView):

	template_name = 'data/forecast_data.html'
	model = Forecast

	def get(self, request, *args, **kwargs):

		data = serializers.serialize('json', Forecast.objects.all())

		context = {
			"data": data,	
		}

		return render(request, 'data/forecast_data.html', context)