from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #/homes/12
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #add home
    url(r'home/add/$', views.HomeCreate.as_view(), name ='home-add'),

    # update home
    url(r'index/(?P<pk>[0-9]+)/$', views.HomeUpdate.as_view(), name='home-update'),

    # delete home
    url(r'index/(?P<pk>[0-9]+)/delete/$', views.HomeDelete.as_view(), name='home-delete'),


]
