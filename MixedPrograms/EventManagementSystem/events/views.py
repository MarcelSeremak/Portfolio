from django.shortcuts import  redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import CommentForm, CustomUserCreationForm, EventForm
from .models import Comment, Event
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class HomepageView(FormView):
    template_name = "events/homepage.html"
    form_class = CommentForm
    success_url = "/"
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = list(Comment.objects.order_by("-id"))
        if comments:
            context["comment_first"] = Comment.objects.order_by("-id")[0]
            context["comments"] = Comment.objects.order_by("-id")[1:4]
        else:
            context["comment_first"] = None  # No comments available
            context["comments"] = []  # Empty list of comments
        return context

class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', 'time')
        allowed_sort_fields = ['time', 'place', 'title', 'creator__username']
        if sort_by not in allowed_sort_fields:
            sort_by = 'time'
        return Event.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = self.get_queryset()
        events_data = []
        for event in events:
            place_coords = event.place.split(',')
            place_lat = float(place_coords[0])
            place_lng = float(place_coords[1])
            events_data.append({
                'id': event.id,
                'title': event.title,
                'subtitle': event.subtitle,
                'place_lat': place_lat,
                'place_lng': place_lng,
                'time': event.time.isoformat(),
                'creator_username': event.creator.username,
            })
        context['events_data'] = json.dumps(events_data, cls=DjangoJSONEncoder)
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        return Event.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_object = Event.objects.get(slug=self.kwargs['slug'])
        event_data = []
        place_coords = event_object.place.split(',')
        place_lat = float(place_coords[0])
        place_lng = float(place_coords[1])
        event_data.append({
            'id': event_object.id,
            'title': event_object.title,
            'subtitle': event_object.subtitle,
            'place_lat': place_lat,
            'place_lng': place_lng,
            'time': event_object.time.isoformat(),
            'creator_username': event_object.creator.username,
            })
        context['events_data'] = json.dumps(event_data, cls=DjangoJSONEncoder)
        return context

class RegisterView(FormView):
    template_name = 'events/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'events/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('homepage')

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        place = self.request.POST.get('place')
        if place:
            form.instance.place = place

        return super().form_valid(form)