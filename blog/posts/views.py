from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

dummy_data = [
    {
        "id": 1,
        "name": "Alice",
        "age": 28,
        "email": "alice@example.com",
        "is_active": True,
        "roles": ["admin", "editor"],
        "profile": {
            "bio": "Loves coding and coffee.",
            "location": "New York"
        }
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 35,
        "email": "bob@example.com",
        "is_active": False,
        "roles": ["viewer"],
        "profile": {
            "bio": "Enjoys hiking and photography.",
            "location": "San Francisco"
        }
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 22,
        "email": "charlie@example.com",
        "is_active": True,
        "roles": ["editor", "contributor"],
        "profile": {
            "bio": "Aspiring writer and musician.",
            "location": "Chicago"
        }
    }
]


def sayHello(request):
    return HttpResponse("Hello, World!")


def sayHi(request,name):
    return HttpResponse(f"Hi, {name}!")  

def capOnlyInt(request, number):

   return HttpResponse(f"Only in {number}!")


def homePage(request):
    return render(request, 'posts/home.html',{
        "content": "Welcome to the home page of the blog!",
    })

def getDummyData(request):
    return render(request, 'posts/dummy_data.html', {
        "data": dummy_data,
    })


def global_view(request):
    return render(request, 'global.html')


