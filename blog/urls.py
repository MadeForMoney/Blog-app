from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path("ind",views.index,name='index'),
    path("post/detail/<str:slug>",views.detail,name='detail'),
    path("old_url",views.old_url_red,name='old_url'),
    path("new_url_some",views.new_url_red,name='new_url'),
    path("contact",views.contact_view,name='contact'),
    path("about",views.about_view,name='about')
]