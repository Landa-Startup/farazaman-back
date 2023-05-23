from .views import ContactViewSet, StartupSubmitViewSet, StartupViewSet, EventViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register('startups', StartupViewSet, basename='startups')
router.register('contact', StartupViewSet, basename='contact')
router.register('startup-submit', StartupSubmitViewSet, basename='startup-submit')
router.register('events', EventViewSet, basename='events')


contact_router = routers.DefaultRouter('contact')
contact_router.register(r'contact', ContactViewSet)


startups_router = routers.DefaultRouter('startups')
startups_router.register(r'startups', StartupViewSet)


startup_submit_router = routers.DefaultRouter('startup-submit')
startup_submit_router.register(r'startup-submit', StartupSubmitViewSet)

events_router = routers.DefaultRouter('events')
events_router.register(r'events', EventViewSet)


urlpatterns = router.urls + startups_router.urls + contact_router.urls + startup_submit_router.urls

