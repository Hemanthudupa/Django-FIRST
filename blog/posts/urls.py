from django.urls import path
from . import views

urlpatterns = [
    path("sayHello/", views.sayHello),
    path("hi/<name>/", views.sayHi),
    path("<int:number>/", views.capOnlyInt),
    path("",views.homePage),
    path("dummy/", views.getDummyData, name="dummy_data"),
]
