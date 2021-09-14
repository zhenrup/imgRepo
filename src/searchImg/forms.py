from django import forms
from django.db.models import fields

from .models import img

class imgForm(forms.ModelForm):
	class Meta:
		model = img
		fields = [
			'image_upload',
			'title',
			'characteristics',
			'price'
		]

class rawImgForm(forms.Form):
	image_upload  = forms.ImageField()
	title = forms.CharField()
	# characteristics = forms.ListCharField()
	price = forms.DecimalField()