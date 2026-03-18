from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("menu-items/", views.MenuItemItemView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemItemView.as_view()),
    path("message/", views.message),
    path("api-token-auth/", obtain_auth_token)
    
]
