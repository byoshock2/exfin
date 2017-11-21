from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.materia_new, name='materia_new'),

]
