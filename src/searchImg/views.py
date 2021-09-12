from django.shortcuts import render
from .models import img
from .forms import imgForm

# Create your views here.
def home_view(request, *args, **kwargs):
	my_context = {
		"title_name": "a picture",
		"price": 2.99,
		"chara": ['happy', 'love', 'students']
	}

	return render(request, "home.html", my_context)


# use data from db
def img_detail_view(request):
	obj = img.objects.get(id = 1)
	# context = {
	# 	'title': obj.title,
	# 	'price': obj.price,
	# 	'output_image': obj.image_upload,
	# }
	context = {
		'obj': obj,
	}
	return render(request, "img/img_detail.html", context)

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
	return render(request, "img/img_create.html", context)