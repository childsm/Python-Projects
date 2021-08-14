from django.shortcuts import render
from django.http import HttpResponse
from .import views
from .models import Profiles

def admin_console(request):
    profiles = Profiles.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})

# Create your views here.
