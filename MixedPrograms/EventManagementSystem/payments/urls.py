from django.urls import path
from . import views
from events.models import Event

urlpatterns = [
    path('cart/<int:event_id>', views.CartView.as_view(), name='cart'),
    path('cart', views.CartWithoutAddingView.as_view(), name='cart_without_adding'),
    path('cart/delete/<int:ticket_id>/', views.DeleteTicketView.as_view(), name='delete_ticket'),
]