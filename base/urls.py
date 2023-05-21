from django.contrib import admin
from django.urls import path, include
from .views import index, ContactViewSet, StartupSubmitViewSet, startups, startupsDetail
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)
router.register(r'startupSubmit', StartupSubmitViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('startups/', startups, name="startups"),
    path('startups/<str:pk>', startupsDetail, name="startups"),
    path('form/', include(router.urls))
]
