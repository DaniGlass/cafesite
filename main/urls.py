# howdy/urls.py
from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^menu/$', views.MenuPageView.as_view()),
    url(r'^reservation/$', views.ReservationPageView.as_view()),
]
