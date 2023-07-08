from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("cart", views.cart, name="cart"),
      path("payment", views.payment, name="payment"),
   
]
