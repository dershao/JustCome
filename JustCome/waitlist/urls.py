from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^waitlist/home', views.home, name="home"),
    url(r'^waitlist/enque', views.enque),
    url(r'^waitlist/success/', views.success, name="success"),
=======
    url(r'^waitlist/dequeue', views.dequeue)
>>>>>>> 50f3cd2c187913c0b9c3fccc7523adf5550619e1
]
