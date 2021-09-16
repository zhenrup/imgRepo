from django.shortcuts import render
from .models import img
from .forms import imgForm
from django.core.exceptions import *
from django.views.generic import DetailView


# Create your views here.
def home_view(request, *args, **kwargs):
	my_context = {
		
	}

	return render(request, "home.html", my_context)


# trying to get input and send something back to the page
def img_detail_view(request):
	if request.method == 'POST':
		input = request.POST.get('imageSearch', None)
		try:
			if len(input.split()) > 1:
				imgObj = img.objects.get(title = input)
				context = {
					'obj': imgObj,
				}
				return render(request, "imgReturn.html", context)

			else:
				result = img.objects.filter(title__contains=input).values_list('title', 'image_upload', 'price', 'seller')
				if len(result) == 0:
					context = {
					'errorM': "cannot find any image with this keyword",
					}
					return render(request, "searchImg.html", context)
				else: 
					context = {
						'obj': result,
					}
					return render(request, "imgReturn.html", context)

		except img.DoesNotExist:
			context = {
				'errorM': "cannot find any image with this title",
			}
			return render(request, "searchImg.html", context)

	else:
		return render(request, "searchImg.html")



# allow user to create their own product
def img_create_view(request):
	form = imgForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = imgForm()
	context = {
		'form': form,
	}
	return render(request, "createImg.html", context)

# def img_create_view(request):
	
# 	context = {}
# 	return render(request, "createImg.html", context)