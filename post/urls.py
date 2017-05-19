from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.pos_list, name='pos_list'),
    url(r'^homepage$', views.pos_list, name='pos_list'),
    url(r'^shopping_list$', views.shopping_list, name='shopping_list'),
    url(r'^shopping_cart$', views.shopping_cart, name='shopping_cart'),
    url(r'^go$', views.go, name='go'),



]
