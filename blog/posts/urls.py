from django.urls import path
from . import views

urlpatterns = [
    path("sayHello/", views.sayHello),
    path("hi/<name>/", views.sayHi),
    path("<int:number>/", views.capOnlyInt),
    path("",views.homePage,name="home"),
    path("dummy/", views.getDummyData, name="dummy_data"),
    path('global/',views.global_view, name='global_view'),

]
