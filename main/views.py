from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"

class MenuPageView(TemplateView):
    template_name = "menu.html"

class ReservationPageView(TemplateView):
    template_name = "reservation.html"
