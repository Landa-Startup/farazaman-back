from .views import StartupSubmitViewSet, StartupViewSet, EventViewSet, ContactViewSet, HireViewSet, EventAttendeesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('startups', StartupViewSet, basename='startups')
router.register('contact', ContactViewSet, basename='contact')
router.register('hire', HireViewSet, basename='hire')
router.register('startup-submit', StartupSubmitViewSet,
                basename='startup-submit')
router.register('events', EventViewSet, basename='events')
router.register('attendees', EventAttendeesViewSet, basename='attendees')


contact_router = routers.DefaultRouter('contact')
contact_router.register(r'contact', ContactViewSet)


hire_router = routers.DefaultRouter('hire')
hire_router.register(r'hire', HireViewSet)

startups_router = routers.DefaultRouter('startups')
startups_router.register(r'startups', StartupViewSet)

startup_submit_router = routers.DefaultRouter('startup-submit')
startup_submit_router.register(r'startup-submit', StartupSubmitViewSet)

events_router = routers.DefaultRouter('events')
events_router.register(r'events', EventViewSet)

attendees_router = routers.DefaultRouter('attendees')
router.register(r'attendees', EventAttendeesViewSet)


urlpatterns = router.urls + startups_router.urls + \
    contact_router.urls + startup_submit_router.urls

