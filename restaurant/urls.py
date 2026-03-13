from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet

urlpatterns = [
    path('', index, name='index'),
    path('menu/item/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]

