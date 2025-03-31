from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.first_page,name='first-page'),
    path('<int:chai_id>/',views.chai_detail,name="chai-detail"),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]