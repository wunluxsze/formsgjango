from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def postuser(request):
    name = request.POST.get("Name", "Undefined")
    email = request.POST.get("Email", "Undefined")
    phone = request.POST.get("Phone Number", "Undefined")
    service = request.POST.get("Select Service", "Undefined")
    about = request.POST.get("about", "Undefined")
    return HttpResponse(f"<h2> name: {name} email: {email} phone: {phone} service: {service} about: {about} </h2>")
