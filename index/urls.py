from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #/homes/12
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'home/add/$', views.HomeCreate.as_view(), name = 'home-add'),
]
