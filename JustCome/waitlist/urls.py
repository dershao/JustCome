from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^waitlist/home', views.home, name='home'),
    url(r'^waitlist/enqueue', views.enqueue),
    url(r'^waitlist/dequeue', views.dequeue),
    url(r'^waitlist/reply', views.reply)
]
