from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"submit", views.submit, name='submit')
    #url(r'^$', include('seminar.urls')),
]