from django.urls import path
from .views import AccountView,User

urlpatterns = [
    path("", AccountView.as_view(), name="account"),
    path("user/",User.as_view(), name="post_list"),
]
