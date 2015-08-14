from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'beyond.views.home', name='home'),
    url(r'^about/$', 'beyond.views.about', name='about'),
    url(r'^make_order', 'beyond.views.make_order', name='order'),
    url(r'^pictures_catalog/$', 'beyond.views.pictures', name='pictures'),
    url(r'^pictures_catalog/(?P<category_id>[0-9]+)/$', 'beyond.views.pictures', name='pictures'),
    url(r'^pictures/(?P<picture_id>[0-9]+)/$', 'beyond.views.show_picture', name='picture'),
    url(r'^cart/$', 'beyond.views.cart', name='cart'),
    url(r'^add_to_cart/(?P<picture_id>[0-9]+)/$', 'beyond.views.add_to_cart', name='add_to_cart'),
    url(r'^remove_from_cart/(?P<picture_id>[0-9]+)/$', 'beyond.views.delete_from_cart', name='delete_from_cart'),
    url(r'^clear_cart/$', 'beyond.views.clear_cart', name='clear_cart'),
]
