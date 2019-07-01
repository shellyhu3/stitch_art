from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', views.admin),
    url(r'^process_login$', views.login),
    url(r'^logout', views.logout),
    url(r'^about$', views.about),
    url(r'^services$', views.services),
    url(r'^shop$', views.shop),
    url(r'^gallery', views.gallery),
    url(r'^delete_img$', views.delete_img),
    url(r'^upload', views.upload),
    url(r'^contact', views.contact)
]