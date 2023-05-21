from django.contrib import admin
from django.urls import path, include
from .views import index, ContactViewSet, StartupSubmitViewSet, StartupViewSet
from rest_framework import routers
#import as_view 



router = routers.DefaultRouter()
#include all urls from router


#router.register(r'startupSubmit', StartupSubmitViewSet)
#router.register(r'startups', StartupViewSet)

contact_router = routers.DefaultRouter()
contact_router.register(r'contact', ContactViewSet)

startups_router = routers.DefaultRouter()
startups_router.register(r'startups', StartupViewSet)
startups_router.register(r'startup-submit', StartupSubmitViewSet)




urlpatterns = router.urls + startups_router.urls + contact_router.urls

# urlpatterns = [
#     path('', index, name="index"),
#     #path('startups/', startups, name="startups"),
#     path('startups/', include(router.urls)),
#     path('form/', include(router.urls))
# ]
