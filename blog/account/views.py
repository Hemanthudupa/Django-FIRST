from django.shortcuts import render
from rest_framework.views import APIView
from json import loads
from account.models import User as UserModel


# Create your views here.
class AccountView(APIView):
    def get(self, request):
        username = request.GET.get("username") 
        return render(request, "account/account.html", {"username": username})
    def post(self,request):
        print("Received POST request")
        username,password=loads(request.body.decode("utf-8"))
        print(f"Username: {username}, Password: {password}")
        return render (request, "account/account.html", {"username": username, "password": password})
    

class User(APIView):
    def post(self,request):
      username,password,email=(request.data.get("username"),request.data.get("password"),request.data.get("email"))
      user = UserModel.objects.create(username=username, password=password, email=email)
      
      return render(request, "account/user.html", {"user": user})
