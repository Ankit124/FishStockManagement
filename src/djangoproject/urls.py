from django.contrib import admin
from django.urls import path
from fishmgt import views


urlpatterns = [
    path('', views.home, name='home'),
    path('list_item/', views.list_item, name='list_item'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('admin/', admin.site.urls),
]
