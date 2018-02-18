from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^waitlist/home', views.home, name="home"),
    url(r'^waitlist/enque', views.enque),
    url(r'^waitlist/success/', views.success, name="success"),
    url(r'^waitlist/dequeue', views.dequeue)
]
