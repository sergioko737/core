from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reg_form, name='reg_form'),
    url(r'^core/reg_success.html$', views.reg_success, name='reg_success'),
]
