from .views import StartupSubmitViewSet, StartupViewSet, EventViewSet, ContactViewSet, HireViewSet, EventAttendeesViewSet, WorkSpaceViewSet, InternshipViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('startups', StartupViewSet, basename='startups')
router.register('contact', ContactViewSet, basename='contact')
router.register('hire', HireViewSet, basename='hire')
router.register('startup-submit', StartupSubmitViewSet,
                basename='startup-submit')
router.register('events', EventViewSet, basename='events')
router.register('attendees', EventAttendeesViewSet, basename='attendees')
router.register('workspace', WorkSpaceViewSet, basename='workspace')


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

workspace_router = routers.DefaultRouter('workspace')
router.register(r'workspace', WorkSpaceViewSet)

internship_router = routers.DefaultRouter('internship')
router.register(r'workspace', InternshipViewSet)


urlpatterns = router.urls + startups_router.urls + \
    contact_router.urls + startup_submit_router.urls+ internship_router.urls + workspace_router.urls + attendees_router.urls

