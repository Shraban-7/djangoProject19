from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = 'tuition/home.html'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex ['msg'] = 'Welcome to our website '
        return contex