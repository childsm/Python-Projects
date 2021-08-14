from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    names = ["Shari", "Adam", "Olive", "Stan", "Percy", "Walter", "Faith", "Victor"]
    #print(request.user) #we are going to print (to the consol) who the user is
    user = request.user
    context = {
        'names': names,
    }
    return render(request, "home.html", context)
