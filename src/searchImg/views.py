from django.shortcuts import render
from .models import img
from .forms import imgForm
from django.shortcuts import HttpResponse
from django.core.exceptions import *

# Create your views here.
def home_view(request, *args, **kwargs):
	my_context = {
		"title_name": "a picture",
		"price": 2.99,
		"chara": ['happy', 'love', 'students']
	}

	return render(request, "home.html", my_context)


# trying to get input and send something back to the page
def img_detail_view(request):
	if request.method == 'POST':
		input = request.POST.get('imageSearch', None)
		try:
			imgObj = img.objects.get(title = input)
			context = {
				'obj': imgObj,
			}
			return render(request, "returnImg.html", context)
		except img.DoesNotExist:
			context = {
				'errorM': "cannot find any image with this keyword",
			}
			return render(request, "returnImg.html", context)

	else:
		return render(request, "returnImg.html")



# allow user to create their own product
# def img_create_view(request):
# 	form = imgForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = imgForm()
# 	context = {
# 		'form': form,
# 	}
# 	return render(request, "img/img_create.html", context)

def img_create_view(request):
	
	context = {}
	return render(request, "createImg.html", context)