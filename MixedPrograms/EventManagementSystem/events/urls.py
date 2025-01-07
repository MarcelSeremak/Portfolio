from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/create', views.EventCreateView.as_view(), name='create_event'),
    path('events/<slug:slug>', views.EventDetailView.as_view(), name='event_detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]