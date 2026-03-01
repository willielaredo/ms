from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organizations/', views.organizations, name='organizations'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('organization/<int:pk>', views.OrganizationDetailView.as_view(), name='organization-detail'),
]

urlpatterns += [
    path('myevents/', views.EventsFollowedByUserListView.as_view(), name='my-events'),
]

urlpatterns += [
    path('follow-event/<int:pk>/', views.follow_event, name='follow_event'),
]

urlpatterns += [
    path('unfollow-event/<int:pk>/', views.unfollow_event, name='unfollow_event'),
]