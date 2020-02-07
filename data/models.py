from django.db import models

class Forecast(models.Model):
	monday = 'monday'
	tuesday = 'tuesday'
	wednesday = 'wednesday'
	thursday = 'thursday'
	friday = 'friday'
	saturday = 'saturday'
	sunday = 'sunday'

	day_choices = (
		(monday, 'monday'),
		(tuesday, 'tuesday'),
		(wednesday, 'wednesday'),
		(thursday, 'thursday'),
		(friday, 'friday'),
		(saturday, 'saturday'),
		(sunday, 'sunday'),
	)

	day = models.CharField(max_length=20, choices=day_choices, default=monday)
	date = models.DateField()
	high = models.IntegerField(default=1)
	low = models.IntegerField(default=1)
	average = models.FloatField()
	wind = models.IntegerField(default=1)
