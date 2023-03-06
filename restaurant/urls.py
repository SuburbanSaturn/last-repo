from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('user/', views.userView.as_view()), 
]