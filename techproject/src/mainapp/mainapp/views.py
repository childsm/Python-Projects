from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    #print(request.user) #we are going to print (to the consol) who the user is
    #user = request.user
    #return HttpResponse("<h1>Welcome {}!</h1>".format(user))
    #user = request.user
    context = {
        'products': products,
    }
    # user in 'user' is the key and you get the value user above
    return render(request, "home.html", context) #context instead of {} to create dictionary
    #render in browser, pass in request obj, pass in file, {} returns some info back
