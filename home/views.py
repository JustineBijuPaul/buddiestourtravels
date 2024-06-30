import email
from django.shortcuts import render, redirect , HttpResponse
from home.models import Detail, Location, Package, Gallery
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


# Create your views here.
def index(request):
	try:
		packageObject = Package.objects.all()
	except ObjectDoesNotExist:
		return HttpResponse(status = 404)
	if request.method =="POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		detail = Detail(name=name,email=email,message=message)
		detail.save()
		return render(request, "contact/success.html")
	return render(request,'index.html', {'packages' : packageObject}) 
def gallery(request):
	try:
		galleryItems = Gallery.objects.all()
	except ObjectDoesNotExist:
		return HttpResponse(status = 404)
	return render(request,'gallery/gallery2.html', {'gallery' : galleryItems})
def order(request, package):
	if request.method == 'POST':
		form = True
		if form:
			try:
				packageObject = Package.objects.get(slug = package)
				loc = packageObject.location_set.get(id = request.POST.get('location', 0))
			except ObjectDoesNotExist:
				return redirect("/error")
			subject = "Website Inquiry"
			body = "New Booking from {name} \n\n Name : {name} \n E-mail : {email} \n Phone : {phone} \n Package : {package} \n Selected Location : {location} \n Departure : {departure} \n Requested Date : {departure_day}/{departure_month}/{departure_year}".format(name = request.POST.get('name', 'Unknown'), phone = request.POST.get('phone', 'Unknown'), email = request.POST.get('email', 'Unknown'), departure = request.POST.get('departure', 'Unknown'), departure_day = request.POST.get('departure_day', 'Unknown'), departure_month = request.POST.get('departure_month', 'Unknown'), departure_year = request.POST.get('departure_year', 'Unknown'), package = packageObject.title, location = loc.title)

			try:
				send_mail(subject, body, 'admin@buddiestourlines.com', ['info@buddiestourlines.com']) 
			except BadHeaderError:
				return render(request, "contact/failed.html")
			return render(request, "contact/success.html")
	# print(package)
	try:
		packageObject = Package.objects.get(slug = package)
		locations = packageObject.location_set.all()
	except ObjectDoesNotExist:
		return HttpResponse(status = 404)
	return render(request,'packages/order/index.html', {'package' : packageObject, 'locations' : locations})
def success(request):
	return render(request,'contact/success.html')
def failed(request):
	return render(request,'contact/failed.html')

# Contact request handler.
def contact(request):
	# POST request handler
	
	# GET request handler.
	return render(request, "contact/index.html")

def maingallery(request):
	try:
		galleryItems = Gallery.objects.all()
	except ObjectDoesNotExist:
		return HttpResponse(status = 404)
	return render(request,'gallery/maingallery.html', {'maingallery' : galleryItems})