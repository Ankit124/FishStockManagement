from django.db import models

# Create your models here.
species_choice = (
		('Big Eye', 'Big Fish'),
		('small', 'cichlid'),
		('qwe', 'abc'),
	)
# class Species(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     def __str__(self):
#         return self.name


class Stock(models.Model):
    # species = models.ForeignKey(Species, on_delete=models.CASCADE)
    species = models.CharField(max_length=50, blank=True, unique=True, null=True)
    name = models.CharField(max_length=50, blank=True, unique=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=True)
    length = models.IntegerField(default='0', blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    #export_to_CSV = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name