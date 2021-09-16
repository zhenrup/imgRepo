from django import forms
from django.db.models import fields

from .models import img

class imgForm(forms.ModelForm):
	class Meta:
		model = img
		fields = [
			'image_upload',
			'title',
			'price',
			'discount',
			'seller'
		]

class rawImgForm(forms.Form):
	image_upload  = forms.ImageField()
	title = forms.CharField()
	price = forms.DecimalField()
	discount = forms.IntegerField()
	seller = forms.CharField()