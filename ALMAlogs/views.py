from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Line

class HomeTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        logs = Line.objects.all()

        context['message'] = "Hello World"
        context['logs'] = logs
        return context

# Create your views here.
