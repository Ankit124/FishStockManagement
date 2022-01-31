from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['species', 'name', 'quantity','length','latitude','longitude']

	def clean_species(self):
		species = self.cleaned_data.get('species')
		if not species:
			raise forms.ValidationError('This field is required')
		return species

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

class StockSearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ['species', 'name']


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['species', 'name', 'quantity','length','latitude','longitude']