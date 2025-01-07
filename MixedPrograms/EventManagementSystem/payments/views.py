from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView, CreateView, ListView, DetailView
from .models import Ticket
from events.models import Event
# Create your views here.

class CartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=self.kwargs['event_id'])

        ticket_from_now = Ticket(event=event, user=request.user)
        ticket_from_now.save()
        user_tickets = Ticket.objects.filter(user=request.user)

        total_amount=0
        for ticket in user_tickets:
            total_amount += float(ticket.event.price)
        context = {
            'user_tickets': user_tickets,
            'total_amount': total_amount
        }
        return render(request, 'payments/cart.html', context)

    def post(self, request, *args, **kwargs):
        user_tickets = Ticket.objects.filter(user=request.user)
        for ticket in user_tickets:
            event = ticket.event
            event.tickets_amount -= 1
            event.save()
            ticket.delete()
        return redirect('cart_without_adding')


class CartWithoutAddingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_tickets = Ticket.objects.filter(user=request.user)

        total_amount=0
        for ticket in user_tickets:
            total_amount += float(ticket.event.price)
        context = {
            'user_tickets': user_tickets,
            'total_amount': total_amount
        }
        return render(request, 'payments/cart.html', context)

    def post(self, request, *args, **kwargs):
        user_tickets = Ticket.objects.filter(user=request.user)
        for ticket in user_tickets:
            event = ticket.event
            event.tickets_amount -= 1
            event.save()
            ticket.delete()
        return redirect('cart_without_adding')

class DeleteTicketView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk=self.kwargs['ticket_id'], user=request.user)
        ticket.delete()
        return redirect('cart_without_adding')